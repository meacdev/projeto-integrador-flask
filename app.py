from flask import Flask, render_template, request, jsonify
import pandas as pd
import uuid
import os

app = Flask(__name__)
JSON_PATH = "dados.json"

@app.route("/")
def main():

    if os.path.exists(JSON_PATH):
        df = pd.read_json(JSON_PATH)
    else: 
        df = pd.DataFrame()

    pagina = request.args.get("pagina", default=1, type=int)
    registros_por_pagina = 5

    inicio = (pagina - 1) * registros_por_pagina
    fim = inicio + registros_por_pagina
    dados = df.iloc[inicio:fim]

    total_paginas = (len(df) + registros_por_pagina - 1) // registros_por_pagina if len(df) else 1

    return render_template(
        "index.html",
        dados=dados.to_dict(orient="records"),
        pagina=pagina,
        total_paginas=total_paginas
    )

@app.route("/registro", methods=["POST"])
def cadastro():
    
    id = uuid.uuid4().hex
    nome = request.form["nome"]
    cidade = request.form["cidades"]
    salario = request.form["salario"]
    departamento = request.form["departamento"]

    df = pd.DataFrame({
        "id": [id],
        "nome": [nome],
        "cidade": [cidade],
        "salario": [salario],
        "departamento": [departamento]
    })

    if os.path.exists(JSON_PATH):
        antigo = pd.read_json(JSON_PATH)
        novo_df = pd.concat([antigo, df], ignore_index=True)
    else:
        novo_df = df

    novo_df.to_json("dados.json", orient="records", indent=4)

    return f"""
        <p>Cadastro realizado com sucesso!</p>
        <p>Seu id: {id}</p>
    """

@app.route("/registro", methods=["GET"])
def buscar():

    df = pd.read_json(JSON_PATH)

    id_procurado = request.args.get("texto-id", "").strip()

    busca = df[df["id"] == id_procurado]

    if not busca.empty:
        cadastro = busca.iloc[0].to_dict()
        return f"""
            <p>Cadastro encontrado!</p>
            <p>{cadastro}</p>
        """
    else:
        return f"""
            <p>Cadastro não encontrado!</p>
        """


if __name__ == "__main__":
    app.run(debug=True)