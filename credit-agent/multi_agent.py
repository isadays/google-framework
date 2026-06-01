from google.adk.agents import Agent

# Tool: função Python comum com docstring clara
def verificar_limite_credito(cpf: str, valor: float) -> dict:
    """Verifica se o cliente tem limite disponível para um empréstimo.
    
    Args:
        cpf: CPF do cliente (string, 11 dígitos)
        valor: Valor do empréstimo solicitado em reais
    
    Returns:
        dict com status e limite disponível
    """
    # Aqui seria uma chamada real ao sistema de crédito
    limite_disponivel = 15000.0
    aprovado = valor <= limite_disponivel
    return {
        "aprovado": aprovado,
        "limite_disponivel": limite_disponivel,
        "valor_solicitado": valor
    }
# Agente especialista 1 — análise de crédito
agente_analise = Agent(
    model="gemini-2.0-flash",
    name="analise_credito",
    description="Especialista em analisar risco de crédito de clientes",
    instruction="Analise o perfil de crédito e retorne score e recomendação.",
    tools=[verificar_limite_credito],
)

# Agente especialista 2 — atendimento
agente_atendimento = Agent(
    model="gemini-2.0-flash",
    name="atendimento",
    description="Especialista em comunicar decisões ao cliente com empatia",
    instruction="Comunique a decisão de crédito de forma clara e humana.",
)

# Orquestrador — decide qual agente usar
orquestrador = Agent(
    model="gemini-2.0-flash",
    name="orquestrador_x",
    instruction="""Você coordena o processo de análise de crédito.
    1. Delegue análise técnica para analise_credito
    2. Delegue comunicação para atendimento
    Não faça nada sozinho — sempre delegue.""",
    # sub_agents: agentes que podem ser chamados
    sub_agents=[agente_analise, agente_atendimento],
)
