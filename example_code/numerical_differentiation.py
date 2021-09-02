'''
** Numerical differentiation **

Example code that explores the concept of numerical differentiation.

'''

import matplotlib.pyplot as plt
import numpy as np

# Non linear function
def f(x):
    return 2*x**2

# Plot the curve on a graph using np.array
x = np.array(np.arange(0, 5, 0.001))
y = f(x)

plt.plot(x, y)

# 5 colours to be used for plotting tangent lines
colours = ['k', 'g', 'r', 'b', 'c']


# Tagent line calulation as a function so it can be called 
# multiple times for different values of x 
# approximate_derivative and b are constant for a given function 
# thus calculated once above this function 
def tangent_line(x):
    return approximate_derivative*x + b


def approximate_tangent_line(x, approximate_derivative):
    return (approximate_derivative*x) + b

# Plotting 5 tanget lines
for i in range(5):
    
    # Applied to give two 'sufficently close' points to calculate the slope
    p2_delta = 0.0001

    x1 = i
    x2 = x1+p2_delta

    y1 = f(x1)
    y2 = f(x2)

    print((x1, y1), (x2, y2))

    # Derivative approximation and y-intercept for tangent line 
    approximate_derivative = (y2-y1)/(x2-x1)
    b = y2 - approximate_derivative*x2


    # Plotting the tangent line 
    # +/- 0.9 to draw the tangent line on our graph 
    # then we calculate the y for given x using the tangent line function 
    # Matplot will draw a line for us through these points 
    to_plot = [x1-0.9, x1, x1+0.9]
    
    plt.scatter(x1, y1, c=colours[i])
    plt.plot([point for point in to_plot], 
        [approximate_tangent_line(point, approximate_derivative) 
        for point in to_plot], c=colours[i])

    print('Approximate derivative for f(x)', 
    f'where x = {x1} is {approximate_derivative}')

plt.show()