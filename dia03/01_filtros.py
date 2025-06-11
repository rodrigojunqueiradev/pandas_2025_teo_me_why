# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%
filtro = df[(df["qtdePontos"]>= 50) & (df["qtdePontos"]<100)] 
filtro

# %%
filtro = df[(df["qtdePontos"] == 1) | (df["qtdePontos"] == 100)] 
filtro
# %%
