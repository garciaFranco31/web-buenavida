import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Verificar si existen las variables de entorno necesarias
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

print("Variables de entorno:")
print(f"SMTP_SERVER: {'✓ existe' if smtp_server else '✗ falta'}")
print(f"SMTP_PORT: {'✓ existe' if smtp_port else '✗ falta'}")
print(f"SENDER_EMAIL: {'✓ existe' if sender_email else '✗ falta'}")
print(f"SENDER_PASSWORD: {'✓ existe' if sender_password else '✗ falta'}")
print(f"RECEIVER_EMAIL: {'✓ existe' if receiver_email else '✗ falta'}")

# Probar la creación de un mensaje de email
def create_contact_email(name: str, email: str, message: str, receiver: str) -> MIMEMultipart:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Nuevo mensaje de contacto de {name}"
    msg["From"] = email
    msg["To"] = receiver
    
    # Crear el cuerpo del email en texto plano
    text = f"""
    Nuevo mensaje de contacto desde Buena Vida
    
    Nombre: {name}
    Email: {email}
    
    Mensaje:
    {message}
    """
    
    # Crear el cuerpo del email en HTML
    html = f"""
    <html>
      <body>
        <h2>Nuevo mensaje de contacto desde Buena Vida</h2>
        <p><strong>Nombre:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Mensaje:</strong></p>
        <p>{message}</p>
      </body>
    </html>
    """
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    msg.attach(part1)
    msg.attach(part2)
    
    return msg

# Probar la creación del mensaje
test_msg = create_contact_email(
    "Juan Pérez",
    "juan@example.com",
    "Hola, me gustaría más información sobre las clases de natación.",
    "buena.vida@example.com"
)

print("\n✓ Función de creación de email funciona correctamente")
print(f"✓ Asunto: {test_msg['Subject']}")
print(f"✓ De: {test_msg['From']}")
print(f"✓ Para: {test_msg['To']}")