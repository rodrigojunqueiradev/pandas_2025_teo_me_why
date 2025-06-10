# %%

import pandas as pd

idades = [10, 50, 15, 68, 48, 65, 99, 105, 23, 32, 35, 42]

series_idades = pd.Series(idades)
series_idades

# %%
# Primeiro elemento da lista:
idades[0]

# %%
#Último elemento da lista:
idades[-1]

# %%
series_idades

# %%
# Primeiro elemento da série:
series_idades[0]

# %%
#Último elemento da séries:
series_idades[11]

# %%
# Ordenando a série de forma crescente
series_idades = series_idades.sort_values()
series_idades

# %%
# Pega o item na posição 1 (não é na chave 1)
series_idades.iloc[1]

# %%
# Pegando os 3 primeiros elementos da série:
series_idades.iloc[:3]

# %%
# Pegando do último para o primeiro:
series_idades.iloc[::-1]

# %%

indexs = ["Rodrigo", "Téo", "Tobi", "Lucky", "Bianca", "Fulano", "Ciclano", "João", "Maria", "Fifi", "Frederico", "Alguém"]
series_idades = pd.Series(idades, index=indexs)
series_idades
# %%
