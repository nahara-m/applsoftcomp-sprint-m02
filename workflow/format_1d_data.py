#format 1d dataset for data viz
import pandas as pd
import os

df_1d = pd.read_csv('./data/1d-data.csv')
df_1d = df_1d.round(2)

#save preprocessed data to new csv file
#add new folder preprocessed to data folder and save the formatted data there   
os.makedirs('./data/preprocessed', exist_ok=True)
df_1d.to_csv('./data/preprocessed/1d-data-formatted.csv', index=False)