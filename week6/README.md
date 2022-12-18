# Week 6

In this week we talk about developing a machine learning system or trying to improve the performance of a machine learning system.

1. Get more training examples

2. Try smaller set of features

3. Try getting additional features

4. Tru adding polynomial features

5. Try decreasing lambda

6. Try increasing lambda

---

#### **Machine learning diagnostic**

It means how to evaluate learning algorithms.

- **Diagnostic** 
  
  A test you can run to gain insight what is/isn't working with a learning algorithm, and gain guidance as to how to improve its performance and it take time to implement but very good use of time.

---

#### **Evaluating a Hypothesis**

There is a tought which getting a really low value of training error might be a good thing, but we have already seen that just because a hypothesis has low training error, that doesn't mean it is necessarily a good hypothesis and we've already seen the example of how a hypothesis can overfit and therefore **fail to generalize**the new examples in the training set.

1. Plot a hypothesis

2. Splitting our Dataset
   
   1. Split out dataset in two portion
   
   2. First portion is our training set (70%)
   
   3. Second portion is test set (30%)
   
   **Better randomly select each portion.**

**Training/Testing procedure**

1. Learn parameter theta from training data (minimizing training error J(Theta))

2. Compute test set error ( Jtest(Theta) ) 
   
   1. **Linear Regression**
      
      Used squared error :
      
      <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/linear-regression-jtest.png" title="" alt="" width="373">
   
   2. **Logistic Regression**
      
      1. Compute cost function
         
         ![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/logistic-regression-jtest.png)
      
      2. Misclassification error
         
         EIther you get a example right or wrong.
         
         ![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/miss-classification.png)

---

#### **Model Selection**

Try to choose what degree polynomial to fit to data. So next to <u>theta parameter</u>you are trying to <u>define degree of polynomial</u> known as d.

You want to choose <u>a model</u> that choose <u>a degree of polynomial</u> to <u>fit the model</u> and also get some <u>estimate of how well your fitted hypothesis was generalize to new examples</u>.

1. Try all models

2. Minimize their training errors and this would give you some parameter vector theta.

3. Then compute Jtest for each model using the parameter we get for each model.

4. As a best fit choose the model which ended up with lowest test cost.

But this isn't right about generalizing our hyphotesis because we fit d using test set and it would fo better on this test set than it would on new examples that it hasn't seen before.

We split our dataset to three parts.

1. First section our Training set ( 60% )

2. Second section cross validation ( CV ) ( 20% )

3. Third section our Test set ( 20% )

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/tr-cv-ts.png" title="" alt="" width="320">

Instead of using test set to select the model, we use the **cross validation set to select the model**. In this way we compute Jcv with theta it composed from min cost function and in this way <u>we fit d on our cv dataset and we can use our test set to estimate the generalization error of the model</u>.

---

#### **Diagnoising Bias vs. Variance**

If you run a learning algorithm and it doesn't do as long as you are hoping, it will be either a high bias problem or a high variance problem, in other words, either an underfitting problem or an overfitting problem. In this case, it's very important to figure out which of these two problems is bias or variance or a bit of both that you actually have.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/jtrain-vs-jcv1.png" title="" alt="" width="196">

If your **Jcv or J test** is High:

1. If d is small > high bias

2. If d is big > high variance.

**Bias (underfit)** :

1. J train will be high

2. J cv = J train

3. Train set will be high

**Variance (overfit)** :

1. J train will be low

2. J cv >> J train

3. Train set will be low

---

#### **Regularization and Bias/Varianve**

- If lambda is too big we have a underfitting problem.

- If lambda is too small we have a overfitting problem.

You can use different lambdas from a specific range and find the theta which minimize the cost function using regularization term, then compute  Jcv without regularization term and only with squared error part and pick the one which give the smallest value for cross validation set.apply it on Jtest​(Θ) to see if it has a good generalization of the problem.

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/lambda-jtrain-vs-jcv.png" alt="" width="237">

---

#### **Learning Curves**

