import umap
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# code copied from the lecture notes since it's noted also available from load_digits

# Load digits dataset (8x8 images, 64 dimensions)
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

# Take a subset for speed (t-SNE is slow on large datasets)
np.random.seed(42)
indices = np.random.choice(len(X_digits), size=1000, replace=False)
X_subset = X_digits[indices]
y_subset = y_digits[indices]