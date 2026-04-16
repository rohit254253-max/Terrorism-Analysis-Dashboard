import pandas as pd

def load_data():
    df = pd.read_csv("data/data.csv", encoding='latin1')
    df = df[['iyear','imonth','iday','country_txt','region_txt',
             'attacktype1_txt','latitude','longitude']]
    df = df.dropna()
    return df