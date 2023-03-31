import numpy as np

x = np.array([2, 1, 1])
b1 = np.array([[1, 2, 0]])
b2 = np.array([[1, 1, 0]])

B = np.concatenate((b1, b2), axis=0).T
BTB = B.T @ B
BTx = B.T @ x
lambda1 = (np.linalg.inv(BTB) @ BTx)
print(f"Lambda = {lambda1}")
MuX = np.dot(B, lambda1)
print(f"MuX = {MuX}")
