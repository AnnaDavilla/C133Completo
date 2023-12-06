# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Alex" # escreva seu nome
    idade = "12" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai():

    nome = "pai" # escreva seu nome
    idade = "50" # escreva sua idade

    return render_template('pai.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/mãe")
def mãe():

    nome = "mãe" # escreva seu nome
    idade = "30" # escreva sua idade

    return render_template('mae.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.route("/amigo")
def amigo():

    nome = "amigo" # escreva seu nome
    idade = "10" # escreva sua idade

    return render_template('amigo.html' , nome = nome , idade = idade)


# defina a rota para anna
@app.route("/anna")
def anna():

    nome = "anna" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('anna.html' , nome = nome , idade = idade)
# defina a rota para Amigas da anna
@app.route("/amigas")
def amigas():

    nome = "Isabela,Maria julia,Maria Eduarda" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('amigas.html' , nome = nome , idade = idade)
# defina a rota para Irmao da Anna
@app.route("/miguel")
def miguel():

    nome = "Miguel" # escreva seu nome
    idade = "2" # escreva sua idade

    return render_template('miguel.html' , nome = nome , idade = idade)

# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
