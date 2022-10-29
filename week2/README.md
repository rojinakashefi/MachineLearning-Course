# Week 2

**Multivariate Linear Regression**

Notation for equations where we can have any number of input variables(features).

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/notations.png" alt="notations.png" width="389" data-align="center">

The multivariable form of the hypothesis function accommodating these multiple features is as follows:

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/multivariate-linear-regression.png" alt="" width="348" data-align="center">

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/multivariate-linear-regression-matrix.png" alt="" width="254" data-align="center">

**Gradient Descent For Multiple Variables**

The gradient descent equation itself is generally the same form; we just have to repeat it for our 'n' features:

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/gradient-descent.png" alt="" width="390" data-align="center">

**Feature Scaling & Mean normalization**

We can speed up gradient descent by having <u>each of our input values</u> in roughly the **same range**.

θ will descend quickly on small ranges (for example (0,5) ) and slowly on large ranges (for example (0,2000) ).

The way to prevent this is to modify the ranges of our input variables so that they are all roughly the same. Ideally:

−1 ≤ x(i)​ ≤ 1     or        −0.5 ≤ x(i)​ ≤ 0.5    (These aren't exact requirements)

The goal is to get **all** input variables into roughly one of these ranges using two techniques:

- Feature Scaling :
  
  Feature scaling involves **dividing the input values by the range** (i.e. the maximum value minus the minimum value) of the input variable, resulting in a new range of just 1.

- Mean normalization :
  
  Mean normalization involves subtracting the average value for an input variable from the values for that input variable resulting in a new average value for the input variable of just zero. 
  
  Where μi​ is the **average** of <u>all the values for feature (i) </u>and si​ is the range of values (max - min), or si​ is the standard deviation. (dividing by the range, or dividing by the standard deviation, give different results.)
  
  <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/mean-normalization.png" alt="mean-normalization.png" width="233" data-align="center">

**Learning Rate**

If u want to check that gradient descent works correctly (Debugging gradient descent) make a plot with *number of iterations* on the x-axis. Now plot the cost function, J(θ) over the number of iterations of gradient descent. If J(θ) ever increases, then you probably need to decrease α.

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/learning-rate.png" alt="learning-rate.png" width="336" data-align="center">

For sufficiently small learning rates, J(θ) should decrease on every iteration.but if learning rate is too small, gradient descent can be slow to converge.

To check gradient descent has led to converage:

- Plot : you can see in plot with x axis of number of iteration and y of J(θ) if we had led to converage or not.

- Automatic convergence test : You can declare converagence if J(θ) decreases by less than 0.001 in one iteration.

**Features and Polynomial Regression**

We can improve our features and the form of our hypothesis function in a couple different ways.

1. We can **combine** multiple features into one. For example, we can combine x1​ and x2​ into a new feature x3​ by taking x1​⋅x2​.

2. Polynomial Regression : Our hypothesis function <u>need not</u> be linear (a straight line) if that does not fit the data well. We can **change the behavior or curve** of our hypothesis function by making it a quadratic, cubic or square root function (or any other form).
   
   <u>One important thing to keep in mind is, if you choose your features this way then feature scaling becomes very important.</u>

**Normal Equation**

Gradient descent gives one way of minimizing J. A second way of doing so, this time performing the minimization explicitly and without resorting to an iterative algorithm. 

In the "Normal Equation" method, we will minimize J by explicitly taking its derivatives with respect to the θj ’s, **and setting them to zero.** This allows us to find the optimum theta without iteration. The normal equation formula is given below:

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/normal-equation.png" alt="normal-equation.png" width="248" data-align="center">

There is **no need** to do feature scaling with the normal equation.

With the normal equation, computing the inversion has complexity O(n3). So if we have a very large number of features, the normal equation will be slow. In practice, when n exceeds 10,000 it might be a good time to go from a normal solution to an iterative process.

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week2/pictures/comparsion.png" alt="comparsion.png" width="388" data-align="center">

If inverse matix is **noninvertible,** the common causes might be having :

- Redundant features, where two features are very closely related (i.e. they are linearly dependent)

- Too many features (e.g. m ≤ n). In this case, delete some features or use "regularization" (to be explained in a later lesson).

Solutions to the above problems include **deleting a feature** that is linearly dependent with another or deleting one or more features when there are too many features.
