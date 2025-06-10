# %%
import pandas as pd

# %%
# Importando o DataFrame de um arquivo:
df = pd.read_csv("../data/clientes.csv")
df

# %%
# Salvando um arquivo em csv:
df.to_csv("clientes.csv")

# %%
# Salvando na extensão parquet (binário):
df.to_parquet("clientes.parquet", index=False)

# %%
df.to_excel("clientes.xlsx", index=False)

# %%
