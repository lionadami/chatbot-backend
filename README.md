# Chatbot Backend

## Projeto: Chatbot Terapêutico com WhatsApp e OpenAI

Este projeto consiste na criação de um chatbot terapêutico que utiliza a API do WhatsApp (via Twilio) e a OpenAI (GPT-3) para interagir com usuários. O objetivo é fornecer respostas terapêuticas e orientações baseadas nas mensagens enviadas pelos usuários.

---

## Funcionalidades

1. **Integração com WhatsApp:**
   - Receber mensagens de usuários via WhatsApp.
   - Enviar respostas personalizadas utilizando a Twilio API.

2. **Geração de Respostas Inteligentes:**
   - Utilizar o modelo GPT-3 da OpenAI para processar e responder às mensagens de forma terapêutica.

3. **Hospedagem e Deploy:**
   - Backend hospedado na Render, utilizando Docker (opcional).

---

## Tecnologias Utilizadas

- **Linguagem:** Python
- **APIs:**
  - OpenAI (GPT-3)
  - Twilio (WhatsApp)
- **Hospedagem:** Render
- **Gerenciamento de Dependências:** pip
- **Controle de Versão:** Git/GitHub
- **Containerização (opcional):** Docker

---

## Pré-requisitos

1. **Python 3.9 ou superior.**
2. **Conta Twilio:**
   - Configure um número do WhatsApp.
   - Obtenha as credenciais (Account SID e Auth Token).
3. **Conta OpenAI:**
   - Gere a chave de API para acessar o GPT-3.
4. **Conta Render:**
   - Para hospedar o backend.
5. **Git:**
   - Repositório para controle de versão.

---

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/lionadami/chatbot-backend.git
   cd chatbot-backend
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` no diretório raiz:
     ```
     OPENAI_API_KEY=your_openai_api_key
     TWILIO_ACCOUNT_SID=your_twilio_account_sid
     TWILIO_AUTH_TOKEN=your_twilio_auth_token
     TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
     ```

---

## Execução Local

1. Certifique-se de que as variáveis de ambiente estão configuradas.
2. Execute o servidor:
   ```bash
   python app.py
   ```
3. Use ferramentas como o Postman ou o WhatsApp para interagir com o chatbot.

---

## Deploy no Render

1. Suba o código para um repositório no GitHub.
2. Crie um novo serviço no Render:
   - Escolha **Web Service**.
   - Selecione o repositório do GitHub.
   - Configure as variáveis de ambiente (conforme o arquivo `.env`).
3. Escolha a linguagem Python e finalize o setup.

---

## Exemplo de Uso

- O usuário envia: *"Como posso melhorar minha autoestima?"*
- O chatbot responde com base no modelo GPT-3: *"Melhorar sua autoestima envolve reconhecer seu valor, estabelecer metas pequenas e comemorar suas conquistas."*

---

## Estrutura do Projeto

```plaintext
chatbot-backend/
├── app.py             # Arquivo principal do backend
├── requirements.txt   # Dependências do projeto
├── .env.example       # Exemplo de variáveis de ambiente
├── README.md          # Documentação do projeto
└── Dockerfile         # Configuração opcional para Docker
```

---

## Dependências

- **openai**: Integração com GPT-3
- **twilio**: Envio e recebimento de mensagens via WhatsApp
- **python-dotenv**: Gerenciamento de variáveis de ambiente

Instale todas com:
```bash
pip install -r requirements.txt
```

---

## Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das alterações:
   ```bash
   git commit -m "Descrição da feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT.

---

## Contato

Criador: Rafael Lion Adami
- GitHub: [lionadami](https://github.com/lionadami)
- Email: rafael.lion.adami@example.com
