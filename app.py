from flask import Flask, request
import openai
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from config import THERAPIST_PROMPT

app = Flask(__name__)

# Configure a chave da API OpenAI usando variáveis de ambiente
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configuração do Twilio
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_client = Client(twilio_account_sid, twilio_auth_token)

@app.route('/')
def home():
    # Verificação da conexão com a API OpenAI
    try:
        openai.Engine.list()
        openai_status = "conectado"
    except Exception as e:
        openai_status = f"não conectado ({str(e)})"
    
    # Verificação da conexão com a API Twilio
    try:
        twilio_client.api.accounts.list()
        twilio_status = "conectado"
    except Exception as e:
        twilio_status = f"não conectado ({str(e)})"
    
    return f"Servidor ativo. Status da API OpenAI: {openai_status}. Status da API Twilio: {twilio_status}."

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    # Obtenha a mensagem do usuário
    user_message = request.form.get('Body')

    # Faça a solicitação para a API OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=THERAPIST_PROMPT + user_message,
        max_tokens=150
    )

    # Obtenha a resposta do ChatGPT
    chatbot_reply = response.choices[0].text.strip()

    # Crie uma resposta para o Twilio
    resp = MessagingResponse()
    resp.message(chatbot_reply)

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
