# 1 Começamos com uma imagem leve do python
FROM python:3.9-slim

# 2 Definimos onde o código vai morar dentro do container
WORKDIR /app

# 3 Copiamos o arquivo de requisitos e instalamos
COPY requirements.txt .
RUN  pip install --no-cache-dir -r requirements.txt

# 4 Copiamos o resto do código
COPY . .

# 5 Expomos a porta que a aplicação usa
EXPOSE 8080

# 6 Comando para ligar a aplicação
CMD ["python", "app.py" ]
