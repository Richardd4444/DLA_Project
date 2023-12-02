# Proyecto final DLA
Este es el proyecto final de la materia de Deep Learning Avanzado del doctorado en ingeniería 
de la red mutis
---
# Predicción del comportamiento de una línea de tiempo
---
Este proyecto tiene como objetivo predecir 12 valores siguientes de una serie de tiempo cuyos
datos corresponden a los kilometros recorridos por una persona en un lapso de tiempo
## RNN
Este proceso se llevó a cabo mediante una red neuronal recurrente, más específicamente un Long
Short-Term Memory (LSTM) el cual toma los datos de entrenamiento, pasa por una función de 
activación de tipo `ReLu` y por último el modelo se compila con un optimizador `adam`

[![lstm.png](https://i.postimg.cc/FzjCwqbr/lstm.png)](https://postimg.cc/xN1Pz6Fh)

<p align="center">
  <img width="460" height="300" src="https://i.postimg.cc/FzjCwqbr/lstm.png">
</p>
