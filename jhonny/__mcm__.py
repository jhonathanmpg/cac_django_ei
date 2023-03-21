#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
#sabemos que el minimo comun multiplo son los numeros que son multiplos de ambos, se repitan o no
#también se puede definir como el número más pequeño que es múltiplo de ambos números.
#solución con función iterativa
from __mcd__ import mcd_recursiva
def mcm_itera(a,b):
    #inicializamos la variable mcm = 1, ya que uno divide a cualquier numero
    mcm = 1
    #primero comprobamos que a y b sean numeros enteros
    if (a % 1 == 0) and (b % 1 == 0): #con esta condición lo que validamos es que el resto de a y b sea 0, es decir, que sean numeros enteros
        #si a es mayor que b, entonces a es el mayor
        if a > b:
            mayor = a
        #si b es mayor que a, entonces b es el mayor
        else:
            mayor = b
        #recorremos desde 1 hasta el mayor de los dos numeros
        for i in range(1, mayor+1):
            #si el resto de a y b es 0, entonces i es el mcm
            if (i % a == 0) and (i % b == 0):
                mcm = i
                break
    #si no son numeros enteros, entonces no se puede calcular el mcm
    else:
        print("No se puede calcular el mcm")
    return mcm
print(mcm_itera(3,6))

#solución con lambda function recursiva
mcm_recursiva = lambda a,b: int(a*b/mcd_recursiva(a,b)) if a != b else a
#aquí lo que hacemos primero es calcular el mcd de a y b
# luego multiplicamos a y b por el mcd y dividimos entre el mcd
# esto nos da el mcm
# si a y b son primos entre si, entonces el mcm es a*b
# si a y b no son primos entre si, entonces el mcm es a*b/mcd
# si a y b son iguales, entonces el mcm es a
# si a y b son 1, entonces el mcm es 1
# si a y b son 0, entonces el mcm es 0
print(mcm_recursiva(3,6))    