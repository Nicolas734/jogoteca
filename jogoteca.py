from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__) 
app.secret_key = 'lira'
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
    if 'usuario_logado' not in  session or session['usuario_logado'] == None:
        flash('Acesso não permitido...')
        return redirect("/login?proxima=novo")
    else:
        print(session['usuario_logado'])
        return render_template("novo.html", titulo="cadastrar novo jogo", titulo_pagina="Cadastro de jogos")


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect("/")


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo="Login de Usuario", titulo_pagina="Login", proxima=proxima)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    username = request.form['usuario']
    senha = request.form['senha']
    if 'alohomora' == senha:
        session['usuario_logado'] = username
        proxima_pagina = request.form['proxima']
        flash(username + ' logado com sucesso...')
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuario ou senha incorretos...')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso...')
    return redirect('/')


app.run(debug = True)