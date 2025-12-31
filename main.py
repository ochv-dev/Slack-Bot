import os
import requests

# 1. Configuración
token = os.environ["SLACK_USER_TOKEN"]
channel_id = "C09L7DNJ25U"  # <--- Tu ID de Asistencia ya puesto
mensaje = "Estoy"

# 2. Enviar mensaje como USUARIO REAL
url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": f"Bearer {token}"}
data = {
    "channel": channel_id,
    "text": mensaje,
    "as_user": True 
}

try:
    response = requests.post(url, headers=headers, json=data)
    respuesta_json = response.json()
    
    if response.status_code == 200 and respuesta_json.get("ok"):
        print("✅ Mensaje enviado (Modo Ninja activado).")
    else:
        print(f"❌ Error: {respuesta_json}")
        exit(1)
except Exception as e:
    print(f"Error de conexión: {e}")
    exit(1)