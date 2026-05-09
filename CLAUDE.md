# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A learning repository demonstrating Claude API features through Jupyter notebooks, progressing from basic requests to advanced RAG pipelines. All AI code uses the `anthropic` Python SDK.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
cp .env.example .env            # then add ANTHROPIC_API_KEY
jupyter notebook
```

## Running Tests

```bash
python -m pytest test.py        # unit tests for utility functions in main.py
python -m pytest test.py -k "test_name"  # single test
```

## Architecture

### Notebook Learning Path (`notebooks/`)

Notebooks are numbered and meant to be run sequentially within each topic group:

- **001–004 Request series** — basic API calls, system prompts, temperature, multi-turn conversation history
- **001–005 Tools series** — function/tool calling, multiple tool responses, streaming, TextEditorTool
- **001 Thinking** — extended thinking (budget tokens)
- **002 Images** — vision/multimodal inputs
- **001–006 RAG series** — chunking → embeddings → vector DB → BM25 → hybrid search → web search
- **Prompting/Evals** — prompt engineering, evaluation strategies

### Key Patterns

**Conversation history** is maintained as a plain list of `{"role": ..., "content": ...}` dicts passed to `client.messages.create()`.

**Tool use loop** — the standard agentic pattern used throughout: call the API, check `stop_reason == "tool_use"`, execute the tool, append a `tool_result` message, and call the API again.

**Hybrid RAG** (`005_hybrid.ipynb`) merges BM25 lexical scores with semantic (embedding cosine similarity) scores using Reciprocal Rank Fusion before passing context to Claude.

**Prompt caching** — where applicable, large static context (e.g., the `report.md` corpus) uses `cache_control: {"type": "ephemeral"}` on the last system-prompt block to reduce latency and cost.

### Supporting Files

- `main.py` / `test.py` — standalone pi-calculation utility (Machin formula); used to demonstrate unit testing patterns, not related to Claude API.
- `report.md` — large interdisciplinary text used as the retrieval corpus in RAG notebooks.
- `dataset.json` — sample dataset for eval/prompting notebooks.

## Environment

API key is loaded via `python-dotenv` from `.env`. All notebooks call `load_dotenv()` at the top and read `os.environ["ANTHROPIC_API_KEY"]`.
