# no formatting needed for this one, so just loading the data for the  2d-data-format branch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_2d = pd.read_csv("./data/2d-data.csv")

# copied + slightly modified from lecture notes (2D Data Visualization)
fig, ax = plt.subplots(figsize=(10, 7))
hb = ax.hexbin(df_2d["x"], df_2d["y"], gridsize=30, cmap='YlOrRd', mincnt=1)
ax.set_xlabel('X Variable')
ax.set_ylabel('Y Variable')
ax.set_title("2D Dataset Visualization using hexbin")
cb = plt.colorbar(hb, ax=ax)
cb.set_label('Measurement')
plt.savefig("./figs/fig-2d-data.png")
sns.despine()
