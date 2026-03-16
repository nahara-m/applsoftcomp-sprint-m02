import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_multi = pd.read_csv('./data/1d-multi-method-data.csv')

# set methods for plotting
methods = df_multi['method'].unique()

fig, ax = plt.subplots(figsize=(10, 5))

# asked Claude and chatGPT how to highlight a specific color for the Proposed method in a swarm plot
# Claude's suggestion seemed better and simpler instead of ChatGPT's solution using just a custom color pallete
# by filtering the df, Proposed can be plotted on the left side to it's easier to read

sns.swarmplot(data=df_multi[df_multi['method'] == 'Proposed'],
              x='method', y='AUCROC',
              #order=methods,
              color='blue', ax=ax)

sns.swarmplot(data=df_multi[df_multi['method'] != 'Proposed'], x='method', y='AUCROC',
              order=methods,
              color='gray', ax=ax)

plt.title('1D Multi Method Data: Highlight Proposed Method')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("./figs/fig-1d-multi-method.png")