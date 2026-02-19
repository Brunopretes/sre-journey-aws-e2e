from flask import Flask
import os
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # Simula uma falha aleatória de 20% para testarmos resiliência depois
    if random.random() < 0.2:
        return "Erro Interno do Servidor", 500
    return "Olá SRE! Aplicação rodando com sucesso no Docker."

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)