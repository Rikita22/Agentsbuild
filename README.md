# aiagents

Learning examples built with [AgentSpan](https://pypi.org/project/agentspan/).

## Scripts

| Script | Description |
|--------|-------------|
| `agent1.py` | Basic assistant with a `get_current_time` tool |
| `agent2.py` | Support bot with guardrails and human-in-the-loop refund approval |
| `agent3.py` | Multi-agent research pipeline (Firecrawl web search + report writing) |

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
```

## Run

```bash
python agent1.py
python agent2.py
python agent3.py
```

## Environment variables

| Variable | Required by | Description |
|----------|-------------|-------------|
| `OPENAI_API_KEY` | All agents | OpenAI API key |
| `FIRECRAWL_API_KEY` | `agent3.py` | Firecrawl API key for web search |
