import pickle

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


@st.cache_resource
def load_model():
    with open('models/modelLSTM.pkl', 'rb') as model_file:
        model_pkl = pickle.load(model_file)
    return model_pkl


st.set_page_config(page_title="Proyecto final DLA", page_icon=":robot_face:")

st.markdown("# Proyecto final DLA :notebook:")
st.markdown("---")
st.markdown("Este proyecto busca predecir el valor siguiente al último de una serie de tiempo"
            "utilizando una red neuronal recurrente, aplicando lo aprendido en la materia de "
            "deep learning avanzado")

st.markdown("## Aquí cargamos series de tiempo")
st.markdown("---")
st.markdown("La serie de tiempo a cargar debe estar en formato xlsx, que será posteriormente"
            "utilizado para realizar la predicción mediante la red neuronal recurrente")

file = st.file_uploader("Sube un archivo .xlsx", type="xlsx")

if file:
    df = pd.read_excel(file)
    st.success("El archivo fue cargado con éxito")
    st.markdown(f"Datos del archivo **{file.name}**: ")
    st.dataframe(df)

st.markdown("## A predecir!")
st.markdown("---")

pred_btn, clear_btn = st.columns(2)
pred_clicked = pred_btn.button("Predecir")

prediction = None

if pred_clicked:
    model = load_model()
    prediction = model.predict()


'''
def plot_series(series, y=None, y_pred=None, y_pred_std=None, x_label="$t$", y_label="$x$"):
    r, c = 3, 5
    fig, axes = plt.subplots(nrows=r, ncols=c, sharey=True, sharex=True, figsize=(20, 10))
    for row in range(r):
        for col in range(c):
            plt.sca(axes[row][col])
            ix = col + row * c
            plt.plot(series[ix, :], ".-")
            if y is not None:
                plt.plot(range(len(series[ix, :]), len(series[ix, :]) + len(y[ix])), y[ix], "bx", markersize=10)
            if y_pred is not None:
                plt.plot(range(len(series[ix, :]), len(series[ix, :]) + len(y_pred[ix])), y_pred[ix], "ro")
            if y_pred_std is not None:
                plt.plot(range(len(series[ix, :]), len(series[ix, :]) + len(y_pred[ix])), y_pred[ix] + y_pred_std[ix])
                plt.plot(range(len(series[ix, :]), len(series[ix, :]) + len(y_pred[ix])), y_pred[ix] - y_pred_std[ix])
            plt.grid(True)
            plt.hlines(0, 0, 100, linewidth=1)
            plt.axis([0, len(series[ix, :]) + len(y[ix]), -1, 1])
            if x_label and row == r - 1:
                plt.xlabel(x_label, fontsize=16)
            if y_label and col == 0:
                plt.ylabel(y_label, fontsize=16, rotation=0)
    return plt
'''


if file:
    df = pd.read_excel(file)
    print(df['Date'].values.shape)