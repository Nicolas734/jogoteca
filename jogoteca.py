from flask import Flask, render_template, request, redirect

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
    return render_template('lista.html', titulo='Jogos', jogos=lista, titulo_pagina="Jogoteca")


@app.route('/novo')
def novo():
    return render_template("novo.html", titulo="cadastrar novo jogo", titulo_pagina="Cadastro de jogos")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect("/")


app.run(debug = True)