class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre, self.titular.apellido)
        print("Cantidad:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad


persona = Persona("Omar", "Galvan")
cuenta = Cuenta(persona, 100000.0)
cuenta.mostrar()
cuenta.ingresar(500.0)
cuenta.mostrar()
cuenta.retirar(5000.0)
cuenta.mostrar()
