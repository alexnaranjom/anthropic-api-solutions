# Building with the Claude API

A hands-on learning path for the [Anthropic Claude API](https://docs.anthropic.com/), covering foundational concepts through practical Jupyter notebooks.

## What's covered

| Notebook | Topic |
|---|---|
| `001Request.ipynb` | Basic API requests, multi-turn conversations, conversation history |
| `002Request.ipynb` | System prompts — controlling model behavior and persona |
| `003Request.ipynb` | Temperature — tuning response creativity and randomness |

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/alexnaranjom/anthropic-api-solutions.git
cd anthropic-api-solutions
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

```bash
cp .env.example .env
# Open .env and add your key:
# ANTHROPIC_API_KEY="sk-ant-..."
```

Get an API key at [console.anthropic.com](https://console.anthropic.com/).

### 5. Launch Jupyter

```bash
jupyter notebook
```

Open any notebook in the `notebooks/` folder and run the cells in order.

## Project structure

```
anthropic-api-solutions/
├── notebooks/
│   ├── 001Request.ipynb   # Conversations & multi-turn chat
│   ├── 002Request.ipynb   # System prompts
│   └── 003Request.ipynb   # Temperature control
├── scr/                   # Standalone Python scripts (in progress)
├── .env.example           # Environment variable template
├── requirements.txt       # Python dependencies
└── README.md
```

## Roadmap

- [ ] Tool use (function calling)
- [ ] Vision — image inputs
- [ ] Streaming responses
- [ ] Prompt caching
- [ ] Batch requests
- [ ] Building a multi-turn CLI chatbot

## Tech stack

- Python 3.13
- [anthropic](https://pypi.org/project/anthropic/) 0.97.0
- [python-dotenv](https://pypi.org/project/python-dotenv/) 1.2.2
- Jupyter Notebook
