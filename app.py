from flask import Flask
import pandas as pd

# -*- coding: utf-8 -*-
app = Flask(__name__)  # cria o site
tabela = pd.read_excel("Colaboradores demitidos.xlsx")

@app.route("/")
def num_registros():
  tabela_desligados = tabela[["Nome", "Número_de_registro"
                              ]]
  dic_desligados = tabela_desligados.to_dict()
  return dic_desligados

if __name__ == "__main__":
    app.run(debug = True)
    