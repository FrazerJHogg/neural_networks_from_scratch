import math

# An example output from the output layer of the neural network 
softmax_output = [0.7, 0.1, 0.2]

# Ground-truth - one-hot target vectors 
target_output = [1, 0, 0]

loss = -(
    math.log(softmax_output[0])*target_output[0] +
    math.log(softmax_output[1])*target_output[1] +
    math.log(softmax_output[2])*target_output[2]
)

print('full equation result: ', loss)

# Simplified equation due to target outputs being '0'
# Negative log of the target class' confidence score 

loss = -math.log(softmax_output[0])

print('simple equation result: ', loss)


# A larger loss value will be provided if a confidence 
# score is lower

print('Loss with a confidence score of "1":', math.log(1.0))
print('Loss with a confidence score of "0.95":', math.log(0.95))
print('Loss with a confidence score of "0.90":', math.log(0.90))
print('Loss with a confidence score of "0.80":', math.log(0.80))
print('\n ... \n')
print('Loss with a confidence score of "0.20":', math.log(0.20))
print('Loss with a confidence score of "0.10":', math.log(0.10))
print('Loss with a confidence score of "0.05":', math.log(0.05))
print('Loss with a confidence score of "0.05":', math.log(0.01))