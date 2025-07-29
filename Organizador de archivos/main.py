# main.py
# Punto de entrada. Lo que hace es llamar a las funciones de los módulos

import os
import logging
from src import organizer, cleaner, mailer
from src.config import CARPETA_LOGS

# Crear carpeta de logs si no existe
os.makedirs(CARPETA_LOGS, exist_ok=True)

# Configurar logging
log_path = os.path.join(CARPETA_LOGS, "actividad.log")
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ejecutar pasos
organizer.organizar_archivos()
cleaner.eliminar_antiguos()
mailer.enviar_log()
