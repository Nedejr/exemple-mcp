import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from mcp_servers import MCP_SERVERS_CONFIG


async def main():

    # -------------------------------------------------------------------
    # Configuração do modelo e memória
    # -------------------------------------------------------------------
    model = ChatOpenAI(model="gpt-5-mini")
    memory = MemorySaver()  # substitui o antigo 'memory'

    # -------------------------------------------------------------------
    # Ferramentas disponíveis para o agente
    # -------------------------------------------------------------------
    mcp_client = MultiServerMCPClient(MCP_SERVERS_CONFIG)
    tools = await mcp_client.get_tools()

    # -------------------------------------------------------------------
    # Criação do agente
    # -------------------------------------------------------------------
    # ✅ A nova API aceita somente 'model', 'tools' e 'checkpointer'
    agent_executor = create_react_agent(
        model=model,
        tools=tools,
        checkpointer=memory,
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
        user_text = await asyncio.to_thread(input, "Digite: ")

        # Mensagens enviadas ao agente
        # ✅ O system_prompt vai como mensagem 'system' dentro de 'messages'
        input_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ]

        # Stream de respostas do agente
        async for step in agent_executor.astream(
            {"messages": input_messages},  # sempre 'messages'
            config=config,
            stream_mode="values",
        ):
            # Exibe a última mensagem gerada pelo agente
            step["messages"][-1].pretty_print()


asyncio.run(main())
