import pandas as pd

# Create DataFrame objects
df1 = pd.DataFrame({'a': [1]})
df2 = pd.DataFrame({'b': [2]})

# Create a DataFrame alias
df_alias = df1

# Display memory addresses using id()
print("Memory addresses:")
print("df1:", id(df1))
print("df2:", id(df2))
print("df_alias:", id(df_alias))

# Check if df_alias refers to the same object as df1
print("df_alias is df1:", df_alias is df1)

# Check if df2 is a different object than df1
print("df2 is df1:", df2 is df1)

