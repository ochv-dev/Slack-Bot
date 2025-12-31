import os
import requests
import json

# Lee la URL secreta que guardaste en GitHub
webhook_url = os.environ["SLACK_WEBHOOK_URL"]

# El mensaje a enviar
payload = {"text": "Estoy"}

try:
    response = requests.post(
        webhook_url, 
        data=json.dumps(payload), 
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code == 200:
        print("Mensaje enviado con éxito.")
    else:
        print(f"Error ({response.status_code}): {response.text}")
        exit(1) # Falla el workflow si Slack rechaza el mensaje
except Exception as e:
    print(f"Error de conexión: {e}")
    exit(1)