def pandas_decorator(fx):

    def mainfunc(*args):
        response = fx(*args)
        response.to_parquet(r"C:\Users\satya\Documents\Projects\PythonAdvanced\CH-3-Polymorphism&Decorators\temp.parquet")
        return response
    return mainfunc

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

response = csv_to_parquet(r"C:\Users\satya\Documents\Projects\PythonAdvanced\CH-3-Polymorphism&Decorators\\data.csv")
print(response.head())