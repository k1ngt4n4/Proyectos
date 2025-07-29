# src/config.py
# Este archivo contiene rutas, extensiones y parámetros de usuario

import os

# Rutas principales
CARPETA_ORIGEN = r"C:\Users\Franco Quintana\Downloads"
CARPETA_DESTINO = "./output"
CARPETA_LOGS = "./logs"

# Comportamiento
EXTENSIONES = ['PDF', 'PNG', 'JPG', 'TXT', 'DOC', 'XLSX', 'ZIP', 'JSON', 'CSV','EXE','WEBP', 'AVIF', 'PY', 'YAML', 'XLS']
RENOMBRAR = True
DIAS_MAXIMOS = 60

# Email
EMAIL_ORIGEN = "franco.quintana@saudasrl.com.ar"
EMAIL_DESTINO = "quintanafranco100@gmail.com"


CLAVE_APP = "pnoq ozzz hzzk izag"

actual = os.getcwd()
print(actual)


