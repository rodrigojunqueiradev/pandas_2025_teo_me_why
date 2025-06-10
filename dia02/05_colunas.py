# %% 
import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv")
df

# %%
df.shape

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%
# Renomenado colunas:
df.rename(columns={"qtdePontos": "qtPontos"})

# %%
df = df.rename(columns={"qtdePontos": "qtPontos"})
df

# %%
# Exibe em formato de série uma coluna:
df["idCliente"]

# %%
# Exibe duas colunas em formato de lista:
df[["idCliente", "qtPontos"]]

# %%
# Comparação com SQL:

# SELECT * FROM df
df

# %%
# SELECT idCliente FROM df
df[['idCliente']]

# %%
# SELECT idCliente, qtPontos FROM df LIMIT 5
df[['idCliente', 'qtPontos']].sample(5)

# %%
# Reordenar as colunas do df:
colunas = df.columns.tolist()
colunas.sort()
colunas
df = df[colunas]
df

# %%
