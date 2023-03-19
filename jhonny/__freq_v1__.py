#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
#solución con función iterativa
def frecuencia_itera(cadena):
    #primero convertimos la cadena a minusculas
    cadena = cadena.lower()
    #inicializamos el diccionario
    diccionario = {}
    #recorremos la cadena
    for i in cadena:
        #si el caracter no es un espacio, entonces lo agregamos al diccionario
        if i != " ":
            diccionario[i] = cadena.count(i)
    return diccionario
print(frecuencia_itera("Hola mundo"))

#solución con lambda function recursiva
frecuencia_recursiva = lambda cadena: {i:cadena.count(i) for i in cadena if i != " "}
#en esta solución lo que hacemos es primero evaluar si el caracter es un espacio
#si no es un espacio, entonces lo agregamos al diccionario
print(frecuencia_recursiva("Hola mundo"))