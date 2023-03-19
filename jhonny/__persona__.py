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
persona.set_nombre("Jhonathan")
persona.set_edad(31)
persona.set_dni(12345678)
persona.mostrar()
print(persona.es_mayor_de_edad())