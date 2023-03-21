#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#● mostrar(): Muestra los datos de la cuenta.
#● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

from __persona__ import Persona
class Cuenta:
    #constructor
    def  __init__(self, titular = Persona(), cantidad = 0):
        self._titular = titular
        self._cantidad = cantidad

    # getters y setters para el atributo titular
    @property
    def titular(self):
        return self._titular.nombre

    @titular.setter
    def titular(self, titular):
        # validamos que el titular no sea un número
        if not isinstance(titular, str):
            print("El titular debe ser una cadena de caracteres")
        else:
            self._titular.nombre = titular

    # getters y setters para el atributo cantidad
    @property
    def cantidad(self):
        #cantidad puede ser un número entero o decimal
        return self._cantidad
    # ingresar dinero a la cuenta
    def ingresar(self, cantidad, nombre =  None):
        #validamos que la cantidad sea un número
        if not isinstance(cantidad, (int, float)):
            print("La cantidad a ingresar debe ser un número")
        else:
            if cantidad > 0:
                self._cantidad += cantidad
            else:
                print("La cantidad a ingresar debe ser mayor a cero")
        if nombre == None:
            pass
        else:
            if nombre != self.titular:
                print(f"El nombre del titular fue modificado de {self.titular} a {nombre}")
                self.titular = nombre

    # retirar dinero de la cuenta
    # retirar dinero de la cuenta
    def retirar(self, cantidad, nombre=None):
    # validamos que la cantidad sea un número
        if not isinstance(cantidad, (int, float)):
            print("La cantidad a retirar debe ser un número")
        else:
            if cantidad > 0:
                self._cantidad -= cantidad
            else:
                print("La cantidad a retirar debe ser mayor a cero")
        if nombre == None:
            pass
        else:
            if nombre != self.titular:
                print(f"El nombre del titular fue modificado de {self.titular} a {nombre}")
                self.titular = nombre

    # mostrar información de la cuenta
    def mostrar(self):
        return "Titular: {}\nCantidad: {}".format(self.titular, self.cantidad)


import unittest

class TestCuenta(unittest.TestCase):

    def setUp(self):
        self.persona = Persona("Juan", 25, 12345678)
        self.cuenta = Cuenta(self.persona, 0)

    def test_titular(self):
        self.assertEqual(self.cuenta.titular, "Juan")
        self.cuenta.titular = "Pedro"
        self.assertEqual(self.cuenta.titular, "Pedro")

    def test_ingresar(self):
        self.cuenta.ingresar(50)
        self.assertEqual(self.cuenta.cantidad, 50)
        self.cuenta.ingresar(-10)
        self.assertEqual(self.cuenta.cantidad, 50)
        self.cuenta.ingresar(20, "Pedro")
        self.assertEqual(self.cuenta.titular, "Pedro")

    def test_retirar(self):
        self.cuenta.ingresar(100)
        self.cuenta.retirar(50)
        self.assertEqual(self.cuenta.cantidad, 50)
        self.cuenta.retirar(-10)
        self.assertEqual(self.cuenta.cantidad, 50)
        self.cuenta.retirar(30, "Pedro")
        self.assertEqual(self.cuenta.titular, "Pedro")

    def test_mostrar(self):
        self.cuenta.ingresar(50)
        self.assertEqual(self.cuenta.mostrar(), "Titular: Juan\nCantidad: 50")
        self.cuenta.titular = "Pedro"
        self.assertEqual(self.cuenta.mostrar(), "Titular: Pedro\nCantidad: 50")

if __name__ == '__main__':
    unittest.main()

