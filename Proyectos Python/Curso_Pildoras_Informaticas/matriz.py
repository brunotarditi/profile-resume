import numpy as np

matrix = np.arange(1,10).reshape(3, 3)
print(matrix)
for elemento in np.nditer(matrix):
    print(elemento, end=' ')
