import dask.dataframe as dd

col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

df = dd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',names=col_names)

print(df.head())
        