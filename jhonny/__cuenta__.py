#7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#● mostrar(): Muestra los datos de la cuenta.
#● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

class Cuenta:
    # constructor
    def __init__(self, titular):
        self._titular = titular
        self._cantidad = 0.0

    # getters y setters para el atributo titular
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        # validamos que el titular no sea un número
        if not isinstance(titular, str):
            print("El titular debe ser una cadena de caracteres")
        else:
            self._titular = titular

    # getters y setters para el atributo cantidad
    @property
    def cantidad(self):
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
        self.cuenta = Cuenta("Juan")

    def test_titular(self):
        self.assertEqual(self.cuenta.titular, "Juan")

        # probamos cambiar el titular
        self.cuenta.titular = "Pedro"
        self.assertEqual(self.cuenta.titular, "Pedro")

        # probamos asignar un número como titular
        self.cuenta.titular = 123
        self.assertEqual(self.cuenta.titular, "Pedro")

    def test_ingresar(self):
        # probamos ingresar una cantidad válida
        self.cuenta.ingresar(100)
        self.assertEqual(self.cuenta.cantidad, 100)

        # probamos ingresar una cantidad inválida (no numérica)
        self.cuenta.ingresar("cien")
        self.assertEqual(self.cuenta.cantidad, 100)

        # probamos ingresar una cantidad inválida (menor o igual a cero)
        self.cuenta.ingresar(-50)
        self.assertEqual(self.cuenta.cantidad, 100)

        # probamos ingresar una cantidad válida con un nombre de titular diferente
        self.cuenta.ingresar(50, "Juan")
        self.assertEqual(self.cuenta.cantidad, 150)
        print (self.cuenta.cantidad, self.cuenta.titular)

    def test_retirar(self):
        # probamos retirar una cantidad válida
        self.cuenta.retirar(50)
        self.assertEqual(self.cuenta.cantidad, -50)

        # probamos retirar una cantidad inválida (no numérica)
        self.cuenta.retirar("cincuenta")
        self.assertEqual(self.cuenta.cantidad, -50)

        # probamos retirar una cantidad inválida (menor o igual a cero)
        self.cuenta.retirar(-10)
        self.assertEqual(self.cuenta.cantidad, -50)

        # probamos retirar una cantidad mayor a la disponible en la cuenta
        self.cuenta.retirar(100)
        self.assertEqual(self.cuenta.cantidad, -150)

    def test_mostrar(self):
        # probamos el método mostrar()
        self.assertEqual(self.cuenta.mostrar(), "Titular: Juan\nCantidad: 0.0")

if __name__ == '__main__':
    unittest.main()

