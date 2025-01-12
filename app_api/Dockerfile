# Escolher a imagem base leve do Python. 'slim' : versão minimalista apenas com bibliotecas descritas no requirements.txt
FROM python:3.13-slim

# Configurar o diretório de trabalho dentro do container. Toda operação subsequente será relativa a essa pasta.
WORKDIR /appFastAPI

# Copiar o arquivo 'requirements.txt' para o diretório de trabalho no container. 
# Esse arquivo contém as dependências do projeto que serão instaladas.
COPY ./requirements.txt /appFastAPI/requirements.txt

# Instalar as dependências listadas no 'requirements.txt' usando pip.
# A flag '--no-cache-dir' evita o cache das dependências, garantindo uma instalação mais leve.
RUN pip install --no-cache-dir -r requirements.txt

# Criar as pastas 'models' e 'preprocessing' dentro do diretório de trabalho '/appFastAPI', caso não existam.
RUN mkdir -p /appFastAPI/models /appFastAPI/preprocessing

# Copiar todo o código da aplicação para o diretório de trabalho no container.
# Isso inclui o código Python e quaisquer outros arquivos necessários para a aplicação funcionar.
COPY . .

# Copiar o modelo 'credit_risk_model.pkl' do diretório 'models' da máquina local para o diretório '/appFastAPI/models' dentro do container.
COPY models/credit_risk_model.pkl /appFastAPI/models/credit_risk_model.pkl

# Copiar o arquivo do scaler 'scaler.pkl' do diretório 'preprocessing' da máquina local para o diretório '/appFastAPI/preprocessing' dentro do container.
COPY preprocessing/scaler.pkl /appFastAPI/preprocessing/scaler.pkl

# Expor a porta 80 do container para que a aplicação possa ser acessada fora do container (no host).
EXPOSE 80

# Comando para rodar a aplicação FastAPI usando o 'gunicorn' com o worker 'uvicorn'. 
# '-w 4' indica que 4 workers serão usados para processar requisições simultâneas.
# '--bind' define o endereço em que o servidor escutará (0.0.0.0:80) e 'appFastAPI.main:app' indica onde o app FastAPI está localizado.
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80", "appFastAPI.main:app"]

## Summary:
# Define a imagem base (Python 3.13 slim).
# Configura o diretório de trabalho dentro do container.
# Instala as dependências do requirements.txt.
# Cria as pastas necessárias (models e preprocessing).
# Copia o código da aplicação e os arquivos necessários (modelos e scaler).
# Expondo a porta 80 para acesso externo.
# Inicia a aplicação FastAPI com gunicorn usando uvicorn como worker.