import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_multi = pd.read_csv('./data/1d-multi-method-data.csv')

# set methods for plotting
methods = df_multi['method'].unique()