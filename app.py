import pickle

import pandas as pd
import streamlit as st


@st.cache_resource
def load_model():
    with open('models/modelLSTM1.pkl', 'rb') as model_file:
        model_pkl = pickle.load(model_file)
    return model_pkl


st.set_page_config(page_title="Proyecto final DLA", page_icon=":robot_face:")

st.markdown("# Proyecto final DLA :notebook:")
st.markdown("## Predicción de kilometros a recorrer por una persona :runner:")
st.markdown("---")
st.markdown("Este proyecto busca predecir el valor siguiente al último de una serie de tiempo"
            "utilizando una red neuronal recurrente, aplicando lo aprendido en la materia de "
            "deep learning avanzado")

st.markdown("## Aquí cargamos series de tiempo")
st.markdown("---")
st.markdown("La serie de tiempo a cargar debe estar en formato xlsx, que será posteriormente "
            "utilizado para realizar la predicción mediante la red neuronal recurrente, el dataframe "
            "debe tener una columna con nombre 'Date' y una con nombre 'Kilometers' para un "
            "correcto funcionamiento.")

file = st.file_uploader("Sube un archivo .xlsx", type="xlsx")

if file:
    df = pd.read_excel(file)
    st.sidebar.success(f"El archivo **{file.name}** fue cargado con éxito")
    st.markdown(f"Datos del archivo **{file.name}**: ")
    st.dataframe(df)
    st.markdown(f"### Gráfica del dataframe **{file.name}**")
    st.markdown("---")
    st.line_chart(df['Kilometers'])

st.markdown("## A predecir!")
st.markdown("---")
st.markdown("Presionando el botón **Predecir** podrá realizar la predicción de su serie de tiempo")

pred_btn, clear_btn = st.columns(2)
pred_clicked = pred_btn.button("Predecir")

prediction = None

if pred_clicked:
    model = load_model()
    prediction = model.predict()

if file:
    df = pd.read_excel(file)
    print(df['Date'].values.shape)
