from Datos import turistas

def Turistas_por_mes(mes):
    try:
        mes = int(mes)
        if mes < 1 or mes > 12:
            raise ValueError
        total_turistas = len(turistas)
        visitas = 0
        for turista in turistas.values():
            fecha = turista[2]
            mes_turista = int(fecha.split("-")[1])
            if mes_turista == mes:
                visitas += 1
        porcentage_visitas = (visitas / total_turistas) * 100
        if porcentage_visitas == 0:
            return f"No hubo turistas que visitaron en el mes {mes}"
        return f"El porcentaje de turistas que visitaron en el mes {mes} es: {porcentage_visitas:.1f}%"

    except ValueError:
        return "El mes debe ser un número entre 1 y 12"