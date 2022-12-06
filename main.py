from fastapi import FastAPI

from pydantic import BaseModel

import pandas as pd

app = FastAPI()

# rota raiz 

@app.get("/")
def raiz():
    return {"Ola": "Mundo"}

# Criar base

database = pd.read_csv("train.csv")

# rota get

@app.get("/Passageiro")
def get_passageiro():
    return df.Name



# rota get por ID

@app.get("/Passageiro/{id_passageiro}")
def get_id_passageiro(id_passageiro: str):
    try:
        banana =  database.query('PassengerId == {}'.format(id_passageiro))
        if banana is not None: 
            return {"Status": 200, "Mensagem": (banana.Name)}
        else:
            return {"Status": 404, "Mensagem": "Nao encontrou passageiro"}
    except Exception as erro:
        return {"Status": 404, "Mensagem": str(erro)}
