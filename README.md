# Proyecto final DLA
Este es el proyecto final de la materia de Deep Learning Avanzado del doctorado en ingeniería 
de la red mutis.

# Predicción del comportamiento de una línea de tiempo
Este proyecto tiene como objetivo predecir 12 valores siguientes de una serie de tiempo cuyos
datos corresponden a los kilometros recorridos por una persona en un lapso de tiempo.

## RNN
Este proceso se llevó a cabo mediante una red neuronal recurrente, más específicamente un Long
Short-Term Memory (LSTM) el cual toma los datos de entrenamiento, pasa por una función de 
activación de tipo `ReLu` y por último el modelo se compila con un optimizador `adam`.

[![lstm.png](https://i.postimg.cc/FzjCwqbr/lstm.png)](https://postimg.cc/xN1Pz6Fh)

Se escogió un LSTM para este proceso ya que las RNN tienen como uno de sus principales propósitos
predecir el comportamiento de una serie de tiempo y resulta ser mejor que un perceptrón multicapa
ya que la `RNN` no solo tiene el valor del peso de la capa oculta sino también el valor del instante
anterior.

## Streamlit
Este proyecto fue elaborado con el framework de [streamlit](https://streamlit.io/) el está diseñado
para facilitar la creación de aplicaciones de `Machine Learning` o aplicaciones basadas en datos, 
permitiendo de una forma interactiva visualizar y manipular los datos.
