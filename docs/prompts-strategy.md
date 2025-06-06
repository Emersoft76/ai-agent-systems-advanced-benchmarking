# 🧩 Prompt Strategies & Fallback Logic  
> Estratégias de Prompts e Lógica de Recuo

---

## EN – Advanced Prompt Engineering

Prompt engineering is critical to agent performance. This project employs adaptive strategies to dynamically tailor prompts based on context, model feedback, and error detection.

### 🔄 Prompt Flow Architecture

1. **Base Prompt Template:** Defines task format, tone, and goals  
2. **Dynamic Slot Injection:** Inserts contextual variables (tools, queries, history)  
3. **Model Feedback Parsing:** Detects failure, hallucination, or irrelevant answers  
4. **Fallback Activation:** Switches to alternative phrasing or smaller tasks  
5. **Self-Reflection Re-entry:** Re-attempts the task with adjusted strategy

---

## 🔧 Prompt Optimization Techniques

| Technique              | Purpose                                         |
|------------------------|-------------------------------------------------|
| Chain-of-Thought (CoT) | Enables reasoning steps                         |
| Few-Shot Examples      | Improves accuracy on known formats              |
| Output Constraints     | Enforces JSON/Markdown formatting               |
| Tool-Aware Context     | Aligns prompts with available external tools    |
| Retry + Logging        | Captures failed runs for fine-tuning            |

---

## PT – Engenharia de Prompts Avançada

A engenharia de prompts é essencial para o desempenho do agente. Este projeto usa estratégias adaptativas para ajustar dinamicamente os prompts com base no contexto, no feedback do modelo e na detecção de erros.

### 🔄 Arquitetura do Fluxo de Prompts

1. **Template Base de Prompt:** Define o formato, tom e objetivo  
2. **Injeção de Variáveis:** Insere dados de contexto, ferramentas e histórico  
3. **Análise de Feedback:** Detecta falhas, alucinações ou respostas irrelevantes  
4. **Ativação de Recuo:** Usa variações alternativas ou subtarefas menores  
5. **Reentrada por Autoavaliação:** Retenta a tarefa com estratégia ajustada

---

## 🔧 Técnicas de Otimização de Prompt

| Técnica                 | Objetivo                                       |
|-------------------------|------------------------------------------------|
| Chain-of-Thought (CoT)  | Permite raciocínio em etapas                   |
| Exemplos Few-Shot       | Aumenta precisão com formatos conhecidos       |
| Restrições de Saída     | Garante formatação JSON/Markdown               |
| Contexto de Ferramenta  | Alinha o prompt às ferramentas disponíveis     |
| Retry + Logging         | Registra falhas para ajustes e melhorias       |

---

📂 Continue reading:  
- [Architecture](architecture.md)  
- [Vision & Multimodal](multimodal-vision.md)  
- [MCP Tool Protocol](mcp-protocol.md)

---
