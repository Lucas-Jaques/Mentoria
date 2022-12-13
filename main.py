from fastapi import FastAPI

from pydantic import BaseModel

import pandas as pd

from passageiro import Passenger

app = FastAPI()

# rota raiz 

@app.get("/")
def raiz():
    return {"Ola": "Mundo"}

# Criar base

database = pd.read_csv("train.csv")



# rota get

"""@app.get("/passageiro")
def get_passageiro():
    return df.Name"""



# rota get por ID

@app.get("/passageiro/{id_passageiro}")
def get_id_passageiro(id_passageiro: str):
        ##print(id_passageiro)
    row =  database.loc[database['PassengerId'] == (id_passageiro)].head(1)
    print(row)
    if row is not None: 
        passageiro = Passenger()
        passageiro.id = row['PassengerId']
        survived = int(row['Survived'])
        if survived == 0 : 
            passageiro.survived = False
        else:
            passageiro.survived = True
        passageiro.boarding_class = row['Pclass']
        passageiro.name = row['Name']
        passageiro.sex = row['Sex']
        passageiro.age = row['Age']
        passageiro.brother_spouse_quantity = row['SibSp']
        passageiro.parent_children_quantity = row['Parch']
        passageiro.ticket_number = row['Ticket']
        passageiro.fare = row['Fare']
        passageiro.cabin = row['Cabin']
        passageiro.embarked = row['Embarked']

        return passageiro
    else:
        return {"Status": 404, "Mensagem": "Nao encontrou passageiro"}
   
