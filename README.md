## Deploy de Aplicação Streamlit na AWS EC2
Como fazer o deploy de uma aplicação Streamlit em uma instância EC2 da AWS para acesso externo.

### Pré-requisitos
Instância EC2 ativa na AWS
Acesso SSH ou EC2 Instance Connect à instância
Security Group configurado
Aplicação Streamlit local pronta

### Passo a Passo

### 1. Conectar à Instância EC2
Opção A: Via Console AWS (Recomendado)

Acesse o Console AWS > EC2 > Instances
Selecione sua instância
Clique em Connect
Escolha EC2 Instance Connect

Opção B: Via SSH
bashssh -i sua-chave.pem ubuntu@SEU_IP_EC2

### 2. Preparar o Ambiente na EC2
Atualizar o sistema:
bashsudo apt update
sudo apt install python3-venv python3-full -y
Criar ambiente virtual:
bashpython3 -m venv streamlit_env
Ativar ambiente virtual:
bashsource streamlit_env/bin/activate

### 3. Instalar Dependências
bash# Atualizar pip
pip install --upgrade pip

### Instalar bibliotecas necessárias
pip install numpy pandas matplotlib seaborn streamlit

### 4. Criar/Transferir o Arquivo da Aplicação
Opção A: Criar diretamente na EC2
bashnano app.py
Cole seu código Python e salve com:

Ctrl + X
Y
Enter

### 5. Executar a Aplicação Streamlit
bashstreamlit run app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true

### 6. Acessar a Aplicação
Abra seu navegador e acesse:
http://SEU_IP_PUBLICO_EC2:8501
