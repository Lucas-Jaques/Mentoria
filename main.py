##Importando bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

##Importanto e lendo arquivo CSV
lucas = pd.read_csv("train.csv")


##Transformando arquivo em DataFrame
df = pd.DataFrame(lucas)

##Exibindo o DataFrame por completo
##print(df.to_string())

##Exibindo type de dados do DataFrame

print(df.dtypes)

##Criando colunas condicionais para classificar qual status de cada passageiro
df.loc[df["Survived"] == 0, "Status"] = "Death"
df.loc[df["Survived"] == 1, "Status"] = "Alive"

##Exibindo o DataFrame com a nova classificação
print(df.to_string())

##Contando a ocorrencia de cada Status
count_status = df['Status'].value_counts()

##Exibindo a contagem
print(count_status)

##Protando Gráfico
count_status.plot(kind='barh', color = ['red','blue'])

plt.show()

## Histograma com todos os passageiros

df.hist(column='Age', bins=10, color = 'yellow')
plt.show()


## Filtrar somente passageiros que sobreviveram + Histograma

Alive = df.query('Status == "Alive"')

Alive.hist(column='Age', bins=10, color = 'blue')
plt.show()

## Filtrar somente passageiros que não sobreviveram + Histograma

Death = df.query('Status == "Death"')

Death.hist(column='Age', bins=10, color = 'red')
plt.show()

