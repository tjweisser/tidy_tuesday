# Pandas
### Commands to access dataframe properties
`df.dtypes`
`df.info`
`df.head()`
`df.tail()`
`df.shape()`
`df.sample(5)` # randome sample of 5 observations
`df.describe()`

### Check for missing values 
`df.isna().any()`
`df.isna().sum()`
### Plot missing values per column
`df.isna().sum().plot(kind="bar")`

### Drop and fill NA 
`df.dropna(axis="columns", how="all")` -- drop all columns with 100% NA's
`df.fillna(0)` -- fill NA with 0
`df.drop("column_name", axis="columns", inplace=True)`
### Select rows or columns 
`.iloc` -- integer locate
`.loc`
`df[df["column"]isin(["a","b","c"])]`

### Sort 
`df.sort_values("column_to_sort_by", ascending = False)`
`df.sort_index()`

### Access values 
`df.loc[df["<column>"] == "<value>"]`

### Unique values
`df['column'].nunique()` -- numnber of unique values 
`df['column'].unique()` -- name of unique values 


## Aggregate
### Group the data by the index keys and find thea mean of the total column
`df.groupby(level=0).agg({"total":"mean"})` -- you can read groupby("x") as "for each x" give me ...
`df.value_counts(normalize=True)`

### transform from wide to long
`df.melt(id_vars="column to keep", var_name="groups", value_name="statistic")`

# Data visualisation 

## Matplotlib
optional: for ggplot-like style
```python
mpl.style.use('ggplot')
```
## Artist vs scription layer
There are two styles/options of ploting with matplotlib. Plotting using the Artist layer and plotting using the scripting layer.
* Option 1: Scripting layer (procedural method) - using matplotlib.pyplot as 'plt' *

```    df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10)) 
    plt.title('Immigration trend of top 5 countries')
    plt.ylabel('Number of immigrants')
    plt.xlabel('Years')```

* Option 2: Artist layer (Object oriented method) - using an Axes instance from Matplotlib (preferred) *
  
ax = df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10))
ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')


## Subplots
To visualize multiple plots together, we can create a figure (overall canvas) and divide it into subplots, each containing a plot. With subplots, we usually work with the artist layer instead of the scripting layer. The typical syntax is :
`fig, ax = plt.subplots()`