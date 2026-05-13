from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# Configuración general de la página
st.set_page_config(
    page_title="Análisis de anuncios de vehículos",
    page_icon="🚗",
    layout="wide",
)


# Lectura del archivo CSV
@st.cache_data
def load_data():
    """Carga el dataset desde la raíz del proyecto."""
    csv_path = Path("vehicles_us.csv")

    if not csv_path.exists():
        st.error("No se encontró el archivo vehicles_us.csv en la raíz del proyecto.")
        st.stop()

    return pd.read_csv(csv_path)


car_data = load_data()


# Encabezado principal
st.header("Análisis exploratorio de anuncios de venta de coches")

st.write(
    "Esta aplicación permite explorar de forma básica el conjunto de datos "
    "de anuncios de vehículos usados."
)

st.write(f"Filas del dataset: {car_data.shape[0]:,}")
st.write(f"Columnas del dataset: {car_data.shape[1]:,}")


# Vista previa opcional
if st.checkbox("Mostrar vista previa de los datos"):
    st.write("Primeras filas del conjunto de datos:")
    st.dataframe(car_data.head())


# Histograma
build_histogram = st.checkbox("Construir histograma del odómetro")

if build_histogram:
    st.write("Histograma de la columna `odometer` para analizar la distribución del kilometraje.")

    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del odómetro",
        labels={"odometer": "Odómetro / millas", "count": "Número de anuncios"},
    )

    st.plotly_chart(fig_hist, use_container_width=True)


# Gráfico de dispersión
build_scatter = st.checkbox("Construir gráfico de dispersión precio vs odómetro")

if build_scatter:
    st.write(
        "Gráfico de dispersión para analizar la relación entre el precio del vehículo "
        "y el kilometraje registrado en el odómetro."
    )

    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        title="Precio vs odómetro",
        labels={
            "odometer": "Odómetro / millas",
            "price": "Precio",
            "condition": "Condición",
        },
        hover_data=["model", "model_year", "type", "fuel", "transmission"],
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
