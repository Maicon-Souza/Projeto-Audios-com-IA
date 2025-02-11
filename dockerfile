# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de dependências e o código-fonte
COPY requirements.txt .
COPY . .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o Whisper e suas dependências
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install --no-cache-dir openai-whisper

# Definir a porta que o Flask vai usar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]