from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from tools import current_stock_price, get_company_info, get_historical_stock_price

# -------------------------------------------------------------------
# Carregar variáveis de ambiente (ex: OPENAI_API_KEY)
# -------------------------------------------------------------------
load_dotenv()

# -------------------------------------------------------------------
# Configuração do modelo e memória
# -------------------------------------------------------------------
model = ChatOpenAI(model="gpt-5-mini")
checkpointer = MemorySaver()  # substitui o antigo 'memory'

# -------------------------------------------------------------------
# Ferramentas disponíveis para o agente
# -------------------------------------------------------------------
tools = [
    current_stock_price,
    get_company_info,
    get_historical_stock_price,
]

# -------------------------------------------------------------------
# Criação do agente
# -------------------------------------------------------------------
# ✅ A nova API aceita somente 'model', 'tools' e 'checkpointer'
agent_executor = create_react_agent(
    model=model,
    tools=tools,
    checkpointer=checkpointer,
)

# -------------------------------------------------------------------
# Configuração de sessão/threads
# -------------------------------------------------------------------
config = {"configurable": {"thread_id": "1"}}

# Prompt do sistema (mensagem inicial de contexto)
system_prompt = (
    "Você é um agente analista financeiro e deve utilizar suas ferramentas "
    "para responder às perguntas dos usuários."
)

# -------------------------------------------------------------------
# Loop principal
# -------------------------------------------------------------------
while True:
    user_text = input("Digite: ")

    # Mensagens enviadas ao agente
    # ✅ O system_prompt vai como mensagem 'system' dentro de 'messages'
    input_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_text},
    ]

    # Stream de respostas do agente
    for step in agent_executor.stream(
        {"messages": input_messages},  # sempre 'messages'
        config=config,
        stream_mode="values",
    ):
        # Exibe a última mensagem gerada pelo agente
        step["messages"][-1].pretty_print()
