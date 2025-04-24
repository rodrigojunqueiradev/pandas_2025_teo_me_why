# %%
# Usando listas para trabalhar com dados em Python:

idades = [10, 50, 15, 68, 48, 65, 99, 105, 23, 32, 35, 42]

media = sum(idades) / len(idades)
print("Média: ", media)

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades) -1)

print("Variância: ", variancia)

# %%
# Usando Pandas

import pandas as pd

idades = [10, 50, 15, 68, 48, 65, 99, 105, 23, 32, 35, 42]

series_idades = pd.Series(idades)
series_idades

#Estatísticas da série:
media_idades = series_idades.mean()
print(media_idades)
variancia_idades = series_idades.var()
print(variancia_idades)
summary_idades = series_idades.describe()
print(summary_idades)

# %%
