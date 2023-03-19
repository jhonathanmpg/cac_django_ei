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

    @cantidad.setter
    def cantidad(self, cantidad):
        # el atributo cantidad solo puede ser modificado a través de los métodos ingresar y retirar
        print("El atributo cantidad no puede ser modificado directamente.")
        pass

    # ingresar dinero a la cuenta
    def ingresar(self, cantidad):
        #validamos que la cantidad sea un número
        if not isinstance(cantidad, (int, float)):
            print("La cantidad a ingresar debe ser un número")
        else:
            if cantidad > 0:
                self._cantidad += cantidad

    # retirar dinero de la cuenta
    def retirar(self, cantidad):
        #validamos que la cantidad sea un número
        if not isinstance(cantidad, (int, float)):
            print("La cantidad a retirar debe ser un número")
        else:
            if cantidad > 0:
                self._cantidad -= cantidad


    # mostrar información de la cuenta
    def mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.cantidad)

#test de validadores
cuenta1 = Cuenta("Juan")
cuenta1.cantidad = "asdasd"#probamos el setter de cantidad
cuenta1.ingresar("asdasd")
cuenta1.retirar("asjkdhklasd")
cuenta1.mostrar()

#test de métodos
cuenta2 = Cuenta("Pedro")
cuenta2.cantidad = 0
cuenta2.ingresar(1000)
cuenta2.retirar(500)
cuenta2.mostrar()
