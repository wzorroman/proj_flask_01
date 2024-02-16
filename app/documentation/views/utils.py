from datetime import datetime


# Configurar la fecha
def convertir_mes_a_espanol(mes: str):
    meses_en = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    meses_es = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", 
                "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    diccionario_meses = dict(zip(meses_en, meses_es))
    return diccionario_meses.get(mes, "")

def formatear_fecha_esp(fecha: datetime):
    # Formatear la fecha
    fecha_formateada = fecha.strftime("%-d %b %Y")

    # Convertir el mes a español
    mes_en = fecha.strftime("%b")
    mes_es = convertir_mes_a_espanol(mes_en)
    fecha_formateada = fecha_formateada.replace(mes_en, mes_es)
    return fecha_formateada