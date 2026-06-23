from Datos import turistas

def Eliminar_turista():
    turista_borrar = input("Ingrese el Nombre y apellido del turista que desea eliminar: ")
    for identificador , datos_turista in turistas.items():
        if datos_turista[0].lower() == turista_borrar.lower():
            del turistas[identificador]
            return f"El turista {turista_borrar} ha sido eliminado."
    return f"No se encontró el turista {turista_borrar} en la lista."

