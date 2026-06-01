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

# Definição do agente — model + instrução + tools
agente_credito = Agent(
    model="gemini-2.0-flash",
    name="agente_credito",
    description="Atendente de crédito do X",
    instruction="""Você é um assistente de análise de crédito.
    Quando o cliente perguntar sobre limite ou empréstimo, 
    use a tool verificar_limite_credito antes de responder.
    Seja claro e objetivo. Nunca invente valores — só use a tool.""",
    tools=[verificar_limite_credito],
)
