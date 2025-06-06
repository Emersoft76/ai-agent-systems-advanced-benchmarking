# 🚀 Deployment Guide (Linux & Windows)  
> Guia de Deploy (Linux e Windows)

---

## EN – Installation & Setup

### ✅ Prerequisites

- Python 3.10+  
- Git  
- Pip or virtualenv  
- Optional: Docker (for sandbox environments)

---

### 🐧 Linux Setup

```bash
# 1. Clone the repository
git clone https://github.com/YourUser/your-agent-project.git
cd your-agent-project

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the agent
python main.py
```
---

## 🪟 Windows Setup
```powershell
# 1. Clone the repository
git clone https://github.com/YourUser/your-agent-project.git
cd your-agent-project

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the agent
python main.py
```
---

## 🐳 Docker Setup (Optional)
```bash
docker build -t ai-agent .
docker run -it ai-agent
```
---

## PT – Instalação e Configuração

### ✅ Pré-requisitos

- Python 3.10+
- Git
- Pip ou virtualenv
- Opcional: Docker (ambiente isolado)

---

## 🐧 Configuração no Linux
```bash
# 1. Clonar o repositório
git clone https://github.com/SeuUsuario/seu-projeto-agente.git
cd seu-projeto-agente

# 2. Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar o agente
python main.py
```
---

## 🪟 Configuração no Windows
```bash
# 1. Clonar o repositório
git clone https://github.com/SeuUsuario/seu-projeto-agente.git
cd seu-projeto-agente

# 2. Criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar o agente
python main.py
```
---

## 🔍 Troubleshooting

| Issue                     | Solution                                         |
| ------------------------- | ------------------------------------------------ |
| Permission denied (Linux) | Run `chmod +x script.sh` or `sudo`               |
| venv not activating       | Use full path to `activate` script               |
| Missing dependency        | Reinstall with `pip install -r requirements.txt` |

---

Ready! Return to README.md or start testing with benchmark... ok?! ;-)...

---
