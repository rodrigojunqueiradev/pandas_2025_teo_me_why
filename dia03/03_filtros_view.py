# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0

# %%
clientes_0["flag_1"] = 1

# %%
