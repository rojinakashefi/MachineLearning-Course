# Week 7

**Support Vector Machine**

SVM sometimes gives a cleaner, and sometimes more powerful way of learning complex non-linear functions.

Cost Function of Logistic regression for a single training example looks like:

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/logistic-regreesion-cost-1.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/logistic-regression-cost-2.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/svm-cost.png)

We **remove term 1/m** in logistic regression because the <u>coeffiecent doesnt make change in  the answer</u> so now the **logistic regression form is A + lambda * B**. (A : we wanted the training set well, B: keeping the values of the parameter small)

In **SVM we use C * A + B**.

So for logistic regression, if we set a very large value of lambda, that means you will give B a very high weight. Here is that if we set C to be a very small value, then that responds to giving B a much larger rate than C, than A.

If C = 1/lambda then the logistic term and svm be the same.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/svm-cost-1.png)

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/svm-hypothesis.png" title="" alt="" width="227">

**SVM Descision Boundary**

- Linear separable case
  
  <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/margin.png" title="" alt="" width="214">

- Linear separable case in presence of outliners
  
  If c very large the line will change but if c is small the line wont change that much.
  
  <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/outliner.png" title="" alt="" width="311">

Vector theta must be 90 degrees to decision boundry.

**Kernels**

Kernels are used for adapting support vector machines in order to develop complex nonlinear classifiers.

Instead of defining <u>a lot of</u> feature , given x we compute new feature depending on proximity to landmarks l(1), l(2), l(3).

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/kernel.png)

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/f-conditions.png" title="" alt="" width="292">

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/kernel-hypothesis.png" title="" alt="" width="291">

**Choosing the landmarks**

The idea is we're gonna take the examples and for every 

training example that we have, we're just going 

to put landmarks as exactly the same locations as the training examples.

This shows **how close** the training sets are with each other.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/choosing-landmarks.png" title="" alt="" width="293">

In this case n ( number of features) = m.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week/pictures/kernel-cost.png)

**SVM parameters**

C = 1/ lambda

- Large C: Lower bias, high variance.

- Small C: Higher bias, low variance.

Sigma squared

- Large Sigma squared: Features fi vary more smoothly. Higher bias, Lower variance.

- Small Sigma squared: Features fi vary less smoothly.
  
  Lower bias, Higher variance.

**Using An SVM**

- Linear Kernel
  
  n (features) is large, m (training set) is small.
  
  You can use logistic regression

- Gaussian kernel
  
  n is small, m is intermediate.
  
  Perform feature scaling before using the gaussian kernel.

- Create/add more feature
  
  n is small, m is large.
  
  Use logistic regreesion or SVM without using a kernel.

- Polynomial kernel
  
  K (X,L) = ( X(T).L + constant ) ^ degree.
  
  Used when X and L are never negative.

<u>All the kernel we use must satisfy "Mercer's Theorem".</u>

SVM is convex and always find the global minimum.

**SVM in multi-class classification**

Using one-vs-all methods. (Train K SVMs, one to distingush y=i from the rest i=1,2,...,K then get theta(1),theta(2),...,theta(k) and pick class i with largest theta(i)T*X )
