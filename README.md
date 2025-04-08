# Servidor Web Python

Um servidor web simples criado com Python e Flask para hospedar sites estáticos.

## Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Coloque seus arquivos HTML, CSS, JavaScript e outros recursos na pasta `static/`
2. Execute o servidor:
```bash
python app.py
```
3. Acesse o site em seu navegador: `http://localhost:5000`

## Estrutura de arquivos

- `app.py`: Arquivo principal do servidor
- `requirements.txt`: Lista de dependências
- `static/`: Pasta onde devem ser colocados os arquivos do site
  - `index.html`: Página inicial do site

## Personalização

Para adicionar novas páginas, basta criar novos arquivos HTML na pasta `static/` e acessá-los através da URL correspondente. 