# %% 
import pandas as pd

# %%
df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes

## AMOSTRAS

# %%
# Visualizando 5 linhas:
df_clientes.head()

# %%
# Visualizar as 10 primeiras linhas:
df_clientes.head(10)

# %%
# Visualizar as últimas linhas:
df_clientes.tail()

# %%
# Ver 5 elementos aleatórios:
df_clientes.sample(5)

# %%
# Verifica as linhas e colunas:
df_clientes.shape

# %%
# Verifica o nome das colunas
df_clientes.columns

# %%
# Verifica o index:
df_clientes.index

# %%
# Exibe informações sobre o df:
df_clientes.info()

# %%
# Exibe a quantidade real de memória utilizada pelo df: 
df_clientes.info(memory_usage='deep')

# %%
# Verifica informações sobre as colunas em formato de séries:
df_clientes.dtypes

# %%
