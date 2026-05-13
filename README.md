# vehicles_env
Creación y gestión de entornos virtuales de Python y el desarrollo de una aplicación web.

# Sprint 7 - Proyecto: Aplicación web para análisis de anuncios de vehículos

## Descripción del proyecto

Este proyecto forma parte del Sprint 7 y tiene como objetivo desarrollar una aplicación web interactiva utilizando Python, Streamlit, pandas y Plotly.

El conjunto de datos utilizado contiene anuncios de venta de vehículos usados en Estados Unidos. A partir de estos datos se realiza un análisis exploratorio y se construye una aplicación web que permite visualizar información relevante sobre los vehículos publicados, como el kilometraje, el precio, la condición y otras características.

La aplicación permite al usuario generar visualizaciones interactivas mediante casillas de verificación, facilitando la exploración básica del conjunto de datos.

## Tecnologías utilizadas

- Python
- pandas
- Plotly
- Streamlit
- Jupyter Notebook
- Git y GitHub
- Render para el despliegue web

## Estructura del proyecto

```text
vehicle_env/
├── notebooks/
│   └── EDA.ipynb
├── app.py
├── requirements.txt
├── vehicles_us.csv
└── README.md
```

## Archivos principales

### `vehicles_us.csv`

Archivo que contiene el conjunto de datos de anuncios de venta de vehículos usados.

### `notebooks/EDA.ipynb`

Notebook utilizado para realizar el análisis exploratorio de datos. En este archivo se revisa la estructura del dataset, los valores ausentes, las variables principales y se generan visualizaciones iniciales con Plotly.

### `app.py`

Archivo principal de la aplicación web desarrollada con Streamlit. La aplicación carga el dataset y permite construir visualizaciones interactivas.

### `requirements.txt`

Archivo que contiene las dependencias necesarias para ejecutar el proyecto.

## Análisis exploratorio de datos

Durante el análisis exploratorio se revisaron aspectos generales del conjunto de datos, incluyendo:

- Número de filas y columnas.
- Tipos de datos.
- Valores ausentes.
- Distribución del precio de los vehículos.
- Distribución del kilometraje.
- Relación entre precio y odómetro.
- Comparación de precios según la condición del vehículo.
- Frecuencia de anuncios por tipo de vehículo.

Este análisis permitió identificar patrones generales y seleccionar visualizaciones útiles para la aplicación web.

## Visualizaciones incluidas en la aplicación

La aplicación web desarrollada con Streamlit permite explorar el conjunto de datos de anuncios de vehículos usados mediante visualizaciones interactivas creadas con Plotly.

Las visualizaciones disponibles son:

- Distribución del precio de los vehículos.
- Distribución del kilometraje registrado en el odómetro.
- Relación entre precio y odómetro mediante un gráfico de dispersión.
- Comparación de precios según la condición del vehículo.
- Frecuencia de anuncios por tipo de vehículo.

La aplicación incluye un panel lateral con casillas de verificación para activar o desactivar cada gráfica. También cuenta con una opción para limitar valores extremos y mejorar la lectura visual de los gráficos.


## Instalación local

Para ejecutar el proyecto localmente, primero clona el repositorio:

```bash
git clone https://github.com/Eldocdou/vehicles_env.git
```

Entra al directorio del proyecto:

```bash
cd vehicles_env
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución local de la aplicación

Para ejecutar la aplicación Streamlit, usa el siguiente comando:

```bash
streamlit run app.py
```

Después de ejecutar el comando, Streamlit abrirá la aplicación en el navegador.

## Despliegue

La aplicación está preparada para ser desplegada en Render.

Para desplegarla, se debe conectar el repositorio de GitHub con Render y configurar el servicio web con los siguientes parámetros:

```text
Build Command:
pip install -r requirements.txt

Start Command:
streamlit run app.py
```

URL de la aplicación desplegada:

```text
https://vehicles-dashboard-z0h2.onrender.com.
```

## Conclusiones

Este proyecto permitió aplicar un flujo completo de trabajo para el desarrollo de una aplicación web de análisis de datos.

Se trabajó con un entorno de desarrollo en Python, se realizó un análisis exploratorio mediante Jupyter Notebook y se construyó una aplicación web interactiva con Streamlit. Además, el proyecto fue versionado con Git y preparado para su despliegue en Render.

La aplicación final ofrece una forma sencilla de explorar visualmente los anuncios de vehículos usados y analizar relaciones básicas entre variables como el precio, el kilometraje y la condición del vehículo.

## Autor

Proyecto desarrollado por J. Abel Saucedo Velázquez como parte del Sprint 7.