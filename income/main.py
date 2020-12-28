# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
data = pd.read_csv(
    "data.csv",
    sep=";",
    usecols=["year", "gender", "agebracket", "medianinc", "atrisk_per"],
)
# %%
data.dtypes
# %%
data.info()
# %%
data.head()
# %%
data["agebracket"].isnull().sum()
# %%
data["agebracket"] = data["agebracket"].str.replace(" to under ", "-")
data["agebracket"] = data["agebracket"].str.replace(" years", "")
data["agebracket"]

# %%
plt.plot(data=data, x="agebracket", y="medianinc")

# %%
