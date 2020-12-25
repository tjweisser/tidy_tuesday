#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("survey_results_public.csv", index_col="Respondent")
df.columns = [x.lower() for x in df.columns]
df.head()
df.info()

# %%
data = df.loc[:, "ethnicity"]

plt.plot(data)
# %%


# %%
