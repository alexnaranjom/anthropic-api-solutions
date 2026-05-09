# Building with the Claude API

A hands-on learning path for the [Anthropic Claude API](https://docs.anthropic.com/), covering foundational concepts through practical Jupyter notebooks.

## What's covered

### Requests & core concepts

| Notebook | Topic |
|---|---|
| `001Request.ipynb` | Basic API requests, multi-turn conversations, conversation history |
| `002Request.ipynb` | System prompts — controlling model behavior and persona |
| `003Request.ipynb` | Temperature — tuning response creativity and randomness |
| `004Request.ipynb` | Extended functionality |

### Tool use (function calling)

| Notebook | Topic |
|---|---|
| `001_tools.ipynb` | Defining and calling tools |
| `002_tools_multiple_responses.ipynb` | Handling multiple tool calls in one turn |
| `003_tool_streaming.ipynb` | Streaming with tool use |
| `005_text_editor_tool.ipynb` | Building a reusable text editor tool |

### Advanced features

| Notebook | Topic |
|---|---|
| `001_thinking.ipynb` | Extended thinking with budget tokens |
| `002_images.ipynb` | Vision — sending image inputs |

### Prompting & evaluation

| Notebook | Topic |
|---|---|
| `001_prompt_evals.ipynb` | Evaluating prompt quality |
| `002_prompting_completed.ipynb` | Advanced prompting strategies |

### Retrieval-Augmented Generation (RAG)

| Notebook | Topic |
|---|---|
| `001_chunking.ipynb` | Text chunking strategies |
| `002_embeddings.ipynb` | Generating and using embeddings for semantic search |
| `003_vectordb.ipynb` | Vector database integration |
| `004_bm25.ipynb` | BM25 lexical search |
| `005_hybrid.ipynb` | Hybrid search — combining semantic and lexical (Reciprocal Rank Fusion) |
| `006_web_search.ipynb` | Web search integration |

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
├── notebooks/        # Jupyter notebooks (see table above)
├── images/           # Image assets used in notebooks
├── scr/              # Standalone Python scripts
├── .env.example      # Environment variable template
├── requirements.txt  # Python dependencies
└── README.md
```

## Tech stack

- Python 3.13
- [anthropic](https://pypi.org/project/anthropic/) 0.97.0
- [python-dotenv](https://pypi.org/project/python-dotenv/) 1.2.2
- Jupyter Notebook
