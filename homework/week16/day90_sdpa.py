# Day 90 · 用 PyTorch 实现 scaled dot-product attention
import torch
import torch.nn.functional as F
import numpy as np

X = torch.tensor([[1., 0.],
                  [0., 1.],
                  [1., 1.]], dtype=torch.float32)

Wq = torch.tensor([[1., 0.5],
                   [0., 1.]], dtype=torch.float32)

Wk = torch.tensor([[1., 0.],
                   [0.5, 1.]], dtype=torch.float32)

Wv = torch.tensor([[1., 2.],
                   [3., 1.]], dtype=torch.float32)

Q = X @ Wq
K = X @ Wk
V = X @ Wv

scores = Q @ K.T
scaled = scores / (K.shape[1] ** 0.5)
weights = torch.softmax(scaled, dim=1)
out_manual = weights @ V

out_builtin = F.scaled_dot_product_attention(Q, K, V)

print(weights)
print(weights.sum(dim=1))
print(out_manual)
print(out_builtin)

max_diff = (out_builtin - out_manual).abs().max()
print(max_diff)
print(out_builtin.shape)