#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# load description
# %%
schema = pd.read_csv("data/schema.csv", index_col=0, names=["variable", "description"])

# load main data
# %%
london = pd.read_csv(
    "data/london.csv",
    usecols=["YEAR", "MO", "DY", "T2M", "WS10M", "PRECTOT"],
    parse_dates={"date": ["YEAR", "MO", "DY"]},
)

hamburg = pd.read_csv(
    "data/hamburg.csv",
    usecols=["YEAR", "MO", "DY", "T2M", "WS10M", "PRECTOT"],
    parse_dates={"date": ["YEAR", "MO", "DY"]},
)

paris = pd.read_csv(
    "data/paris.csv",
    usecols=["YEAR", "MO", "DY", "T2M", "WS10M", "PRECTOT"],
    parse_dates={"date": ["YEAR", "MO", "DY"]},
)

# make column' names lowercase
# %%
london.columns = [x.lower() for x in london.columns]
hamburg.columns = [x.lower() for x in london.columns]
paris.columns = [x.lower() for x in london.columns]

# add name LON
# %%
london["place"] = "lON"

# get info
# %%
london.info()

# get first 5 rows
# %%
london.head()

# %%
london["date"] = pd.to_datetime(london["date"], format="%Y-%m-%d")
london.set_index("date", inplace=True)
london

hamburg["date"] = pd.to_datetime(hamburg["date"], format="%Y-%m-%d")
hamburg.set_index("date", inplace=True)
hamburg

paris["date"] = pd.to_datetime(paris["date"], format="%Y-%m-%d")
paris.set_index("date", inplace=True)
paris

# %% aggregate data for each month
lnd_grouped = (
    london.groupby(
        [(london.index.month.rename("month")), (london.index.day.rename("day"))]
    )
    .mean()
    .reset_index()
)
lnd_grouped.head()

ham_grouped = (
    hamburg.groupby(
        [(hamburg.index.month.rename("month")), (hamburg.index.day.rename("day"))]
    )
    .mean()
    .reset_index()
)
ham_grouped.head()

par_grouped = (
    paris.groupby(
        [(paris.index.month.rename("month")), (paris.index.day.rename("day"))]
    )
    .mean()
    .reset_index()
)
par_grouped.head()

# %% create date column
lnd_grouped["date"] = (
    lnd_grouped["month"].astype(str) + "-" + lnd_grouped["day"].astype(str)
)
lnd_grouped

ham_grouped["date"] = (
    ham_grouped["month"].astype(str) + "-" + ham_grouped["day"].astype(str)
)
ham_grouped

par_grouped["date"] = (
    par_grouped["month"].astype(str) + "-" + par_grouped["day"].astype(str)
)
par_grouped


# %% delete unused columns
lnd_grouped.drop(columns=["month", "day"], inplace=True)
lnd_grouped

ham_grouped.drop(columns=["month", "day"], inplace=True)
ham_grouped

par_grouped.drop(columns=["month", "day"], inplace=True)
par_grouped

# %% exponential moving average
lnd_grouped["prectot_ema"] = lnd_grouped["prectot"].ewm(alpha=0.1, adjust=False).mean()
lnd_grouped["t2m_ema"] = lnd_grouped["t2m"].ewm(alpha=0.1, adjust=False).mean()
lnd_grouped["ws10m_ema"] = lnd_grouped["ws10m"].ewm(alpha=0.1, adjust=False).mean()
lnd_grouped

ham_grouped["prectot_ema"] = ham_grouped["prectot"].ewm(alpha=0.1, adjust=False).mean()
ham_grouped["t2m_ema"] = ham_grouped["t2m"].ewm(alpha=0.1, adjust=False).mean()
ham_grouped["ws10m_ema"] = ham_grouped["ws10m"].ewm(alpha=0.1, adjust=False).mean()
ham_grouped

par_grouped["prectot_ema"] = par_grouped["prectot"].ewm(alpha=0.1, adjust=False).mean()
par_grouped["t2m_ema"] = par_grouped["t2m"].ewm(alpha=0.1, adjust=False).mean()
par_grouped["ws10m_ema"] = par_grouped["ws10m"].ewm(alpha=0.1, adjust=False).mean()
par_grouped


# %% plot temperature

lnd_grouped["t2m_ema"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)
ham_grouped["t2m_ema"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)
par_grouped["t2m_ema"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)

# modify ticks size
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(labels=["london", "Hamburg", "Paris"], fontsize=14)

# title and labels
plt.title("Yearly average air temperature (1982-2020)", fontsize=20)
plt.xlabel("Day", fontsize=16)
plt.ylabel("Temperature [°C]", fontsize=16)


# %% plot rainfall

lnd_grouped["prectot_ema"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)
ham_grouped["prectot_ema"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)
par_grouped["prectot_ema"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)

# modify ticks size
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(labels=["london", "Hamburg", "Paris"], fontsize=14)

# title and labels
plt.title("Yearly average rainfall (1982-2020)", fontsize=20)
plt.xlabel("Day", fontsize=16)
plt.ylabel("Rainfall [mm]", fontsize=16)

# %%
lnd_grouped["sma_10"] = lnd_grouped["prectot"].rolling(30, min_periods=1).mean()
ham_grouped["sma_10"] = ham_grouped["prectot"].rolling(30, min_periods=1).mean()
par_grouped["sma_10"] = par_grouped["prectot"].rolling(30, min_periods=1).mean()

# %% plot rainfall

lnd_grouped["sma_10"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)
ham_grouped["sma_10"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)
par_grouped["sma_10"].plot(linewidth=3, figsize=(12, 6), alpha=0.8)

# modify ticks size
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(labels=["london", "Hamburg", "Paris"], fontsize=14)

# title and labels
plt.title("Yearly average rainfall (1982-2020)", fontsize=20)
plt.xlabel("Day", fontsize=16)
plt.ylabel("Rainfall [mm]", fontsize=16)

# %%
