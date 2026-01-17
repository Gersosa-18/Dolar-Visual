import requests

from utils.helpers import formatear_fecha




def obtener_cotizaciones():
    response = requests.get("https://dolarapi.com/v1/dolares")
    cotizaciones = []
    
    if response.status_code == 200:
        datos = response.json()
        for item in datos:
            cotizacion = {
                "nombre": item["nombre"],
                "compra": item["compra"],
                "venta": item["venta"],
                "fecha_actualizacion": formatear_fecha(item["fechaActualizacion"])
            }
            cotizaciones.append(cotizacion)

    return cotizaciones