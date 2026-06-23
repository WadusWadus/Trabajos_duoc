from Datos import turistas

def Turistas_por_pais(pais):
    turistas_encontrados = []
    for turista in turistas.values():
        if turista[1].lower() == pais.lower():
            turistas_encontrados.append(turista[0])
    if turistas_encontrados == []:
        turistas_encontrados = "No hay turistas de ese pais"
    return turistas_encontrados


