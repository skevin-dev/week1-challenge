import pandas as pd 

def read_data(filepath):
    df = pd.read_csv(filepath)
    return df  