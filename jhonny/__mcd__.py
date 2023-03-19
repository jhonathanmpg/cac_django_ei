#1. Escribir una función que calcule el máximo común divisor entre dos números.
#sabemos que el minimo comun multiplo son los numeros que son multiplos de ambos, se repitan o no
#también se puede definir como el número más grande que divide a ambos números sin dejar resto.
#solucion con funcion iterativa
def mcd_itera(a,b):
    #inicializamos la variable mcd = 1, ya que uno divide a cualquier numero
    mcd = 1
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
            #si el resto de a y b es 0, entonces i es el mcd
            if (a % i == 0) and (b % i == 0):
                mcd = i
    #si no son numeros enteros, entonces no se puede calcular el mcd
    else:
        print("No se puede calcular el mcd")
    return mcd
print(mcd_itera(3,6))

#solución con lambda function recursiva
mcd_recursiva = lambda a,b: a if b == 0 else mcd_recursiva(b, a%b)
#aquí lo que hacemos primero es comprobar si b es 0, si es 0, entonces a es el mcd
#si b no es 0, entonces llamamos a la función recursivamente, pasando como primer argumento b y como segundo el resto de a y b
print(mcd_recursiva(3, 6))