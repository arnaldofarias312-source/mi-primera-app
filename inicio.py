import streamlit as st

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