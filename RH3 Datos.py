# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np

input_dir='C:/Users/Rafae/Downloads/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename=input_dir+'energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
#datos=np.genfromtxt(filename,delimiter=';',skip_header=1)
datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = range(8,9))
#datos=np.loadtxt(filename,delimiter=',',skiprows=1)

#alternativamente, se pueden leer columnas específicas entre el rango [X,Y] de esta forma:
#datos=np.genfromtxt(filename,delimiter=',',skip_header=1, usecols = range(X,Y))

# Su código va aquí...


data = sorted(datos)
n = np.size(datos)



#Datos de tendencia

    #Promedio
promedio = datos.mean()
print ('Promedio = ', promedio)


    #Moda
def mode(dataset):
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items()
                      if value == most_frequent]

    return modes
print ('Moda = ', mode(data))


    #Mediana
medianaX = (n + 1) / 2
mediana = data[int(medianaX)]
print ('Mediana = ', mediana)


    #Cuartiles
    
indiceQ1 = n/4
indiceQ2 = medianaX
indiceQ3 = (3*n)/4


cuartil1 = data[int(indiceQ1)]
cuartil2 = data[int(indiceQ2)]
cuartil3 = data[int(indiceQ3)]

print ('Q1 = ', cuartil1, 'Q2 = ', cuartil2, 'Q2 = ', cuartil3)


#Dispersion

    #Varianza
varianza = datos.var()
print ('Varianza = ', varianza)

    #Desviacion estandar
desvestandar = varianza**0.5
print ('Desviacion Estandar = ', desvestandar)

    #Coeficiente de variacion
coevariacion = (desvestandar/promedio)*100
print ('Coeficiente de variacion = ', coevariacion, '%')

    #Rango muestral
rmuestral = data[n-1] - data[0]
print ('Rango muestral', rmuestral)

    #Rango Intercuartil
RIC = cuartil3 - cuartil1
print ('Rango intercuartil', RIC)





#def median(dataset):
 #   data = sorted(dataset)
  #  index = len(data) // 2
    
    # If the dataset is odd  
   # if len(dataset) % 2 != 0:
    #    return data[index]
    
    # If the dataset is even
   # return (data[index - 1] + data[index]) / 2


