class Validacion:
    def __init__(self, texto=''):
        self.__texto = texto

    # GETS: permite obtener el valor del atributo privado
    def _getTexto(self):
        return self.__texto

    # SETS: permiten establecer el valor del atributo privado, inicializarlo o cambiarlo
    def _setTexto(self, pTexto):
        self.__texto = pTexto

    # Función para imprimir una línea decorativa
    def estetico(self, pParametro):
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(pParametro)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    # Función para imprimir una línea decorativa después de un texto
    def semiEstetico(self, pParametro):
        print(pParametro)
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    # Función para pedir un número entero
    def _pedirNumeroEntero(self):
        while True:
            try:
                numero = int(input(f'Ingrese {self._getTexto()}: '))
            except ValueError:
                self.estetico('Debe ingresar números enteros. \nIntente nuevamente!')
            else:
                if numero >= 1:
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    return numero
                else:
                    self.estetico('Debe ingresar números enteros positivos. \nIntente nuevamente!')

    # Función para pedir una cadena de texto sin caracteres especiales
    def _pedirStringMayMas(self):
        while True:
            try:
                caracter = input(f'Ingrese {self._getTexto()}: ')
                if not caracter.strip() or any(c in ',<.>/?:;[{]}=+-_)(*&^%$#@!`~¨¡¿?-/`1~|' for c in caracter):
                    raise ValueError
            except ValueError:
                self.estetico('Debe ingresar caracteres válidos. \nIntente nuevamente!')
            else:
                return caracter.title()

    # Función para verificar que el número de teléfono tiene 8 dígitos
    def _verNumero(self, pNumero):
        while True:
            if len(str(pNumero)) == 8 and str(pNumero).isdigit():
                return pNumero
            else:
                print('No cumples con los requisitos. Ingrese un número de teléfono correspondiente.')
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                pNumero = self._pedirNumeroEntero()

    # Función para pedir una dirección de correo electrónico con "@" y ".com"
    def _pedirEmail(self):
        while True:
            try:
                email = input(f'Ingrese {self._getTexto()}: ')
                if '@' and '.com' not in email:
                    raise ValueError
            except ValueError:
                self.estetico('El email debe contener el símbolo @ y ser ".com".\nIntente nuevamente!')
            else:
                return email

    # Función para hacer que si es opción 1 sea Verdadero y 2 sea Falso
    def _opcion(self, pOpcion):
        while True:
            if pOpcion == 1:
                return True
            elif pOpcion == 2:
                return False
            else:
                self.estetico('No cumples con los requisitos.\nIntente nuevamente!')
                pOpcion = self._pedirNumeroEntero()
