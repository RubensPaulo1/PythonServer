from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Configuração do diretório de arquivos estáticos
STATIC_DIR = 'static'
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

@app.route('/')
def home():
    return send_from_directory(STATIC_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(STATIC_DIR, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 