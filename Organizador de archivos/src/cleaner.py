# src/cleaner.py
# Este archivo contiene la logica para eliminar archivos viejos según la fecha de modificación

import os, datetime, logging
from .config import CARPETA_ORIGEN, DIAS_MAXIMOS

def eliminar_antiguos():
    ahora = datetime.datetime.now()
    for archivo in os.listdir(CARPETA_ORIGEN):
        ruta = os.path.join(CARPETA_ORIGEN, archivo)
        if os.path.isfile(ruta):
            modificado = datetime.datetime.fromtimestamp(os.path.getmtime(ruta))
            if (ahora - modificado).days > DIAS_MAXIMOS:
                try:
                    os.remove(ruta)
                    logging.warning(f"Eliminado por antigüedad: {archivo}")
                    print(f"🗑️ Eliminado: {archivo}")
                except Exception as e:
                    logging.error(f"Error al eliminar {archivo}: {e}")
                    print(f"❌ Error al eliminar {archivo}")
