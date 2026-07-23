import json
import pandas as pd
import random
import uuid

random.seed(20)

with open("nomes.txt", "r", encoding="utf-8") as f:
    nomes = f.read().splitlines()

with open("static/municipios.json", "r", encoding="utf-8") as f:
    municipios = json.load(f)

salario = ["classe-e", "classe-d", "classe-c", "classe-b", "classe-a"]

departamentos = [
    "Recursos Humanos",
    "Marketing",
    "Tecnologia da Informação",
    "Financeiro",
    "Contabilidade",
    "Jurídico",
    "Comercial / Vendas",
    "Atendimento ao Cliente",
    "Logística",
    "Compras / Suprimentos",
    "Produção / Operações",
    "Qualidade",
    "Pesquisa e Desenvolvimento",
    "Engenharia",
    "Administrativo",
    "Auditoria Interna",
    "Comunicação Corporativa",
    "Relações Públicas",
    "Segurança do Trabalho",
    "Facilities"
]

registros = []
for i in range(0, 5000):
    estado = random.choice(list(municipios.keys()))
    registros.append({
        "id": uuid.uuid4().hex,
        "nome": random.choice(nomes),
        "idade": random.randint(18, 65),
        "cidade": random.choice(municipios[estado]),
        "salario": random.choice(salario),
        "departamento": random.choice(departamentos)
    })

df = pd.DataFrame(registros)
df.to_json("dados.json", orient="records", indent=4)
print(df.head())
