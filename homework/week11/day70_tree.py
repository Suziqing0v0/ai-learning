# Day 70 · 决策树：一串是/否问题
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split

folder = os.path.dirname(os.path.abspath(__file__))

rng = np.random.default_rng(42)
n = 100

x1 = np.concatenate([rng.normal(-1,1,n), rng.normal(1,1,n)])
x2 = np.concatenate([rng.normal(-1,1,n), rng.normal(1,1,n)])

X = np.column_stack([x1,x2])
y = np.concatenate([np.zeros(n),np.ones(n)])

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0)
tree = DecisionTreeClassifier(max_depth=3,random_state=0)
tree.fit(X_tr,y_tr)

print(f"训练{tree.score(X_tr,y_tr):.4f} 测试{tree.score(X_te,y_te):.4f}")
print(f"叶子数{tree.get_n_leaves()}")

from sklearn.tree import export_text
print(export_text(tree,feature_names=["x1","x2"]))

plt.figure(figsize=(14,7))
plot_tree(tree,feature_names=["x1","x2"],class_names=["0","1"],filled=True)
plt.tight_layout()
plt.savefig(os.path.join(folder, "tree.png"))