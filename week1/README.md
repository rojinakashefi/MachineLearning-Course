# Week 1



Two **definitions of Machine Learning** are offered.

1. Arthur Samuel: "The field of study that gives computers the ability to learn without being explicitly programmed." 

2. Tom Mitchell: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."      
   
     

**Supervised** **Learning**

In supervised learning, we are <u>given a data</u> set and already know what our correct <u>output should look like</u>, having the idea that there is a relationship between the input and the output. Supervised learning problems are categorized into "regression" and "classification" problems.

- Regression problem : 
  
  we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function.

- Classification probelm :
  
  we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories.

**Unsupervised Learning**

Unsupervised learning allows us to approach problems with little or <u>no idea what our results should look like</u>. We can <u>derive structure from data</u> where we don't necessarily know the effect of the variables. We can derive this structure by **clustering the data**  **based on relationships among the variables** in the data.

Real word usage of clustering algorithm:

- Organize computer clusters

- Social network analysis

- Market segmentation

- Cocktail party problem

**Model representation**

1. We’ll use x(i) to denote the “input” variables , also called input features.

2. We'll use y(i) to denote the “output” or target variable that we are trying to predict.

3. A pair (x(i),y(i)) is called a training example.

4. The dataset that we’ll be using to learn —a list of m training examples (x(i),y(i));i=1,...,m— is called a training set.

5. We will also use X to denote the <u>space</u>of input values, and Y to denote the <u>space</u> of output values.

**Supervised learning using model representation**

Our goal is, <u>given a training set</u>, <u>to learn a function</u> h : X → Y so that h(x) is a “good” predictor for the corresponding value of y. This function h is called a hypothesis.

- Regression problem :
  
  When the <u>target variable</u> that we’re trying to predict is <u>continuous</u> we call the learning problem a regression problem. 

- Classification probelm :
  
  When <u>target variable</u> can take on only a <u>small number of discrete values</u>, we call it a classification problem. 
  
     

**Cost function**

We can measure the accuracy of our hypothesis function by using a cost function. This takes an average difference of all the results of the hypothesis with inputs from x's (predicted value) and the actual output y's (actual value). This function is otherwise called the "Squared error function", or "Mean squared error".

We need to choose θ(0) and θ(1) in h which minimzie the diffrence bewteen predicted value and actual value. ( idelly diffrecence = 0 → cost function = 0)

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/tree/main/week1/pictures/cost-function.png" data-align="center" width="412">

- Cost Function - Intuition I
  
  Our training data set is scattered on the x-y plane. We are trying to make a line (defined by hθ​(x)) which passes through these scattered data points. There are two plots first for h : X → Y and the second for cost function : θ → J(θ)
  
  Our objective is to get the best possible line. The best possible line will be such so that the**average squared <u>vertical distances</u> of the scattered points from the line will be the least.** Ideally, the line should pass through all the points of our training data set. In such a case, the value of J(θ0​,θ1​) will be 0.

- Cost Function - Intuition II
  
  A contour plot is a graph that contains many contour lines. A contour line of a
  
  **two variable function** has a **constant value** at **all points of the same line.** Going along the 'circle', one would expect to get the same value of the cost function.
  
  There are two plots first for h : X → Y and the second for J(θ0,θ1) : θ0 → θ1

**Gradient Descent**

So we have our hypothesis function and we have a way of measuring how well it fits into the data. Now we need to **estimate the parameters in the hypothesis function**.

We put θ0​ on the x axis and θ1​ on the y axis, with the cost function on the vertical z axis. We will know that we have succeeded when our cost function is at the very bottom of the pits in our graph, when its value is the minimum.

The way we do this is by taking the derivative (**the tangential line to a function**) of our cost function. The **slope of the tangent** is the derivative at that point and it will give us a direction to move towards. We make steps down the cost function in the direction with the <u>steepest descent</u>. The <u>size of each step</u> is determined by the **parameter α**, which is called the **learning rate**.

A smaller α would result in a smaller step and a larger α results in a larger step.

 The direction in which the step is taken is determined by the <u>partial derivative</u> of J(θ0​,θ1​).

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/tree/main/week1/pictures/gradient-descent.png" data-align="center" width="194">

**Gradient Descent intuition**

Used one parameter θ1​ and plotted its cost function to implement a gradient descent

1. Regardless of the slope's sign, θ1​ eventually converges to its minimum value.

2. When the slope is negative, the value of θ1​ increases and when it is positive, the value of θ1​ decreases.

3. if α is too small gradient descent can be slow.

4. if α is too large gradient descent can overshoot the minimum. It may fail to converge or even diverge.

5. At the minimum, the derivative will always be 0.

6. Gradient descent can converge to a local minimum,even with fixed learning rate. because as we approach a local minimum, gradient descent will automatically take smaller steps (because of slop of tangent will be reduced).

**Gradient Descent For Linear Regression**

When specifically applied to the case of linear regression, a new form of the gradient descent equation can be derived. We can substitute our actual cost function and our actual hypothesis function and modify the equation to :

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/tree/main/week1/pictures/gradient-descent-linear-regression.png" alt="gradient-descent-derivative.png" width="229" data-align="center">

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/tree/main/week1/pictures/gradient-descent-derivative.png" alt="gradient-descent-derivative.png" width="229" data-align="center">

So, this is simply gradient descent on the original cost function J. This method looks at every example in the entire training set on every step, and is called **batch gradient descent**.
