'''
** Transposition **

An example of creating row vectors from a list, and converting 
one of the row vectors into a column vector through transposition.

'''

import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

a = np.array([a])
b = np.array([b]).T

print(np.dot(a, b))