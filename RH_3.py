# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1


"""

import math

import numpy as np
import matplotlib.pyplot as plt

#input_dir='C:/Users/PATH/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename='energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) para números solamente. Otro tipo de variable (texto por ejemplo) se leerá como nan
#datos=np.genfromtxt(filename,delimiter=';',skip_header=1)
muestra = np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = range(8,9), dtype=float) #obtener los datos de columna especifica
#datos=np.loadtxt(filename,delimiter=',',skiprows=1)


#Ordenar y tamaño de los datos
datos = sorted(muestra)
n = np.size(muestra)



"Datos de tendencia"

    #Promedio con un ciclo que hace la suma total a partir de indices para luego devidir la suma total entre datos totales.... 
promedio = 0
cont = 0
while cont < n:
    promedio = muestra[cont] + promedio
    cont += 1
promedio = promedio/n
print ('Promedio = ', promedio)


    #Moda, se realiza una lectura por indices para "ordenar" la repeticion de X dato y retornar el o los valores mas repetidos
    #con apoyo de https://geekflare.com/es/python-find-mean-median-and-mode/#:~:text=Usando%20mean%20%28%29%20del%20m%C3%B3dulo%20de%20estad%C3%ADsticas%20de,calcularlos%2C%20junto%20con%20otros%20temas%20b%C3%A1sicos%20de%20estad%C3%ADstica.
def mode(entrada):
    frecuencia = {}
    for dato in entrada:
        frecuencia[dato] = frecuencia.get(dato, 0) + 1
    frecuente = max(frecuencia.values())
    valor = [key for key, dato in frecuencia.items()
                      if dato == frecuente]
    return valor
print ('Moda = ', mode(datos))


    #Mediana aca entraria if si varian los datos totales, para este trabajo especifico es una cantidad total impar por lo que
    #se busca el indice central de los datos ordenados y se extrae el valor
medianaX = (n + 1) / 2
mediana = datos[int(medianaX)]
print ('Mediana = ', mediana)


    #Cuartiles, si la cantidad total de datos no es divisible entre cuatro se redondea el indice del cuartil X al mayor mas cercano
    #en este caso se transforma a interger
indiceQ1 = n/4
indiceQ3 = (3*n)/4

cuartil1 = datos[int(indiceQ1)]
cuartil2 = datos[int(medianaX)]
cuartil3 = datos[int(indiceQ3)]
print ('Q1 = ', cuartil1, 'Q2 = ', cuartil2, 'Q2 = ', cuartil3)


"Medidas de variabilidad o dispersion"

    #Varianza, para mayor eficiencia seria usar numpy.var(), pero en este caso usamos una funcion para realizar las operaciones
    #necesarias para el calculo de la varianza, teniendo en cuenta que los datos se trabajan al cuadrado      
def varianza(data):
    cont1 = 0
    suma = 0
    for valor in data:
        suma = suma + (data[cont1] - promedio)**2
        cont1 += 1
    varianza = suma/(n-1)
    return varianza
print ('Var = ', varianza(datos))


    #Desviacion estandar, obtenemos la raiz cuadrada de la varianza que obtenmos con la funcion varianza(datos)
desvestandar = varianza(datos)**0.5
print ('Desviacion Estandar = ', desvestandar)


    #Coeficiente de variacion, deviacion estandar en porcentaje
coevariacion = (desvestandar/promedio)*100
print ('Coeficiente de variacion = ', round(coevariacion, 2), '%')


    #Rango muestral, mayor dato menos el menor dato de la muestra ordenada
rmuestral = datos[n-1] - datos[0]
print ('Rango muestral', rmuestral)


    #Rango Intercuartil, cuartil 3 menos cuartil 1
RIC = cuartil3 - cuartil1
print ('Rango intercuartil', RIC)



"Codigo para presentacion de los datos de forma adecuada"


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





