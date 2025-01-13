from flask import Flask, request
import openai
import os
from twilio.twiml.messaging_response import MessagingResponse
from config import THERAPIST_PROMPT

app = Flask(__name__)

# Configure a chave da API OpenAI usando variáveis de ambiente
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return "Olá, mundo!"

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
