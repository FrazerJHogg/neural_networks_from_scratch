'''
** Single neuron **

An example of a single neuron from a neural network. This neuron has 3 
inputs with corresponding weights. 

'''

inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2 

output =  (inputs[0]*weights[0] + 
inputs[1]*weights[1] + 
inputs[2]*weights[2] + bias)

print(output)