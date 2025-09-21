import pandas as pd
import matplotlib.pyplot as plt



import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 2. Define Functions
def predict(X, w0, w1):
    return w0 + w1 * X

def compute_cost(X, y, w0, w1):
    m = len(y)
    predictions = predict(X, w0, w1)
    return (1/(2*m)) * np.sum((predictions - y)**2)

def gradient_descent(X, y, w0, w1, learning_rate, iterations):
    m = len(y)
    cost_history = []
    for i in range(iterations):
        predictions = predict(X, w0, w1)
        grad_w0 = (1/m) * np.sum(predictions - y)
        grad_w1 = (1/m) * np.sum((predictions - y) * X)
        w0 -= learning_rate * grad_w0
        w1 -= learning_rate * grad_w1
        cost_history.append(compute_cost(X, y, w0, w1))
    return w0, w1, cost_history

# 3. Train Model
w0, w1, history = gradient_descent(X, y, 0, 0, 0.1, 1000)
print(f"w0: {w0}, w1: {w1}")

# 4. Plot Results
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(history)
plt.xlabel('Iterations'); plt.ylabel('Cost')
plt.subplot(1,2,2)
plt.scatter(X, y)
plt.plot(X, predict(X, w0, w1), color='red')
plt.xlabel('X'); plt.ylabel('y')
plt.tight_layout()
plt.show()