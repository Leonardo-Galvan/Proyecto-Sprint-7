import pandas as pd
import plotly.express as px
import streamlit as st
#Este es un comentario de prueba
# Título de la aplicación
st.header("Análisis de anuncios de venta de coches")

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

st.write("""
Esta aplicación permite explorar un conjunto de datos de anuncios de venta de coches.
Puedes generar visualizaciones interactivas utilizando los controles de abajo.
""")

# Casillas de verificación
show_histogram = st.checkbox("Construir histograma del odómetro")
show_scatter = st.checkbox("Construir gráfico de dispersión (precio vs odómetro)")

# Histograma
if show_histogram:
    st.write("Histograma del kilometraje (odómetro)")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje de los vehículos"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if show_scatter:
    st.write("Gráfico de dispersión: Precio vs Odómetro")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre el precio y el kilometraje"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)