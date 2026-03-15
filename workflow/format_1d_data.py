#format 1d dataset for data viz
import pandas as pd

df_1d = pd.read_csv('./data/1d-data.csv')
df_1d = df_1d.round(2)

#save preprocessed data to new csv file
df_1d.to_csv('./data/preprocessed/1d-data-formatted.csv', index=False)