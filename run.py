import dask.dataframe as dd

df = dd.read_csv('Iris.csv')

print(df.head())
        