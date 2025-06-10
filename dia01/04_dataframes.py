# %%
import pandas as pd

idades = [10, 50, 15, 68, 48, 65, 99, 105, 23, 32, 35, 42]
nomes = ["Rodrigo", "Téo", "Tobi", "Lucky", "Bianca", "Fulano", "Ciclano", "João", "Maria", "Fifi", "Frederico", "Alguém"]
series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_idades

# %%
# Criando um DataFrame:
df = pd.DataFrame()

# Colocando séries no DataFrame:
df["idades"] = series_idades
df["nomes"] = series_nomes
df

# %%
type(df)

# %%
# Acessar uma coluna específica:
df["nomes"]

# %%
# Acessar uma linha específica:
df.iloc[0]

# %%
# Acessar o primeiro nome da primeira linha
df.iloc[0]["nomes"]

# %%
# Acessar a idade da última pessoa
df.iloc[-1]["idades"]

# %%