Learning curves is often a very useful thing to plot. If either you wanted to sanity check that your algorithm is working correctly, or if you want to improve the performance of the algorithm.

Training an algorithm on a **very few number of data points** (such as 1, 2 or 3) will easily **have 0 errors** because we can always find a quadratic curve that touches exactly those number of points. Hence:

- As the training set gets larger, the error for a quadratic function increases.

- The error value will plateau out after a certain m, or training set size.

- On cross validation set because we cant generalize the hypothesis we get from three training set in cv set we have a high error at first but after increasing the training set we can fit to cv set better so the error reduces.
  
  <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/m-jtrain-vs-jcv.png" title="" alt="" width="331">

**Experiencing high bias:**

**Low training set size**: causes Jtrain​(Θ) to be low and JCV​(Θ) to be high.

**Large training set size**: causes both Jtrain​(Θ) and JCV​(Θ) to be high with Jtrain​(Θ)≈JCV​(Θ).

If a learning algorithm is suffering from **high bias**, getting more training data will not **(by itself)** help much.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/m-highbias.png" title="" alt="" width="193">

**Experiencing high variance:**

**Low training set size**: Jtrain​(Θ) will be low and JCV​(Θ) will be high.

**Large training set size**: Jtrain​(Θ) increases with training set size and JCV​(Θ) continues to decrease without leveling off. Also, Jtrain​(Θ) < JCV​(Θ) but the difference between them remains significant.

If a learning algorithm is suffering from **high variance**, getting more training data is likely to help.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/m-highvariance.png" title="" alt="" width="194">

---

#### **Summary**

- **Getting more training examples:** Fixes high variance

- **Trying smaller sets of features:** Fixes high variance

- **Adding features:** Fixes high bias

- **Adding polynomial features:** Fixes high bias

- **Decreasing λ:** Fixes high bias

- **Increasing λ:** Fixes high variance.

**Diagnosing Neural Networks**

- A neural network with fewer parameters is **prone to underfitting**. It is also **computationally cheaper**.

- A large neural network with more parameters is **prone to overfitting**. It is also **computationally expensive**. In this case you can use regularization (increase λ) to address the overfitting.

Using a single hidden layer is a good starting default. **You can train your neural network on a number of hidden layers using your cross validation set**. You can then select the one that performs best.

---

#### **How to spend your time to improve the accuracy of this classifier?**

- Collect lots of data (for example "honeypot" project but doesn't always work)

- Develop sophisticated features (for example: using email header data in spam emails)

- Develop algorithms to process your input in different ways (recognizing misspellings in spam).

The **recommended approach** to solving machine learning problems is to:

- Start with a simple algorithm, implement it quickly, and test it early on your cross validation data.

- Plot learning curves to decide if more data, more features, etc. are likely to help.

- **Error analysis** : Manually examine the errors on examples in the cross validation set and try to spot a trend where most of the errors were made.

It is very important to get error results as a single, **numerical value**. Otherwise it is difficult to assess your algorithm's performance.

**Precision/Recall**

 y = 1 in presence of rare class that we want to detect. used for skewed classes.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/precision:recall.png" title="" alt="" width="170">

Precision : Of all the cases we **predicted** true (y=1), what fraction **actually** are true.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/precision.png" title="" alt="" width="340">

Recall : Off all the cases which **actually** are true,  How many did we **predicted** true.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/recall.png" title="" alt="" width="344">

**Trade off between precision/Recall**

In generall be can say : *Predict 1 if hΘ(x) >= threshold*

- Predict y=1 only if we are very confident
  
  1. Change the threshold higher : higher precision, lower recall.

- Avoid missing too many cases (avoid false negatives)
  
  1. Change the threshold lower : lower precision, higher recall.

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/precision:recall:tradeoff.png" title="" alt="" width="219">

For comparing algorithm using precision/recall we should have a single real number evaluation metric.

**F score** = 2 * ((P * R) / ( P+R ) )

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week6/pictures/fscore.png" title="" alt="" width="250">
