#8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
#● Un constructor.
#● Los setters y getters para el nuevo atributo.
#● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
#● Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta

from __cuenta__ import Cuenta
from __persona__ import Persona
class CuentaJoven(Cuenta):
    #constructor
    def __init__(self, titular, cantidad = 0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
    # getters y setters para el atributo bonificacion
    @property
    def bonificacion(self):
        #validamos que la bonificación sea un número
        if type(self._bonificacion) != int:
            print("La bonificación debe ser un número")
        else:
            return self._bonificacion
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        if not isinstance(bonificacion, (int, float)):
            print("La bonificación debe ser un número")
        else:
            self._bonificacion = bonificacion
    # método para validar el titular
    def es_titular_valido(self):
        if self.titular.edad > 18 and self.titular.edad < 25:
            return True
        else:
            return False

    # método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido")
    # método para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Cuenta Joven de {self.titular} con bonificación de {self.bonificacion}%")


#creamos una Persona
persona1 = Persona(str("Jhonny"), 22, 9123456)
#creamos una Cuenta
cuenta1 = Cuenta(persona1, 1000)
#creamos una Cuenta Joven
cuenta_joven1 = CuentaJoven(persona1, 1000, 10)
#mostramos los datos de la cuenta
cuenta_joven1.mostrar() 
print(persona1.mostrar())
cuenta_joven1.es_titular_valido()

