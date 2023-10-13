class Persona:
    def __init__(self, nombre='', apellido=''):
        # Constructor de la clase Persona, inicializa los atributos nombre y apellido
        self.__nombre = nombre
        self.__apellido = apellido

    # Métodos Get
    def _getNombre(self):
        # Devuelve el valor del atributo privado nombre
        return self.__nombre

    def _getApellido(self):
        # Devuelve el valor del atributo privado apellido
        return self.__apellido

    # Métodos Set
    def _setNombre(self, nombre):
        # Establece el valor del atributo privado nombre
        self.__nombre = nombre

    def _setApellido(self, apellido):
        # Establece el valor del atributo privado apellido
        self.__apellido = apellido

    # Método de Polimorfismo
    def _mostrar(self):
        # Muestra el nombre y el apellido de la persona
        print('El nombre es:', self._getNombre())
        print('El apellido es:', self._getApellido())
