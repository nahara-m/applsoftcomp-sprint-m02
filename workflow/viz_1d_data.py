#data viz for 1d dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter


#load preprocessed 1d dataset
df_1d = pd.read_csv('./data/preprocessed/1d-data-formatted.csv')


# plot 1d data
# asked chatGPT how to keep the decimals in labels
sns.swarmplot(data=df_1d, x='group', y='value').yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

plt.title('Swarm Plot of 1D Data')
plt.savefig('./figs/fig-1d-data.png')
#plt.show()