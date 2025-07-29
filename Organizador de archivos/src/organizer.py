# src/organizer.py
# Este archivo contiene la lógica para mover y renombrar archivos por el tipo de cada uno

import os, shutil, datetime, logging
from .config import CARPETA_ORIGEN, CARPETA_DESTINO, EXTENSIONES, RENOMBRAR

def organizar_archivos():
    for ext in EXTENSIONES:
        os.makedirs(os.path.join(CARPETA_DESTINO, ext), exist_ok=True)

    for root, _, files in os.walk(CARPETA_ORIGEN):
        for file in files:
            ruta = os.path.join(root, file)
            if CARPETA_DESTINO in ruta or '.' not in file:
                continue

            ext = file.split('.')[-1].upper()
            if ext in EXTENSIONES:
                nombre = f"{os.path.splitext(file)[0]}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.{ext.lower()}" if RENOMBRAR else file
                destino = os.path.join(CARPETA_DESTINO, ext, nombre)
                try:
                    shutil.move(ruta, destino)
                    logging.info(f"Movido: {file} → {destino}")
                    print(f"✔ Movido: {file}")
                except Exception as e:
                    logging.error(f"Error al mover {file}: {e}")
                    print(f"❌ Error al mover {file}: {e}")
