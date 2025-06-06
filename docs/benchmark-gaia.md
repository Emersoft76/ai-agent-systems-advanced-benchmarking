# 🧪 GAIA Benchmark & Agent Reasoning  
> Benchmark GAIA e Raciocínio do Agente

---

## EN – What is the GAIA Benchmark?

**GAIA** (General AI Agent Assessment) is an advanced benchmark designed to evaluate autonomous reasoning, planning, memory use, and tool execution in intelligent agents.  
It simulates realistic tasks, with multi-step goals that require contextual understanding and tool orchestration.

Although GAIA is not open-source, this project includes a **simulated version**, inspired by its logic, to allow local testing and training.

---

### 🎯 Educational Objectives

- Train agents to decompose tasks and reason with context
- Integrate memory and tools dynamically
- Benchmark output accuracy with a scoring function
- Compare agents and configurations across test cases

---

### ⚙️ Simulation Components

| Module               | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `agent_self_reflection.py` | Reasoning loop with self-evaluation                     |
| `prompt-strategy.md`      | Dynamic prompt selection, fallback logic                |
| `multimodal_task_runner.py` | Handles image + document queries                     |
| `test_benchmark_score.py`  | Simulated benchmark with scoring                       |

---

## PT – O que é o Benchmark GAIA?

**GAIA** (Avaliação Geral de Agentes de IA) é um benchmark avançado projetado para avaliar o raciocínio autônomo, o planejamento, o uso de memória e a execução de ferramentas por agentes inteligentes.  
Ele simula tarefas realistas com múltiplas etapas, exigindo compreensão contextual e coordenação de ferramentas.

Embora o GAIA não seja de código aberto, este projeto inclui uma **versão simulada** inspirada em sua lógica, permitindo testes e treinamentos locais.

---

### 🎯 Objetivos Educacionais

- Treinar agentes para decompor tarefas e raciocinar com contexto
- Integrar memória e ferramentas dinamicamente
- Avaliar a precisão das respostas com função de pontuação
- Comparar agentes e configurações em diferentes testes

---

### ⚙️ Componentes da Simulação

| Módulo                    | Descrição                                                  |
|---------------------------|------------------------------------------------------------|
| `agent_self_reflection.py` | Loop de raciocínio com autoavaliação                      |
| `prompt-strategy.md`       | Seleção dinâmica de prompt e lógica de fallback           |
| `multimodal_task_runner.py` | Consulta multimodal: imagem + documento                   |
| `test_benchmark_score.py`   | Benchmark simulado com sistema de pontuação              |

---

📂 See also:  
- [Architecture Overview](architecture.md)  
- [Prompt Strategy](prompts-strategy.md)  
- [Vision Pipeline](multimodal-vision.md)

---
