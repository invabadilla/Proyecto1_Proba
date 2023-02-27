# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""
import math

import numpy as np
import matplotlib.pyplot as plt

#input_dir='C:/Users/PATH/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename='energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
#datos=np.genfromtxt(filename,delimiter=';',skip_header=1, dtype=float)

#alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = range(8,9), dtype=float)
print(datos)

# Su código va aquí...


#Diagrama de cajas
fig = plt.figure(figsize =(30, 10))
plt.boxplot(datos, vert = False)
plt.xlabel("humedad")
plt.title("Diagrama de cajas humedad en el área de lavado")
plt.show()


#Histograma
intervalos = range(math.floor(min(datos)), math.ceil(max(datos)) + 2) #calculamos los extremos de los intervalos
plt.hist(x=datos, bins=intervalos, color='#F2AB6D', rwidth=0.85)
plt.title('Histograma de humedad en el área de lavado')
plt.xlabel('Huemadad')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)

plt.show() #dibujamos el histograma
