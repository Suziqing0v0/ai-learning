# Day 85 · 卷积：保留空间结构
from torchvision import datasets, transforms

tf = transforms.ToTensor()
train = datasets.MNIST(r"D:\ai-learning\data", train=True,
                       download=False, transform=tf)
img, label = train[0]
print(img.shape, label)

import torch.nn as nn

conv = nn.Conv2d(1,8,3)

print("权重", conv.weight.shape)
print("偏置", conv.bias.shape)

out = conv(img.unsqueeze(0))
print(out.shape)

mlp_first = 784 * 128 + 128
print(mlp_first)