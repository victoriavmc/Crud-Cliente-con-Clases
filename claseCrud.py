from claseCliente import Cliente  # Importa la clase Cliente
from claseValidacion import Validacion  # Importa la clase Validacion
import random

validacionInstancia = Validacion()  # Crea una instancia de la clase Validacion

class Crud:
    def __init__(self, numero1=1, numero2=100):
        # Constructor de la clase Crud, inicializa los números 1 y 100
        self.__numero1 = numero1
        self.__numero2 = numero2

    # Métodos Get
    def _getNumero1(self):
        return self.__numero1

    def _getNumero2(self):
        return self.__numero2

    # Métodos Set
    def _setNumero1(self, numero1):
        self.__numero1 = numero1

    def _setNumero2(self, numero2):
        self.__numero2 = numero2

    # Función para pedir datos de un cliente
    def pedirDatos(self):
        texto1 = Validacion('nombre del cliente')
        nombre = texto1._pedirStringMayMas()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        texto1._setTexto('apellido del cliente')
        apellido = texto1._pedirStringMayMas()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        texto1._setTexto('domicilio del cliente')
        domicilio = texto1._pedirStringMayMas()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        texto1._setTexto('telefono del cliente')
        telefono = texto1._pedirNumeroEntero()
        telefono = texto1._verNumero(telefono)

        texto1._setTexto('email del cliente')
        email = texto1._pedirEmail()

        return nombre, apellido, domicilio, telefono, email

    # Función para crear un nuevo cliente
    def _crearCliente(self):
        nombre, apellido, domicilio, telefono, email = self.pedirDatos()
        ticket = random.randint(self._getNumero1(), self._getNumero2())

        # Asegurarse de que el número no se repita
        while ticket in Cliente.listaClientes:
            ticket = random.randint(self._getNumero1(), self._getNumero2)

        # Creando la instancia de cliente
        clienteNuevo = Cliente(nombre, apellido, domicilio, telefono, email, ticket)
        validacionInstancia.estetico('Cliente creado con éxito.')

    # Función para buscar un cliente por número de ticket
    def _buscarCliente(self, pTicket):
        for cliente in Cliente.listaClientes:
            if cliente._getTicket() == pTicket:
                return cliente
        return None

    # Función para pedir el número de ticket y buscar un cliente
    def pedirTicket(self):
        texto1 = Validacion('el número de ticket del cliente')
        ticket = texto1._pedirNumeroEntero()
        return self._buscarCliente(ticket)

    # Función para leer datos de clientes
    def _leer(self):
        print('Desea 1. Buscar cliente en específico. 2. Listar todo.')
        texto1 = Validacion('una opción')
        op = texto1._pedirNumeroEntero()
        op = texto1._opcion(op)
        if op:
            cliente = self.pedirTicket()
            if cliente:
                cliente._mostrar()
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
            else:
                validacionInstancia.semiEstetico('Cliente no encontrado.')
        else:
            if len(Cliente.listaClientes) == 0:
                validacionInstancia.semiEstetico('No hay clientes.')
            else:
                print('Clientes:\n')
                for cliente in Cliente.listaClientes:
                    cliente._mostrar()
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

    # Función para eliminar un cliente
    def _eliminar(self):
        validacionInstancia = Validacion()
        print('Según el ticket, elimine un cliente')
        cliente = self.pedirTicket()
        if cliente:
            Cliente.listaClientes.remove(cliente)
            validacionInstancia.semiEstetico('Cliente eliminado con éxito.')
        else:
            validacionInstancia.semiEstetico('Cliente no encontrado.')

    # Función para actualizar los datos de un cliente
    def _actualizar(self):
        print('Según el ticket, modifique un cliente')
        cliente = self.pedirTicket()
        if cliente:
            print('Ingrese los nuevos datos del cliente')
            nombre, apellido, domicilio, telefono, email = self.pedirDatos()

            #Actualiza los datos
            cliente._setNombre(nombre)
            cliente._setApellido(apellido)
            cliente._setDomicilio(domicilio)
            cliente._setTelefono(telefono)
            cliente._setEmail(email)

            validacionInstancia.estetico('Cliente actualizado con éxito.')
        else:
            validacionInstancia.semiEstetico('Cliente no encontrado.')
