# Week 5

For **fitting the parameters** of a neural network for a training set there are learning algorithms.

- L = total number of layers in this network.

- S(l) = number of units in layer L or number of neurons ( not counting the bias unit ).

- K = the number of units in output layer .

There are two types of classification problems : 

- Binary classification
  
  In this type the lables y are either 0 or 1 and we have **one output unit** so in this case **h(x) is a real number**. (K = 1)

- Multi-class classification
  
  In this type we have K distinct classes so h(x) of output units is K dimensional and we have **K output units**.  Usually K is greater than or equal 3.

**Cost Function for Neural Network**

Its a generalization of the one we use for logistic regression. Rember in extra regularization term in logistic regression, we start the sum form J =1 because we **did not regularize the bias term** theta0.

Instead of having one output we have K of them.

If there is a binary classification K = 1 and the output unit is R demensional.

![](https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/cost-function.png)

The summation form k equals one through k is for calculating the cost function **over each** of our output unit and loops through the number of output nodes so we can **calculate cost function for each of them.**

- the double sum simply adds up the logistic regression costs calculated **for each cell** in **the output layer**.

In the cost function term we are comparing Y(k) which is k'th elemnts of our output unit (what the cost should be) with h(x)k which is the hypothesis we got for element number K in our neural network.

The regularization term is summing over these terms of theta j i l for all values of i and j .We must account for **multiple theta matrices**. The number of columns in our current theta matrix is equal to the number of nodes in our current layer (including the bias unit). The number of rows in our current theta matrix is equal to the number of nodes in the next layer (excluding the bias unit). As before with logistic regression, **we square every term for each layer**.

- the triple sum simply adds up the squares of all the individual Θs in the **entire network**.

We use regularization term because we are computing the activation of neurons. (Dont sum over the terms bias values which is terms responding <u>where is i equal to zero</u> becuase <u>after regualrization thier value become zero</u>).

**Backpropagation Algorithm**

Another learning algorithm is for minimizing the cost function. We would linke to **find parameters theta** to minimize j of theta. Either using gradient decscent or another advance optimization algorithms we need an algorithm to **get an input theta** and **computes j of theta** and **their partial derivative terms**.

We can calculate j of theta using cost function and now we will talk how to compute partial derivative terms.

1. For computing the activation values for all neurons in our neural network we apply forward propagation to compute wheter a hypothises outputs given the input.

2. For computing the derivativers we use backpropagation. In this algorithm we compute delta(l)j which represent the error of j in layer l (**how do we wish the activation value was**). if we have k output units we compute delta for each term. a can be written as h(x) also.
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/delta.png" alt="" data-align="center" width="204">
   
   When we compute delta for output layer we will compute it for earlier layers in our network from right to left.
   
   The delta values of **layer l** are calculated by multiplying the **delta values in the next layer** with the **theta matrix of layer l**. We then element-wise **multiply that with a function called g'**, or g-prime, which is the **derivative of the activation function g evaluated with the input values given by z(l)**.
   
   ![](https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/delta-earlier-layers.png)
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/g.png" alt="" width="167" data-align="center">
   
   Remeber **we dont compute delta for first layer** becuase the activation value for layer one is the input value and there is no error.
   
   The fact we compute the delta terms for the output layer and then we go back a layer and compute the delta terms for previous layers we are sort of back propagating the errors from output layer to other layers.
   
   We can compute derivitives using by activations and these delta terms.( Ignoring lambda or if it is zero ).
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/big-delta.png" alt="" width="181" data-align="center">
   
   and the vectorized implementation is :
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/vectorized-big-delta.png" alt="" data-align="center" width="226">
   
   Then we compute D(L)ij terms .
   
   The case of j equals zero corresponds to the bias term so when j equals zero that's why we're missing is an extra regularization term.
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/di.png" width="221" data-align="center">
   
   and finally we compute partial derivitives using D matrix.
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/partial-derivitive.png" alt="" data-align="center" width="220">

**Summary of Back Propagation Algorithm**

![](https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/summary.png)

So delta terms are computing :

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/delta-z-term.png" alt="" width="234" data-align="center">

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/cost-i.png" alt="" width="234" data-align="center">

If we change z(l)j values we can affect to the values of deltas.

for example:

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/example-1.png" alt="" data-align="center" width="196">

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/example-2.png" alt="" data-align="center" width="204">

Dont write derivitives for bias units.

**Unrolling parameters**

1. We put vectors together( unroll ) to pass it to fminunc.

2. After that we reshape and get each theta.

3. We compute derivitives using back propagation.

4. Put together derivitives( unroll ) and get a gradient vector.

**Gradient Checking**

Back prop as an algorithm has a lot of details and can be a little bit tricky to implement and one unfortunate property is that there are many ways to have subtle bugs in back prop. So that if you run it with gradient descent or some other optimizational algorithm, it could actually look like it's working and your cost function, J of theta may end up decreasing on every iteration of gradient descent. 

But this could prove true even though there might be some bug in your implementation of back prop. So that it looks J of theta is decreasing, but you might just wind up with a neural network that has a higher level of error than you would with a bug free implementation.

Gradient checking will assure that our backpropagation works as intended. We can approximate the derivative of our cost function with:

- **Theta is a real number**


  <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/plot-gradient-checking.png" alt="" width="257" data-align="center">
  
  
  <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/gradientchecking-1.png" alt="" data-align="center" width="278">
  
  ϵ = 0.0001

- **Theta is a vector**
  
  ![](https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/theta-vector.png)
  ![](https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week5/pictures/theta-vector-j.png)

Finally we check it **gradApprox ≈ deltaVector**. 

Once you have verified **once** that your backpropagation algorithm is correct, **you don't need to compute gradApprox again**. The code to compute gradApprox can be very slow.

**Random intialization**

If we <u>initialize theta to zero</u> then all the <u>activation function in a layer will be equal</u> so that make all the <u>delta values be equal</u> and it means <u>the partial derivitives become also equal</u> so the **theta the gradient descent finds for each node in a layer will be equal** and this will cause a **symmetric weights** problem.

<u>Symmetry breaking</u> : Define a random initialize theta between -ϵ and ϵ.

**Steps for creating a neural network**

1. Pick a network architecture
   
   - Number of input units = dimension of features x(i)
   
   - Number of output units = number of classes
   
   - Number of hidden units per layer = usually more the better (must balance with cost of computation as it increases with more hidden units)
   
   - Defaults: 1 hidden layer. If you have more than 1 hidden layer, then it is recommended that you have the same number of units in every hidden layer.

2. Training a neural network
   
   1. Randomly initialize the weights
   
   2. Implement forward propagation to get hΘ​(x(i)) for any x(i)
   
   3. Implement the cost function
   
   4. Implement backpropagation to compute partial derivatives
   
   5. Use gradient checking to confirm that your backpropagation works. Then disable gradient checking.
   
   6. Use gradient descent or a built-in optimization function to minimize the cost function with the weights in theta.
   
   J(theta) is non-convex and can get in local minimum.
