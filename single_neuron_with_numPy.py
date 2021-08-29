'''
** Single neuron with NumPy **

An example of a single neuron, using the dot product and the addition 
of the vectors with NumPy

https://nnfs.io/blq

'''

import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [0.2, 0.8, -0.5, 1.0]

bias = 2.0

outputs = np.dot(weights, inputs) + bias

print(outputs)
