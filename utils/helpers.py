from datetime import datetime

def formatear_fecha(fecha_str):
    try:
        fecha_obj = datetime.fromisoformat(fecha_str.replace('Z', '+00:00'))
        return fecha_obj.strftime("%d/%m/%Y %H:%M")
    except Exception:
        return "Fecha inválida"