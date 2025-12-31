# 🤖 Bot de Asistencia Automática para Slack

Este proyecto es una automatización en Python diseñada para gestionar el envío de mensajes de asistencia ("Estoy") en canales de Slack de forma programada, utilizando **GitHub Actions**.

## 🚀 ¿Cómo funciona?

El sistema combina un script de Python con un flujo de trabajo (workflow) en la nube:

1.  **Script (`main.py`):** Utiliza la API de Slack (`chat.postMessage`) para enviar un mensaje. A diferencia de los Webhooks tradicionales, este script usa un **Token de Usuario (OAuth)** para que el mensaje aparezca enviado por la persona real, sin etiquetas de "Bot" o "App".
2.  **Automatización (`cron.yml`):** Un trabajo de Cron en GitHub Actions ejecuta el script automáticamente de lunes a viernes a las 8:30 AM (hora Chile).

## 🛠️ Configuración (Si quieres usarlo)

Si eres un compañero y quieres implementar esto, sigue estos pasos:

### 1. Requisitos Previos
* Una cuenta de GitHub.
* Acceso al espacio de trabajo de Slack.

### 2. Obtener Credenciales de Slack
1.  Ve a [api.slack.com/apps](https://api.slack.com/apps) y crea una App.
2.  En **OAuth & Permissions**, añade el permiso de usuario `chat:write`.
3.  Instala la App en tu espacio de trabajo y copia el **User OAuth Token** (empieza por `xoxp-...`).
4.  Obtén el **ID del Canal** donde quieres enviar la asistencia (Click derecho en el canal -> Ver detalles).

### 3. Configurar el Repositorio
1.  Haz un **Fork** de este repositorio.
2.  En tu repositorio, ve a **Settings > Secrets and variables > Actions**.
3.  Crea un nuevo secreto llamado `SLACK_USER_TOKEN` y pega tu token `xoxp`.
4.  Edita el archivo `main.py`:
    ```python
    # Cambia esto por TU ID de canal
    channel_id = "C0XXXXXX" 
    ```

## ⚠️ Disclaimer (Para el Profesor)

Si estás leyendo esto porque el bot falló, se envió un sábado, o simplemente me descubrieron:

> **"Profe, no diga que no lo intenté. Identifiqué un problema repetitivo (despertar, abrir Slack, escribir) y apliqué una solución tecnológica usando APIs REST, autenticación OAuth y CI/CD en la nube. ¡Técnicamente, es una aplicación práctica de lo aprendido en clase!"**

---
*Este proyecto fue realizado con fines educativos (y de eficiencia de sueño).*