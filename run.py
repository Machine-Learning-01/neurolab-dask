import dask.dataframe as dd

def read_dask_data():
    try:
        col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

        df = dd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',names=col_names)

        return df.head()
        
    except Exception as e:
        raise e 
    
