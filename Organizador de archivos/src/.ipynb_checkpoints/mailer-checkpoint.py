# src/mailer.py
# Función para enviar el archivo de log por correo eléctronicoS

import smtplib, os, logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from .config import EMAIL_ORIGEN, EMAIL_DESTINO, CLAVE_APP, CARPETA_LOGS

def enviar_log():
    ruta_log = os.path.join(CARPETA_LOGS, "actividad.log")
    mensaje = MIMEMultipart()
    mensaje['From'] = EMAIL_ORIGEN
    mensaje['To'] = EMAIL_DESTINO
    mensaje['Subject'] = "Log de automatización de archivos"
    mensaje.attach(MIMEText("Adjunto el log de automatización.", 'plain'))

    with open(ruta_log, "rb") as adjunto:
        part = MIMEApplication(adjunto.read(), Name="actividad.log")
        part['Content-Disposition'] = 'attachment; filename="actividad.log"'
        mensaje.attach(part)

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL_ORIGEN, CLAVE_APP)
        servidor.send_message(mensaje)
        servidor.quit()
        logging.info("Log enviado por correo.")
        print("📤 Log enviado.")
    except Exception as e:
        logging.error(f"Error al enviar log por email: {e}")
        print(f"❌ Error al enviar log por correo: {e}")
