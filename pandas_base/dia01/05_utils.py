# %%
import pandas as pd

df = pd.read_csv("ufs.csv", sep=";")
df

# %%
df.head(2)

# %%
df.tail(3)

# %%
df.sample(4)

# %%
df.info(memory_usage='deep')

# %%

df.dtypes