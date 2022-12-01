from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__) 
#esse name faz uma referência ao próprio arquivo, garantindo que isso vai fazer rodar a aplicação.

class Jogo:
    def __init__(self,nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo("Skyrim", "RPG", "PC")
jogo2 = Jogo("Fallout new vegas", "RPG", "PC")
jogo3 =Jogo("The Witcher 3", "RPG", "PC")
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template("novo.html", titulo="cadastrar novo jogo")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run(debug = True)