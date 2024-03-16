import csv

# Archivo CSV para guardar y cargar datos
ARCHIVO_CSV = "datos_equipo.csv"
  
# Cargar datos del archivo CSV 
def cargar_datos():
    jugadores = []
    try:
        with open(ARCHIVO_CSV, "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                jugadores.append(dict(fila))
    except FileNotFoundError:
        pass
    return jugadores

# Guardar datos en el archivo CSV
def guardar_datos(jugadores):
    with open(ARCHIVO_CSV, "w", newline="") as archivo:
        campos = ["Pos", "Jugador", "Apariciones", "Goles", "Asistencias", "PoImbatida", "TarjetasRojas", "Mvp"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for jugador in jugadores:
            escritor.writerow(jugador)
      
# Al iniciar el programa, cargar datos del archivo CSV
equipo = cargar_datos()

# Importar la biblioteca tabulate - pip install tabulate (para instalar el modulo)
from tabulate import tabulate  

# Función para añadir un jugador al equipo
def agregar_jugador():
    while True:
        print("==============================================")
        print("Agregar un nuevo jugador al equipo")
        print("==============================================")
        print("1. Agregar jugador")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Pos = input("Posición del jugador: ")
            jugador = input("Nombre del jugador: ")
            apariciones = int(input("Apariciones: "))
            goles = int(input("Goles: "))
            asistencias = int(input("Asistencias: "))
            po_imbatida = int(input("Po Imbatida: "))
            tarjetas_rojas = int(input("Tarjetas Rojas: "))
            mvp = int(input("MVP: "))

            jugador_stats = {
                "Pos": Pos,
                "Jugador": jugador,
                "Apariciones": apariciones,
                "Goles": goles,
                "Asistencias": asistencias,
                "PoImbatida": po_imbatida,
                "TarjetasRojas": tarjetas_rojas,
                "Mvp": mvp
            }

            equipo.append(jugador_stats)
            print(f"El jugador {jugador} ha sido añadido al equipo con éxito.")
        elif opcion == "3":
            opcion = menu_principal()
        elif opcion == "2":
            opcion = menu_principal()
            guardar_datos(equipo)
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def menu_principal():
    print("==============================================")
    print("Sistema de estadísticas de equipo de fútbol")
    print("==============================================")
    print("1. Agregar jugador")
    print("2. Mostrar estadísticas de jugador")
    print("3. Mostrar estadísticas de todos los jugadores")
    print("4. Actualizar estadísticas de un jugador")
    print("5. Eliminar un jugador")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion

while True:
    opcion = menu_principal()

    if opcion == "1":
        agregar_jugador()
    elif opcion == "2":
        jugador = input("Ingrese el nombre del jugador: ")
        mostrar_estadisticas(jugador)
    elif opcion == "3":
        mostrar_estadisticas_todos()
    elif opcion == "4":
        jugador = input("Ingrese el nombre del jugador que quiere actualizar: ")
        actualizar_estadisticas(jugador)
        guardar_datos(equipo)
    elif opcion == "5":
        jugador = input("Ingrese el nombre del jugador que desea eliminar: ")
        eliminar_jugador(jugador, equipo)
        guardar_datos(equipo)
    elif opcion == "6":
        print("¡Gracias por usar el sistema de estadísticas!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

    print("¡Gracias por usar el sistema de estadísticas!")
    break