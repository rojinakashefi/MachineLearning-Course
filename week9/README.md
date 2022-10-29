# Week 9

## Anomaly detection

In anomaly detection problem, we're give some data sets, x1 through xm of examples, and we usually asume that these end examples are normal or non-anomalous examples, and we want an algorithm to tell us if some new example x-test is anomalous or not.

p(X) = we are going to build a model for the probability of x(features) 

having built a model of the probability of x we're then going to say that for the new x-test (feature), if p of x-test is less than some epsilon then  we flag this as an anomaly.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/P-TEST.png" title="" alt="" width="241">

Anomaly detection example:

1. Fraud detection

2. Manufacturing

3. Monitoring computers in a data center

## Guassian distribution

If x is a a distributed gaussian with mean µ, variance σ2 :

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/gauessian2.png" title="" alt="" width="268">

if σ is smaller we get higher gauessian distribution.

if σ is bigger we get wider gauessian distribution.

### Parameter estimation

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/mu-variance.png)

### Density estimation

![](/https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/p(X).png)

## Anomaly detection algorithm

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/algorithm.png)

### Anomaly detection vs supervised![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/vs.png)

### Choosing what features to use

Choose features that might take on unusually large or small values in the event of an anomaly.

 we can create new features manually using original model or use multivariate gauessian dirstribuation which automatically capture correlations between features

### Multivariate gaussian distribution

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/mgd.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/mgd-om.png)

## Recommender Systems

In predicting movie rating we use below notations:

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/movie-notation.png" title="" alt="" width="185">

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/parameter.png)

for learning theta for all users (given x):

![](/https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/all-users.png)

we use different for k's because of bias term dont have regularization

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/gradientd.png)

In the above approch we have the features list. but now we are going to recognize the systems that arent content based and learn the features itself.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/learn-x.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/learn-all-x.png)

### Collaborative filtering

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/summary.png)

instead of back and forth :

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/allllll.png)

### Collaborative filtering algorithm

There is no theta zero and we **dont** have a special case for k = 0 like before.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/cta.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/rm.png)

if a person has no rating (like last column) we use mean normalization:

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week9/pictures/mn.png)
