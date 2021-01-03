# %%
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
%config InlineBackend.figure_format = 'retina'

# %%
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

# %%
df = pd.read_csv("fifa21_male2.csv")

# %%
df.head(5)

# %% delete columns with just links
df.drop(columns=['player photo', 'club logo', 'flag photo'], inplace = True)


# %%
df.dtypes

# %%
df.isna().sum()

# %% # lowercase column headers
df.columns = [x.lower() for x in df.columns]

# %% highest and lowest rated player 
df.sort_values(by="ova")

# %% highest difference between ova and potential 

# %% age and ova correlation

# %% median weight for each position 

# %% nationality of best player for each position 

# %% average score for each position 
