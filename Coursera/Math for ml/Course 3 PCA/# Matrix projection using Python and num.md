# Matrix projection using Python and numpy

This is a Python script that demonstrates matrix projection using numpy. To run this script, you must have Python and numpy installed on your computer.

```python
import numpy as np

# Number 1
print("Number 1")
x = np.array([6, 0, 0])
# reshape is just to make it a column vector
b1 = np.array([1, 1, 1]).reshape((-1, 1))
b2 = np.array([0, 1, 2]).reshape((-1, 1))
B = np.concatenate((b1, b2), axis=1)

projection_matrix = B @ np.linalg.inv(B.T @ B) @ B.T
print(f"Projection Matrix aka MuX: \n{projection_matrix}")

x_to_B = (projection_matrix @ x)
print(f"Projection of x onto U :\n{x_to_B}")

lambda1 = np.linalg.inv(B.T @ B) @ B.T @ x
print(
    f"Lambda aka Coordinate of projected point \nwith resptect to b1,b2 = {lambda1}")

# Number 2
print("\nNumber 2")
x = np.array([3, 2, 2])
b1 = np.array([1, 0, 0]).reshape((-1, 1))
b2 = np.array([0, 1, 1]).reshape((-1, 1))
B = np.concatenate((b1, b2), axis=1)

xtoB_projection = B @ np.linalg.inv(B.T @ B) @ B.T @ x
print(f"Projection of x onto U :\n{xtoB_projection.reshape((-1, 1))}")

# Number 3
print("\nNumber 3")
x = np.array([12, 0, 0])
b1 = np.array([1, 1, 1]).reshape((-1, 1))
b2 = np.array([0, 1, 2]).reshape((-1, 1))
B = np.concatenate((b1, b2), axis=1)

projection1 = B @ np.linalg.inv(B.T @ B) @ B.T @ x

U = np.array([-10, -4, 2]) * np.sqrt(6)  # its a trap

projection1_to_U = U * projection1  # its a trap

print(f"Projection of x onto U :\n{projection1.reshape((-1, 1))}")
```
