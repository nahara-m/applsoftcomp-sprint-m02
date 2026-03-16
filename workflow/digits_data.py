import umap
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# code copied and slightly modified from the lecture notes since it's noted also available from load_digits

# Load digits dataset (8x8 images, 64 dimensions)
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

# Take a subset for speed (t-SNE is slow on large datasets)
np.random.seed(42)
indices = np.random.choice(len(X_digits), size=1000, replace=False)
X_subset = X_digits[indices]
y_subset = y_digits[indices]

# Apply UMAP
umap_model = umap.UMAP(n_components=2, random_state=42, n_neighbors=30)
X_digits_umap = umap_model.fit_transform(X_subset)

fig, ax = plt.subplots(figsize=(7, 6))

# UMAP
scatter = ax.scatter(X_digits_umap[:, 0], X_digits_umap[:, 1],
                          c=y_subset, cmap='tab10', alpha=0.7, s=30)
ax.set_xlabel('UMAP1')
ax.set_ylabel('UMAP2')
ax.set_title('UMAP')
cbar = plt.colorbar(scatter, ax=ax, ticks=range(10))
cbar.set_label('Digit Class')
sns.despine(ax=ax)
plt.tight_layout()
plt.savefig("./figs/fig-digits.png")