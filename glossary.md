# Glossary for Neural Networks

* **Accuracy** : Describes how often the largest is the correct class. 

* **Array** : An ordered homologous container for numbers, which can have one or more dimensions (N.b. In the context of nnfs book)

* **Bias** : 

* **Batches** : A package of data that contains multiple 'observations' / 'samples'

* **Categorical cross-entropy** : A loss function used to compare a "ground-truth" ( _y_ or targets) probability annd some predicted distribution ( _y-hat_ or 'predictions'). It is one of the most commonly used loss function with a softmax activation on the output layer

* **Classification** : The process of recognising, understanding, and grouping ideas and objects into preset categories or “sub-populations”

* **Confidence score** : A score for a prediction adding up to _1_ (e.g. confidence a classificaition is class A or class B, 0.45 and 0.55 respectively)

* **Cross product** : 

* **Dead neuron** : A 'neuron' that outputs '0' everytime. 

* **Deep** : Used to describe a neural network with 2 or more 'hidden layers'

* **Dense layer** : A layer in which each neuron of a given layer is connected to every neuron of the next layer

* **Derivative** : The slope of the tangent line for a function that takes a single parameter as an input.

* **Dot product** : Is the sum of products of consecutive vecor elements (e.g. the multiplication and addition operations performed on 'weights' and 'inputs' of a neuron)

* **Exploding values** : Very large numbers that cause problems with neural networks 

* **Feature** : An individual measurable property or characteristic of a phenomenon

* **Feature observation datum** : 

* **Fully connected neural network** : A neural network where every neuron in the current layer has connection to every neuron from the previous layer

* **Generalisation** : The process of training a model to accurately predict on training data as well as out-of sample data

* **Hidden layers** : The layers inbetween the inputs and outputs in a Neural Network 

* **Homologous** : An array (e.g. a list of lists) where each list is the same length

* **Instantaneous slope** : The slope at a given point

* **Linear activiation function** : An activation function usually applied to the last layers output in the case of a regression model

* **Linear function** : The equation of a line. 

* **Log (logarithm)** : The solution for the x-term in an equation of the form `a^x = b` (e.g. `10^x = 100` can be solved with a log: `log10(100)`, which evaluates to 2). 

* **Loss** : A metric to measure 'wrong' a model is when making predictions

* **Loss function (cost function)** : An algorithm that quantifies how wrong a model is. 

* **Matrix** : Is a retangular array with two dimensions (e.g. a list of lists) 

* **Matrix Product** : An operation in which we have 2 matrices, and dot products is performed for all combinations of rows from the first matrix and the columns of the second matrix, resulting in a matrix of dot products (https://nnfs.io/jei/)

* **(Artificial) Neural networks** : Type of machine learning, often used for deep learning

* **Neuron** : A mathmatical function that takes one or more inputs and multiplys them by weights

* **Normalisation** : 

* **Numerical differentiation** : A method for calculating derivatives (e.g. calculating the slope of a tangent line using two infinitely close points)

* **Observation** : One sample of a feature set

* **One-hot (vector)** : One of the values in the vector is 'hot' (on), with a value of 1, and the rest are 'cold' (off) with a value of 0 (e.g. `[1, 0, 0]`) 

* **Overfitting** : Refers to a model that models the training data too well, which negatively impacts the performance of the model when presented with new data

* **Parameters** : The weights and biases of a neural network. 

* **Partial derivative** :

* **Preprocess** : Converting 'raw' data into numeric form using function such as 'normalisation' and 'scaling'

* **Rectified Linear (ReLU) activation function** : A function where if _x_ is less than ot equal to _0_ then _y_ is _0_, otherwise _y_ is equal to _x_. This is more simple to compute than a sigmoid activation function. 

* **Regression** : A method for prediciting numerical values (e.g. stock prices) 

* **Sample** : More common term for 'Observation'

* **Scaling** : 

* **Sigmoid activation function** : A more granular step function when compared to the 'Step activiation function', which provides additional information that allows for determining how close the function was to 'activating or 'deactivating

* **Slope** : An inidication of a lines steppness of inclination, which is usually denoted as _m_

* **Softmax activation function** : An activation function used for classification that outputs a confidence score for each class (probability distribution)

* **(Mean) squared error** : A loss function used for neural networks that perform regression.

* **Step activation function** : A function that causes the neuron to fire and output a 1 if the *weights x inputs + bias* results in a value greater than 0, outherwise it will output 0 

* **Supervised learning** : A form of machine learning where a pre-established and labeled data set can be used to train the model 

* **Tangent line** : The line through a pair of infinitely close points on a curve. The function for a straight line is `y = mx+b` Where:
    * _y_ : is how far up or down the line is on the graph
    * _m_ : is the slope or approximate derivative 
    * _x_ : is how far along the line is on the graph 
    * _b_ (or y-intercept): the point where a line or curve crosses the y-axis on a graph (https://nnfs.io/but/). To calculate _b_ the formula is `b = y - mx`

* **Tensor** : A tensor object is an object that can be represented as an array  

* **Transposition** : The process of modifying a matrix where rows become columns and columns become rows

* **Unsupervised learning** : A form of machine learning where the a machine finds structure in data without knowing the classifications ahead of time

* **Vector** : An array with a single dimension (e.g. a list)

* **Weight** : A trainable factor of how much of an input is used