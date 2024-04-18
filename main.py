mi_agenda = Agenda()

# Función para agregar un evento
def agregar_evento():
   
    print("Agregar evento")


def eliminar_evento():
    
    print("Eliminar evento")

def mostrar_eventos():

    eventos = mi_agenda.mostrar_eventos()
    for evento in eventos:
        print(evento)

# Función para mostrar el menú y ejecutar la opción seleccionada
def mostrar_menu():
    while True:
        print("Menú de la Agenda:")
        print("1. Agregar evento")
        print("2. Eliminar evento")
        print("3. Mostrar eventos")
        print("4. Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            agregar_evento()
        elif opcion == '2':
            eliminar_evento()
        elif opcion == '3':
            mostrar_eventos()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

