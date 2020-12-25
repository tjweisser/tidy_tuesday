#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
df = pd.read_csv(
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-26/cocktails.csv"
)

# %%
df.info()
df.head()

# %%
df["category"].unique()
# %%
