import streamlit as st

# ---- CONFIGURACIÓN DE LA PÁGINA ----
st.set_page_config(page_title="Mi Primera App", page_icon="⚽", layout="centered")

# ---- TRUCO PARA OCULTAR ELEMENTOS DE STREAMLIT ----
hide_style = """
    <style>
    /* Ocultar el botón de GitHub (Fork) en la esquina superior derecha */
    .stAppDeployButton {visibility: hidden;}
    
    /* Ocultar la barra de menú superior y el ícono de GitHub */
    header {visibility: hidden;}
    
    /* Ocultar el pie de página de Streamlit de abajo */
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Título de la página web
st.title("⚽ ¡Mi Primera App Interactiva!")

# Subtítulo explicativo
st.markdown("---")
st.subheader("¡El entorno de Python y Streamlit está al 100%!")

# Un componente interactivo: Caja de texto para ingresar datos
nombre_usuario = st.text_input("Por favor, introduce tu nombre:")

# Si el usuario escribe algo, la app reacciona en tiempo real
if nombre_usuario:
    st.success(f"¡Excelente trabajo, {nombre_usuario}! Acabas de levantar tu primer frontend con Python puro.")
    
    # Añadimos un botón de celebración interactivo
    if st.button("¡Celebrar!"):
        st.balloons()
