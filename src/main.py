from flask import Flask, render_template, request
from datetime import datetime
from tinydb import TinyDB

app = Flask(__name__)

pong = TinyDB("pong.json")
echo = TinyDB("echo.json")
db = TinyDB("logs.json")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['GET'])
def ping():
    return pong

@app.route('/echo', methods=['POST'])
def echo():
    if request.method == 'POST':
        dados = request.form.get('dados')
        texto = request.form.get('texto')

        echo.insert({"resposta": dados}, {"resposta" : texto})

        return f'<h1>dados: {dados}, texto: {texto}</h1>'

@app.route('/dash')
def dash():
    db.insert({
    "endereco":request.environ['REMOTE_ADDR'],
    "metodo": request.method,
    "hora":datetime.now()
    })
    return render_template('dash.html')

@app.route('/info')
def info():
    return render_template('info.html', itens=db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)