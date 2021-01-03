
# Commands to access dataframe properties
`df.dtypes`
`df.info`
`df.head()`
`df.tail()`
`df.shape()`
`df.sample(5)` # randome sample of 5 observations
`df.describe()`

# Check for missing values 
`df.isna().any()`
`df.isna().sum()`
### Plot missing values per column
`df.isna().sum().plot(kind="bar")`

### Drop and fill NA 
`df.dropna(axis="columns", how="all")` -- drop all columns with 100% NA's
`df.fillna(0)` -- fill NA with 0
`df.drop("column_name", axis="columns", inplace=True)`
# Select rows or columns 
`.iloc` -- integer locate
`.loc`
`df[df["column"]isin(["a","b","c"])]`

# Sort 
`df.sort_values("column_to_sort_by", ascending = False)`
`df.sort_index()`

# Access values 
`df.loc[df["<column>"] == "<value>"]`

# Unique values
`df['column'].nunique()` -- numnber of unique values 
`df['column'].unique()` -- name of unique values 


# Aggregate
# Group the data by the index keys and find thea mean of the total column
`df.groupby(level=0).agg({"total":"mean"})` -- you can read groupby("x") as "for each x" give me ...
`df.value_counts(normalize=True)`

# transform from wide to long
`df.melt(id_vars="column to keep", var_name="groups", value_name="statistic")`