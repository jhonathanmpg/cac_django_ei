
#5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
#cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
#del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
#ejercicio tanto de manera iterativa como recursiva
#solución con función iterativa
def get_int_itera():
    #inicializamos la variable numero
    numero = 0
    #inicializamos la variable bandera
    bandera = True
    #recorremos el bucle
    while bandera:
        #leemos el numero
        numero = input("Ingrese un numero entero: ")
        #si el numero es entero, entonces lo retornamos
        try:
            numero = int(numero)
            bandera = False
        #si el numero no es entero, entonces le pedimos que ingrese un numero entero
        except ValueError:
            print("No es un numero entero")
    return numero
print(get_int_itera())

#solución con lambda function recursiva
get_int_recursiva = lambda numero = 0: int(input("Ingrese un numero entero: ")) if numero == 0 else numero
print(get_int_recursiva())