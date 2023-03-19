#6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#● mostrar(): Muestra los datos de la persona.
#● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    #constructor
    def __init__(self, nombre = "", edad = 0, dni = 0): #constructor donde los datos pueden estar vacíos
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
            print("El nombre debe ser una cadena de caracteres")
        else:
            self.__nombre = nombre
    @property
    def edad(self):
    #validamos que la edad sea un número entero
        return self.__edad
    @edad.setter
    def edad(self, edad):
        if not isinstance(edad, int):
            print("La edad debe ser un número entero")
        else:
            self.__edad = edad
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        if not isinstance(dni, int):
            print("El DNI debe ser un número entero")
        else:
            self.__dni = dni
    #mostrar
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.dni)
    #es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad == 0:
            return "No se ha ingresado la edad"
        elif self.edad >= 18:
            return f"{self.nombre} Es mayor de edad"
        else:
            return f"{self.nombre} No es mayor de edad"

persona = Persona()
persona.nombre = 123
persona.edad = "a"
persona.dni = "12345678"
persona.mostrar()
print(persona.es_mayor_de_edad())