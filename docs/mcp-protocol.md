# 🔧 MCP – Model Context Protocol  
> Protocolo de Contexto do Modelo (MCP)

---

## EN – What is MCP?

The **Model Context Protocol (MCP)** is a flexible layer that allows intelligent agents to dynamically plug and route external tools (APIs, functions, libraries) into the reasoning pipeline.

This modular integration enhances the agent’s abilities by offering contextual access to capabilities like web search, math, code execution, and custom functions.

---

## 🔌 Architecture Overview

User Query → Agent → MCP → Tool Selection → Tool Execution → Agent Response


- **Router Layer:** Matches the task with the appropriate tool
- **Schema Injector:** Formats the input/output to match agent expectations
- **Execution Layer:** Invokes the external function asynchronously
- **Logging & Fallback:** Monitors success, retries or disables faulty tools

---

## 🧰 Examples of Tool Types

| Tool Type        | Example                                  |
|------------------|-------------------------------------------|
| Calculator       | MathJS, WolframAlpha API                  |
| Web Search       | SerpAPI, DuckDuckGo Scraper               |
| Document Parser  | PDF Extractors, OCR (Tesseract)           |
| Code Interpreter | Python sandbox, Jupyter kernel            |
| Custom API       | Internal business logic or SaaS functions |

---

## PT – O que é o MCP?

O **Model Context Protocol (MCP)** é uma camada de integração flexível que permite ao agente inteligente acoplar e utilizar ferramentas externas (APIs, funções, bibliotecas) de forma dinâmica e contextual.

Essa integração modular amplia as capacidades do agente com recursos como busca web, cálculo, execução de código, e APIs específicas.

---

## 🔌 Visão Geral da Arquitetura

Consulta → Agente → MCP → Seleção de Ferramenta → Execução → Resposta do Agente


- **Camada de Roteamento:** Identifica a ferramenta ideal para cada tarefa  
- **Injeção de Esquema:** Adapta entradas e saídas ao padrão do agente  
- **Camada de Execução:** Invoca a ferramenta de forma assíncrona  
- **Logs e Fallback:** Monitora resultados e executa recuos, se necessário

---

## 🧰 Exemplos de Ferramentas Integráveis

| Tipo de Ferramenta | Exemplo                                    |
|---------------------|---------------------------------------------|
| Calculadora         | MathJS, WolframAlpha API                    |
| Busca Web           | SerpAPI, DuckDuckGo Scraper                 |
| Leitor de Documentos| Extratores de PDF, OCR com Tesseract        |
| Interpretador de Código | Sandbox Python, kernel Jupyter        |
| API Customizada     | Lógicas internas ou APIs de SaaS            |

---

📂 See also:  
- [Architecture](architecture.md)  
- [Multimodal Processing](multimodal-vision.md)  
- [Deployment Guide](deployment-guide.md)

---
