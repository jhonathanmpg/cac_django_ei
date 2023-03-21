#6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#● mostrar(): Muestra los datos de la persona.
#● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    #constructor
    def __init__(self, nombre=None, edad=None, dni=None): #constructor donde los datos pueden estar vacíos
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    #setters y getters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter

    def nombre(self, nombre):
        #validamos que el nombre no sea un número
        if not isinstance(nombre, str):
            self.__nombre = None
        else:
            self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        #validamos que la edad sea un número entero
        if not isinstance(edad, int):
            self.__edad = None
        else:
            self.__edad = int(edad)

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        #validamos que el dni sea un número entero
        if not isinstance(dni, int):
            self.__dni = None
        else:
            self.__dni = dni

    #mostrar
    def mostrar(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}"

    #es mayor de edad
    def es_mayor_de_edad(self):
        #validar que se haya ingresado la edad
        if self.edad == None:
            return "No se ha ingresado la edad"
        #validar si es mayor de edad
        if self.edad >= 18:
            return True
        else:
            return False

import unittest

class TestPersona(unittest.TestCase):
    def test_nombre(self):
        persona = Persona()
        persona.nombre = 123
        self.assertEqual(persona.nombre, None)
        persona.nombre = "Juan"
        self.assertEqual(persona.nombre, "Juan")

    def test_edad(self):
        persona = Persona()
        persona.edad = "veinte"
        self.assertEqual(persona.edad, None)
        persona.edad = 20
        self.assertEqual(persona.edad, 20)

    def test_dni(self):
        persona = Persona()
        persona.dni = "1234"
        self.assertEqual(persona.dni, None)
        persona.dni = 12345678
        self.assertEqual(persona.dni, 12345678)

    def test_mostrar(self):
        persona = Persona("Juan", 20, 12345678)
        self.assertEqual(persona.mostrar(), "Nombre: Juan\nEdad: 20\nDNI: 12345678")

    def test_es_mayor_de_edad(self):
        persona = Persona(nombre="Juan", dni=12345678)
        self.assertEqual(persona.es_mayor_de_edad(), "No se ha ingresado la edad")
        persona.edad = 17
        self.assertEqual(persona.es_mayor_de_edad(), False)
        persona.edad = 18
        self.assertEqual(persona.es_mayor_de_edad(), True)


if __name__ == '__main__':
    unittest.main()