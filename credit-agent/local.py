# Ou chamar por código Python direto
from dotenv import load_dotenv
load_dotenv()

from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from agent import agente_credito

session_svc = InMemorySessionService()
session_svc.create_session_sync(app_name="credito_bv", user_id="user_123", session_id="sessao_456")
runner = Runner(
    agent=agente_credito,
    app_name="credito_bv",
    session_service=session_svc,
)

# Enviar mensagem e ler eventos de resposta
new_message = types.Content(
    role="user",
    parts=[types.Part(text="Quero um empréstimo de R$8.000")],
)
for event in runner.run(
    user_id="user_123",
    session_id="sessao_456",
    new_message=new_message,
):
    if event.is_final_response():
        print(event.response.text)