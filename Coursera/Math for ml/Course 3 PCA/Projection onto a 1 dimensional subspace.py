import numpy as np

# * Number 1

b = np.array([1, 2, 2])
# * To get the projection matrix
projection_matrix = np.outer(b, b) / np.dot(b, b)
print(f"Number 1 :\n{projection_matrix}")


# * Number 2
x = np.array([[9, 0, 12],
              [0, 0, 0],
              [12, 0, 16]])/25
b = np.array([1, 1, 1])
result = (np.dot(x, b) * 25)  # ! to get the projection of x onto b
print(f"Number 2 : 1/25 * {result}")

# * Number 3
x = np.array([5, 10, 10])/9
b = np.array([1, 1, 1])
result = np.linalg.norm(x-b)  # ! To get the distance between x and b
result = np.round(result, 2)
print(f"Number 3 : {result}")
