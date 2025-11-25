from flask import Flask, render_template
from asasintegracao import gerar_link_pagamento

app = Flask(__name__)

@app.route("/")
def homepage():
    link = "https://sandbox.asaas.com/c/6dgymrzuu4aa265o"
    #link = gerar_link_pagamento()
    return render_template("baby.html", link_pagamento=link)

@app.route("/compracerta")
def compra_certa():
    return render_template("compracerta.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

if __name__ == "__main__":
    app.run()
