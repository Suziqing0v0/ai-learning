# Day 79 · numpy 手写两层网络：XOR 实验
import os
import numpy as np

X = np.array([[0.,0.], [0.,1.], [1.,0.], [1.,1.]])
y = np.array([[0.], [1.], [1.], [0.]])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0,z)

def forward(X,W1,b1,W2,b2):
    z1 = X @ W1 + b1
    h = relu(z1)
    z2 = h @ W2 + b2
    out = sigmoid(z2)
    return z1,h,out

def loss(X,y,W1,b1,W2,b2):
    z1,h,out = forward(X,W1,b1,W2,b2)
    return ((out - y)**2).mean() 

n = 4

def train(hidden, lr=0.5, epochs=3000, seed=0):
    rng = np.random.default_rng(seed)
    W1 = rng.normal(size=(2, hidden)) 
    b1 = np.zeros(hidden)
    W2 = rng.normal(size=(hidden, 1))  
    b2 = np.zeros(1)

    for i in range(epochs):
        z1,h,out = forward(X,W1,b1,W2,b2)
        d_out = ((out - y)*2) / n
        d_z2 = d_out*out*(1 - out)
        dW2 = h.T @ d_z2
        db2 = d_z2.sum(axis=0)
        d_h = d_z2 @ W2.T
        d_z1 = d_h * (z1 > 0)
        dW1 = X.T @ d_z1
        db1 = d_z1.sum(axis=0)
        W2 -= lr * dW2
        W1 -= lr * dW1
        b2 -= lr * db2
        b1 -= lr * db1

    z1,h,out = forward(X,W1,b1,W2,b2)
    loss = ((out - y) ** 2).mean()
    acc  = ((out > 0.5) == (y > 0.5)).mean()
    return loss, acc, out.ravel()

for hidden in (1,4):
    loss, acc, out = train(hidden)
    print(f"hidden {hidden}: loss={loss:.4f} acc={acc:.2f} out={np.round(out,3)}")