# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv")
df.head()

# %%
# Retorna os ids iguais a 5 ou a 11:
df[(df["idProduto"] == 5) | (df["idProduto"] == 11)]

# %%
# Retorna os ids iguais a 5 ou a 11:
df[df["idProduto"].isin([5,11])]

# %%
clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%
