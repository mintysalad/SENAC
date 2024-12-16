from flask import Flask, render_template

app = Flask(__name__)
# route -> meowmeow.com/
# função -> o que vc quer exibir naquela página
# template

@app.route("/")
def homepage():
    return "Esse é meu primeiro site :D (Salad)"

@app.route("/contatos")
def contatos():
    return "<p>Contatos do Site: </p>Email: meowmeow@gmail.com <br>Fone: (051)989708786"

# colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

