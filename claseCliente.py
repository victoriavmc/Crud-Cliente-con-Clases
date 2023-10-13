from clasePersona import Persona  # Importa la clase Persona desde un módulo llamado clasePersona

class Cliente(Persona):  # Define una nueva clase Cliente que hereda de la clase Persona
    listaClientes = []  # Atributo de clase que almacenará instancias de Cliente

    def __init__(self, nombre, apellido, domicilio='', telefono=0, email='', ticket=0):
        # Constructor de la clase Cliente
        super().__init__(nombre, apellido)  # Llama al constructor de la clase base Persona
        # Inicializa atributos específicos de Cliente
        self.__domicilio = domicilio
        self.__telefono = telefono
        self.__email = email
        self.__ticket = ticket
        # Agrega la instancia de Cliente a la lista de clientes
        Cliente.listaClientes.append(self)

    # Métodos Get
    def _getDomicilio(self):
        return self.__domicilio  # Devuelve el domicilio del cliente

    def _getTelefono(self):
        return self.__telefono  # Devuelve el número de teléfono del cliente

    def _getEmail(self):
        return self.__email  # Devuelve el correo electrónico del cliente

    def _getTicket(self):
        return self.__ticket  # Devuelve el número de ticket del cliente

    # Métodos Set
    def _setDomicilio(self, domicilio):
        self.__domicilio = domicilio  # Establece el domicilio del cliente

    def _setTelefono(self, telefono):
        self.__telefono = telefono  # Establece el número de teléfono del cliente

    def _setEmail(self, email):
        self.__email = email  # Establece el correo electrónico del cliente

    def _setTicket(self, ticket):
        self.__ticket = ticket  # Establece el número de ticket del cliente

    # Método de Polimorfismo
    def _mostrar(self):
        # Muestra información sobre el cliente
        print('Ticket:', self._getTicket())
        super()._mostrar()  # Llama al método mostrar de la clase Persona (clase base)
        print('El domicilio:', self._getDomicilio())
        print('El telefono:', self._getTelefono())
        print('El email:', self._getEmail())
