
#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.
#solución con función iterativa
from __freq_v1__ import frecuencia_itera

def tupla_itera(diccionario):
    #inicializamos la variable maximo
    maximo = 0
    #recorremos el diccionario
    for i in diccionario:
        #si el valor de la clave es mayor que maximo, entonces maximo es el valor de la clave
        if diccionario[i] > maximo:
            maximo = diccionario[i]
            #la clave con el valor maximo es la palabra mas repetida
            palabra = i
    #retornamos la palabra mas repetida y su frecuencia
    return palabra, maximo
print(tupla_itera(frecuencia_itera("Hola mundo Hola mundo Hola mundo Hola mundo hola mundo hola hola")))

#solución con lambda function recursiva
tupla_recursiva = lambda diccionario: (max(diccionario, key=diccionario.get), diccionario[max(diccionario, key=diccionario.get)])
