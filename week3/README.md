# Week 3

**Classification**

The classification problem is just like the regression problem, except that the values we now want to predict take on only a small number of discrete values.For now, we will focus on the **binary classification** **problem** in which y∈{0,1}. 0 is also called the negative class, and 1 the positive class, and they are sometimes also denoted by the symbols “-” and “+.” Given x(i), the corresponding y(i) is also called the label for the training example.

To attempt classification, one method is to use linear regression and map all predictions greater than 0.5 as a 1 and all less than 0.5 as a 0. However, this method doesn't work well because classification is not actually a linear function.

**Hypothesis representation**

Our hypotheses hθ​(x) needs to satisfy 0≤hθ​(x)≤1. This is accomplished by plugging θT*x into the Logistic Function.Our new form uses the "Sigmoid Function," also called the "Logistic Function". The function g(z), shown here, maps any real number to the (0, 1) interval.

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/sigmoid.png" alt="" data-align="center" width="124">

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/sigmoid-graph.png" alt="" width="259" data-align="center">

hθ​(x) will give us the **probability** that our output is 1. For example, hθ​(x)=0.7 gives us a probability of 70% that our output is 1. 

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/probability.png" alt="" width="274" data-align="center">

**Decision Boundary**

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/db1.png" alt="" width="209" data-align="center">

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/db2.png" alt="" width="140" data-align="center">

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/db3.png" alt="" width="166" data-align="center">

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/db4.png" alt="" width="207" data-align="center">

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/db5.png" alt="" width="237" data-align="center">

The input to the sigmoid function g(z) doesn't need to be linear, and could be a function that describes a circle or any shape to fit our data.

**Logistic Regression Model**

We cannot use the same cost function that we use for linear regression because the Logistic Function will cause the output to be<u>wavy,</u> causing many <u>local optima</u>. In other words, it will not be a convex function.

- Cost function :
  
    <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/cost-function.png" alt="vectorized-cost.png" width="294" data-align="center">
    
    
  Vectorized implementation :
  
  <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/vectorized-cost.png" alt="vectorized-cost.png" width="294" data-align="center">
  
  y = 0 :
  
  <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/cost-y=0.png" alt="cost-y=0.png" width="156" data-align="center">
  
  
  y = 1 :

  <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/cost-y=1.png" alt="cost-y=1.png" width="164" data-align="center">

- Gradient Descent :
  
  <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/gradient-descent.png" alt="gradient-descent.png" width="244" data-align="center">
  
  Vectorized implementation :
  
  <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/vectorized-gradient.png" alt="vectorized-gradient.png" data-align="center" width="296">

- Advanced Optimization :
  
  Conjugate gradient", "BFGS", and "L-BFGS" are more sophisticated, faster ways to optimize θ that can be used instead of gradient descent.

**Multiclass Classification : One-vs-all**

Some classification problmes have more than two categories. Instead of y = {0,1} we will expand our definition so that y = {0,1...n}. So we divide our problem into n+1 (+1 because the index starts at 0) binary classification problems; in each one, we predict the probability that 'y' is a member of one of our classes.

We are basically choosing **one class** and then **lumping all the others into a single second class.** We do this repeatedly, applying binary logistic regression to each case, and then use the hypothesis that returned the highest value as our prediction.

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/multiclass.png" alt="multiclass.png" data-align="center" width="213">

**The problem of overfitting :**

- Underfitting : 
  
  Underfitting or high bias is a situation which the data clearly shows its structure haven't been captured by the model and doesn’t really fit very good on a line. This happens when the form of our hypothesis function h maps poorly to the trend of the data. It is usually caused by a function that is too simple or uses too few features.

- Overfitting : 
  
  It might seem that the more features we add, the better. However, there is also a danger in adding too many features: We see that even though the fitted curve passes through the data perfectly, we would not expect this to be a very good predictor of different datas.
  
  Overfitting, or high variance, is caused by a hypothesis function that fits the available data but does not generalize well to predict new data. It is usually caused by a complicated function that creates a lot of unnecessary curves and angles unrelated to the data.

- The issue of overfitting  :
  
  1. Reduce the number of feature
     
     Manually select which features to keep.
     
     Use a model selection algorithm.
  
  2. Regularization
     
     Keep all the features, but reduce the magnitude of parameters θj​.
     
     Regularization works well when we have a lot of slightly useful features.

**Regularization**

If we have overfitting from our hypothesis function, we can reduce the weight that some of the terms in our function carry by <u>increasing their cost</u>. So, In order for the cost function to <u>get close to zero</u>, we will have to reduce the values of the features​ to near zero.

The λ, or lambda, is the **regularization parameter**. It determines how much the costs of our theta parameters are inflated.

- If lambda is chosen to be too large, it may smooth out the function too much and cause underfitting.

- If lambda is chosen to be too small, it may cause overfitting.

   <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/cost-regularization.png" alt="cost-regualirzation.png" width="283" data-align="center">

**Regularization Linear Regression**

1. Gradient descent :
   
   The first term in the above equation, will always be less than 1. Intuitively you can see it as reducing the value of θj​ by some amount on every update.
   
      <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/liner-gradient-regularization.png" alt="linear-gradient-regualirzation.png" width="283" data-align="center">
   

2. Normal Equation :
   
   L is a matrix with 0 at the top left and 1's down the diagonal, with 0's everywhere else. It should have dimension (n+1)×(n+1). 
   
   <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/linear-regualirzation.png" alt="linear-regualirzation.png" width="283" data-align="center">

**Regularization Logistic Regression**

1. Cost Function : 
   
   ![logistic-regualization.png](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/logistic-regualization.png)

2. Gradient Descent : 

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week3/pictures/gradient-regualization.png" alt="gradient-regualization.png" width="369" data-align="center">
