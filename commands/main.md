
# Commands to access dataframe properties
`df.dtypes`
`df.info`
`df.head()`
`df.tail()`
`df.shape()`
`df.sample(5)` # randome sample of 5 observations

# Check for missing values 
`df.isna().any()`
`df.isna().sum()`
### Plot missing values per column
`df.isna().sum().plot(kind="bar")`

### Drop and fill NA 
`df.dropna()`
`df.fillna(0)` -- fill NA with 0
# Select rows or columns 
`.iloc` -- integer locate
`.loc`

# Sort 
`df.sort_values("column_to_sort_by", ascending = False)`
`df.sort_index()`

# Access values 
`df.loc[df["<column>"] == "<value>"]`

# Aggregate
# Group the data by the index keys and find thea mean of the total column
`df.groupby(level=0).agg({"total":"mean"})`
`df.value_counts`
