from flask import Flask, render_template, request, jsonify
import pandas as pd
import uuid
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/cadastro", methods=["POST"])
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

    if os.path.exists("dados.json"):
        antigo = pd.read_json("dados.json")
        novo_df = pd.concat([antigo, df], ignore_index=True)
    else:
        novo_df = df

    novo_df.to_json("dados.json", orient="records", indent=4)

    return f"""
        <p>Cadastro realizado com sucesso!</p>
        <p>Seu id: {id}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)