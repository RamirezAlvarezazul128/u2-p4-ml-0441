import pandas as pd
import numpy as np
# Ramirez Azul NC = 0441
n_filas = 5
n_columnas = 5 
tag_columnas = tuple('ABCDE') # etiqueta para las columnas de una tupla
print(tag_columnas)
matriz = np.random.randint(1,6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable  df es DataFrame
df = pd.DataFrame(matriz, columns = tag_columnas)
print("---La tabla o DataFrame---NC = 0441")
print(df)
print("---Ramirez Azul NC = 0441---")