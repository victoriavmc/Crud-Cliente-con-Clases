from claseCrud import Crud  # Importa la clase Crud
from claseCliente import Cliente  # Importa la clase Cliente
from claseValidacion import Validacion  # Importa la clase Validacion

crud = Crud()  # Crea una instancia de la clase Crud

print(' \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
    print('1. Crear cliente')
    print('2. Leer cliente(s)')
    print('3. Actualizar cliente')
    print('4. Eliminar cliente')
    print('5. Salir')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n')

    texto1 = Validacion('una opción')
    op = texto1._pedirNumeroEntero()

    if op == 1:
        crud._crearCliente()  # Llama a la función para crear un nuevo cliente
    elif op == 2:
        crud._leer()  # Llama a la función para leer datos de clientes
    elif op == 3:
        crud._actualizar()  # Llama a la función para actualizar datos de un cliente
    elif op == 4:
        crud._eliminar()  # Llama a la función para eliminar un cliente
    elif op == 5:
        texto1.semiEstetico('''Profesor: 
            Lic. Plazas, Ricardo Gastón      
    Estudiante:
            Maidana Corti, Victoria Valentina ''')
        break  # Sale del bucle
    else:
        texto1.semiEstetico('Opción no válida. Intente de nuevo.')
