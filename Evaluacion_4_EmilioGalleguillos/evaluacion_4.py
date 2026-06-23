from TuristasPais import Turistas_por_pais
from TuristasMes import Turistas_por_mes
from TuristaEliminar import Eliminar_turista
from Datos import turistas

def Main():
    while True:
        print("""
              MENU PRINCIPAL
        1.- Turistas por pais.
        2.- Turista por mes.
        3.- Eliminar turista.
        4.- Salir.
            """)
        input_usuario = input("Ingrese la opcion que desea realizar: ")
        match input_usuario:
            case "1":
                pais = input("Ingrese el pais que desea buscar: ")
                print(Turistas_por_pais(pais))
            case "2":
                mes = input("Ingrese el mes que desea buscar (1-12): ")
                if 0 < int(mes) < 13:
                    print(Turistas_por_mes(mes))
                else:
                    print("Mes no valido, intente nuevamente.")
                    continue
            case "3":
                print(Eliminar_turista())
            case "4":
                print("Programa Terminado...")
                break
            case _:
                print("Opcion no valida, intente nuevamente.")
                continue

Main()