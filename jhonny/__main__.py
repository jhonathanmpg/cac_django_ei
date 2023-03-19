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

#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
#sabemos que el minimo comun multiplo son los numeros que son multiplos de ambos, se repitan o no
#también se puede definir como el número más pequeño que es múltiplo de ambos números.
#solución con función iterativa
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

#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.
#solución con función iterativa
def frecuencia_v3(cadena):
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
print(frecuencia_v3("Hola mundo"))

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
print(tupla_itera(frecuencia_v3("Hola mundo")))

#solución con lambda function recursiva
frecuencia_v4 = lambda cadena: {i:cadena.count(i) for i in cadena if i != " "}
tupla_recursiva = lambda diccionario: (max(diccionario, key=diccionario.get), diccionario[max(diccionario, key=diccionario.get)])

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
            print("Ingrese nuevamente")
    return numero
print(get_int_itera())

#solución con lambda function recursiva
get_int_recursiva = lambda numero = 0: int(input("Ingrese un numero entero: ")) if numero == 0 else numero
print(get_int_recursiva())


#6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#● mostrar(): Muestra los datos de la persona.
#● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    #constructor
    def __init__(self, nombre = "", edad = 0, dni = 0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    #setters y getters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre
    def set_edad(self, edad):
        self.edad = edad
    def get_edad(self):
        return self.edad
    def set_dni(self, dni):
        self.dni = dni
    def get_dni(self):
        return self.dni
    #mostrar
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.dni)
    #es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

persona = Persona()
persona.set_nombre("Juan")
persona.set_edad(20)
persona.set_dni(12345678)
persona.mostrar()
print(persona.es_mayor_de_edad())


#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#● mostrar(): Muestra los datos de la cuenta.
#● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

class Cuenta:
    #constructor
    def __init__(self, titular):
        self.titular = titular
        self.cantidad = 0
    #setters y getters
    def set_titular(self, titular):
        self.titular = titular
    def get_titular(self):
        return self.titular
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def get_cantidad(self):
        return self.cantidad
    #mostrar
    def mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.cantidad)
    #ingresar
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    #retirar
    def retirar(self, cantidad):
        self.cantidad -= cantidad

cuenta = Cuenta("Juan")
cuenta.ingresar(100)
cuenta.retirar(50)
cuenta.mostrar()
     
