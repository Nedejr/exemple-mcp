# Agente de Análise de Ações com LangGraph e MCP

Este projeto demonstra a criação de um agente de IA para análise financeira usando LangChain, LangGraph e o Multi-Component Protocol (MCP). O agente é capaz de responder a perguntas sobre o mercado de ações, como cotações atuais, dados históricos e informações de empresas.

São apresentados dois exemplos de implementação:

1.  `sample_agent.py`: Um agente síncrono que utiliza ferramentas definidas localmente.
2.  `mcp_agent.py`: Um agente assíncrono mais avançado que consome ferramentas de um servidor remoto via MCP.

## Funcionalidades

O agente pode utilizar as seguintes ferramentas para responder às perguntas:

- **Obter preço atual da ação**: Retorna a cotação mais recente de um ticker.
- **Obter dados históricos**: Fornece o histórico de preços para um determinado período.
- **Obter informações da empresa**: Retorna dados gerais sobre a empresa (setor, resumo, etc.).

## Estrutura do Projeto

```
stock_agent/
├── .env            # Arquivo para variáveis de ambiente (não versionado)
├── mcp_agent.py    # Ponto de entrada para o agente principal (assíncrono com MCP)
├── sample_agent.py # Ponto de entrada para o agente de exemplo (síncrono local)
├── tools.py        # Definição das ferramentas locais que usam a biblioteca yfinance
├── mcp_servers.py  # Configuração dos servidores MCP remotos
└── README.md       # Este arquivo
```

- `mcp_agent.py`: Implementa o agente principal. Ele se conecta a um servidor MCP (configurado em `mcp_servers.py`) para obter dinamicamente as ferramentas disponíveis e as executa de forma assíncrona.
- `sample_agent.py`: Uma implementação mais simples que importa e utiliza as ferramentas diretamente do arquivo `tools.py`. Serve como um exemplo base de um agente ReAct com LangGraph.
- `tools.py`: Contém a lógica de negócio das ferramentas. As funções são decoradas com `@tool` da LangChain e utilizam a biblioteca `yfinance` para buscar os dados financeiros.
- `mcp_servers.py`: Define os dicionários de configuração para os servidores MCP. Neste exemplo, ele está configurado para se conectar a um endpoint da Smithery.ai que serve as ferramentas financeiras.

## Instalação e Configuração

Siga os passos abaixo para preparar o ambiente de execução.

### 1. Crie um Ambiente Virtual

É uma boa prática isolar as dependências do projeto.

```bash
python -m venv .venv
source .venv/bin/activate
# No Windows, use: .venv\Scripts\activate
```

### 2. Instale as Dependências

Instale todas as bibliotecas Python necessárias.

```bash
pip install langchain langgraph langchain-openai yfinance python-dotenv langchain-mcp-adapters
```

### 3. Configure as Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto, copiando o exemplo abaixo.

```ini
# .env
OPENAI_API_KEY="sk-sua-chave-da-openai"
SMITHERY_API_KEY="sua-chave-da-smithery-ai"
```

- `OPENAI_API_KEY`: Sua chave de API da OpenAI, necessária para o modelo de linguagem (`gpt-5-mini`).
- `SMITHERY_API_KEY`: Sua chave de API da Smithery.ai, necessária para se conectar ao servidor MCP remoto em `mcp_agent.py`.

## Como Executar

Você pode interagir com qualquer um dos dois agentes.

### Executando o Agente Principal (com MCP)

Este agente se conecta a um servidor remoto para obter as ferramentas.

```bash
python mcp_agent.py
```

### Executando o Agente de Exemplo (Local)

Este agente usa as ferramentas definidas localmente no arquivo `tools.py`.

```bash
python sample_agent.py
```

Após iniciar um dos agentes, você verá um prompt para interagir:

```
Digite: Qual o preço atual da PETR4.SA?
```
