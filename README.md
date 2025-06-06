# 🧠 AI Agent Systems – Advanced Benchmarking & Reasoning Toolkit  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![LangChain](https://img.shields.io/badge/LangChain-Framework-informational?logo=langchain&color=blue)](https://www.langchain.com/)  
[![OpenAI](https://img.shields.io/badge/OpenAI-LLMs-green?logo=openai&logoColor=white)](https://openai.com/)  
[![Claude](https://img.shields.io/badge/Claude-Vision-orange)](https://www.anthropic.com/index/claude)  
[![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-blueviolet?logo=data&logoColor=white)](https://www.pinecone.io/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success?logo=fastapi)](https://fastapi.tiangolo.com/)  

---

## 📘 Overview | Visão Geral

**EN:**  
This project provides a complete educational and practical implementation of an AI agent system with reasoning, multimodal input handling, and GAIA-style benchmark optimization. It includes real examples, technical documentation, and local environment setup (Linux & Windows).

**PT-BR:**  
Este projeto oferece uma implementação educacional e prática de um sistema de agentes de IA com raciocínio, entrada multimodal e otimização baseada no benchmark GAIA. Inclui exemplos reais, documentação técnica e configuração do ambiente local (Linux e Windows).

---

## 📂 Repository Structure | Estrutura do Repositório

- 📄 [README.md](README.md)  
- 📁 [docs](docs/)  
  - 📄 [architecture.md](docs/architecture.md)  
  - 📄 [benchmark-gaia.md](docs/benchmark-gaia.md)  
  - 📄 [prompts-strategy.md](docs/prompts-strategy.md)  
  - 📄 [multimodal-vision.md](docs/multimodal-vision.md)  
  - 📄 [mcp-protocol.md](docs/mcp-protocol.md)  
  - 📄 [deployment-guide.md](docs/deployment-guide.md)  
- 📁 [examples](examples/)  
  - 📄 [agent_self_reflection.py](examples/agent_self_reflection.py)  
  - 📄 [async_pipeline_demo.py](examples/async_pipeline_demo.py)  
  - 📄 [document_parser_gpt4v.py](examples/document_parser_gpt4v.py)  
  - 📄 [multimodal_task_runner.py](examples/multimodal_task_runner.py)  
- 📁 [src](src/)  
  - 📁 [core](src/core/)  
  - 📁 [tools](src/tools/)  
  - 📁 [vision](src/vision/)  
  - 📁 [prompts](src/prompts/)  
  - 📁 [utils](src/utils/)  
- 📁 [tests](tests/)  
  - 📄 [test_benchmark_score.py](tests/test_benchmark_score.py)  
- 📄 [.env.example](.env.example)  
- 📄 [requirements.txt](requirements.txt)  
- 📄 [setup.sh](setup.sh)  
- 📄 [run_demo.py](run_demo.py)

---

## 🔗 Quick Access | Acesso Rápido

- 📘 [Architecture Overview](docs/architecture.md)  
- 🧠 [GAIA Benchmark & Agent Reasoning](docs/benchmark-gaia.md)  
- 🔁 [Prompt Strategies & Fallback Logic](docs/prompts-strategy.md)  
- 🖼️ [Multimodal Processing (Vision Models)](docs/multimodal-vision.md)  
- 🔧 [Tool Integration via MCP](docs/mcp-protocol.md)  
- 🚀 [Deployment Guide (Linux & Windows)](docs/deployment-guide.md)

---

  | Tecnologia       | Descrição                                  | Link Oficial                                            |
| ---------------- | ------------------------------------------ | ------------------------------------------------------- |
| **LangChain**    | Framework para agentes LLM                 | [langchain.com](https://www.langchain.com)              |
| **OpenAI GPT**   | Modelos LLM para linguagem e visão         | [openai.com](https://openai.com)                        |
| **Claude AI**    | Multimodal Vision Model (OCR, doc parsing) | [anthropic.com](https://www.anthropic.com/index/claude) |
| **FastAPI**      | Backend para APIs de agentes               | [fastapi.tiangolo.com](https://fastapi.tiangolo.com)    |
| **Pinecone**     | Banco vetorial para memória semântica      | [pinecone.io](https://www.pinecone.io)                  |
| **Docker**       | Containerização e deploy                   | [docker.com](https://www.docker.com/)                   |
| **Python 3.10+** | Linguagem principal do projeto             | [python.org](https://www.python.org/)                   |

---

## ⚙️ Setup (Linux & Windows)
```bash
# Clone o projeto
git clone https://github.com/Emersoft76/ai-agent-systems-advanced-benchmarking.git
cd ai-agent-systems-advanced-benchmarking

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o demo
python run_demo.py
```
---

## 📜 License

MIT © Emerson Maciel — Educational AI Repository
LICENSE

---

🚧 Em desenvolvimento ativo. Mais exemplos práticos e integrações serão adicionados em breve.

---

  
