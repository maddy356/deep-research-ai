# Deep Research AI Agent System

This project is a dual-agent research system built using Tavily, LangGraph, and LangChain.

## Features
- A Research Agent that collects and summarizes online data
- A Drafting Agent that writes a final response using a language model

## Setup Instructions

```bash
git clone https://github.com/yourusername/deep-research-ai.git
cd deep-research-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Edit and add your API keys
```

## Running

```bash
python main_graph.py
```

Enter a topic and the AI agents will do the rest!