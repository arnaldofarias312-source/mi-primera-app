import streamlit as st

# ---- CONFIGURACIÓN DE LA PÁGINA ----
st.set_page_config(page_title="Mi Primera App", page_icon="⚽", layout="centered")

# ---- CSS FORZADO PARA MÓVILES Y COMPUTADORAS ----
hide_style = """
    <style>
    /* Ocultar barra superior y botones de desarrollo */
    header {visibility: hidden; display: none !important;}
    .stAppDeployButton {visibility: hidden; display: none !important;}
    
    /* Ocultar TODO el contenedor de la barra de herramientas inferior (Mobile Toolbar) */
    [data-testid="stStatusWidget"] {visibility: hidden; display: none !important;}
    .stDecoration {display: none !important;}
    
    /* Apuntar a los botones flotantes del hosting de Streamlit en la esquina inferior */
    div[data-testid="stConnectionStatus"] {id: hidden; display: none !important;}
    iframe[title="Streamlit popover"] {display: none !important;}
    footer {visibility: hidden; display: none !important;}
    
    /* Quitar espacios extra que deja la barra oculta */
    .stAppToolbar {right: 0px; display: none !important;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# ---- TU CÓDIGO NORMAL CONTINÚA AQUÍ ----

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
