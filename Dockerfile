# Base da imagem
FROM python:3.13-slim

# Configurar diretório de trabalho
WORKDIR /app

# Copiar todos os arquivos do projeto
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta padrão do FastAPI
EXPOSE 8000

# Rodar o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]