# 🧠 Projeto Streamlit - Execução Local

### Pré-requisitos

- Python 3.10 ou superior instalado
- Acesso ao terminal (Prompt de Comando, PowerShell, Terminal ou Bash)
- Editor de código como VS Code (opcional, mas recomendado)

---

### Passo a Passo para Rodar Localmente

### 1. Abrir o Terminal na Pasta do Projeto

Abra o terminal e navegue até a pasta onde extraiu o projeto:

#### Windows:

```powershell``
cd "C:\Users\SeuUsuario\Downloads\nome-da-pasta"

### 2. Criar e Ativar o Ambiente Virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

### 3. Instalar as Dependências
exe: pip install streamlit numpy pandas matplotlib seaborn

### 4. Executar a Aplicação
streamlit run app.py
