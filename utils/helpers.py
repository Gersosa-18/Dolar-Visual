import arrow

def formatear_fecha(fecha_str):
    try:
        fecha_obj = arrow.get(fecha_str)
        return fecha_obj.format("DD/MM/YYYY HH:mm")
    except Exception:return "Fecha inválida"