import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(5))

'''
# Linear function: f(x) = 2x
def f(x):
    return 2*x 

y = f(x)

print(x)
print(y)

plt.plot(x, y)
plt.show()

# Calculating slope: Change in y / Change in x
# Change in y: P2y - P1y
# change in x: P2x - P1x
print((y[1]-y[0]) / (x[1]-x[0]))
'''

# Non-linear function: f(x)=2x^2
def f(x):
    return 2*x**2

y = f(x)

print(x)
print(y)

# Calculating the change for the first pair of points
print((y[1]-y[0]) / (x[1]-x[0]))

# Calculating the change for the next pair of points
print((y[3]-y[2]) / (x[3]-x[2]))



p2_delta = 0.0001

x1 = 1
x2 = x1 + p2_delta # add delta

y1 = f(x1) # result at the derivation point 
y2 = f(x2) # result at the other, close point

approximate_derivative = (y2-y1)/(x2-x1)
print(approximate_derivative)