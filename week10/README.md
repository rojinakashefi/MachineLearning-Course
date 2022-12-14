# Large scale machine learning

We have a very large training set gradient descent becomes a computationally very expensive procedure.

## Batch Gradient Descent

One version of gradient descent is also called Batch gradient descent and the term Batch refers to the fact that we're looking at all of the training examples at a time. We call it sort of a batch of all of the training examples.

## Stochastic Gradient Descent

The ideas of Stochastic gradient descent is fully general and also applies to other learning algorithms like logistic regression, neural networks and other algorithms that are based on training gradient descent on a specific training set.

That doesn't need to look at all the training examples in every single iteration, but that needs to look at only a single training example (x(i), y(i)) in one iteration.

Stochastic gradient descent every iteration is going to be much faster because we don't need to sum up over all the training examples But every iteration is just trying to fit single training example better.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/sgd-bgd.png)

## Mini Batch Gradient Descent

Another variation on these ideas is called Mini-batch gradient descent they can work sometimes even a bit faster than stochastic gradient descent. after watching b examples we take a step to global minumim.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/mbgds.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/mbgds-2.png)

So, why do we want to look at b examples at a time rather than look at just a single example at a time as the Stochastic gradient descent? 

The answer is in vectorization. In particular, Mini-batch gradient descent is likely to outperform Stochastic gradient descent only if you have a good vectorized implementation. In that case, the sum over 10 examples can be performed in a more vectorized way which will allow you to partially parallelize your computation over the ten examples. So, in other words, by using appropriate vectorization to compute the rest of the terms, you can sometimes partially use the good numerical algebra libraries and parallelize your gradient computations over the b examples, whereas if you were looking at just a single example of time with Stochastic gradient descent then, you know, just looking at one example at a time their isn't much to parallelize over. 

At least there is less to parallelize over. 

One disadvantage of Mini-batch gradient descent is that there is now this extra parameter b, the Mini-batch size which you may have to fiddle with, and which may therefore take time. But if you have a good vectorized implementation this can sometimes run even faster that Stochastic gradient descent. 

So that was Mini-batch gradient descent which is an algorithm that in some sense does something that's somewhat in between what Stochastic gradient descent does and what Batch gradient descent does. And if you choose their reasonable value of b. I usually use b equals 10, but, you know, other values, anywhere from say 2 to 100, would be reasonably common. 

So we choose value of b and if you use a good vectorized implementation, sometimes it can be faster than both Stochastic gradient descent and faster than Batch gradient descent.

## Stochastic Gradient Descent Convergence

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/convergence.png)

In left top picture the red line is when we use smaller learning rate.

And when we have a noisy output like top right and left buttom we  can increase the number of examples to see a smooth line.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/pic1.png)

For setting alpha :

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/alpha.png)

## Online Learning

Today, many of the largest websites, or many of the largest website companies use different versions of online learning algorithms to learn from the flood of users that keep on coming to, back to the website. Specifically, if you have a continuous stream of data generated by a continuous stream of users coming to your website, what you can do is sometimes use an online learning algorithm to learn user preferences from the stream of data and use that to optimize some of the decisions on your website.

In online learning setting where actually discarding the notion of there being a fixed training set instead we have an algorithm. Now what happens as we get an example and then we learn using that example like so and then we throw that example away. We discard that example and we never use it again and so that's why we just look at one example at a time. We learn from that example. We discard it. Which is why, you know, we're also doing away with this notion of there being this sort of fixed training set indexed by i.

Interesting effect of this sort of online learning algorithm is that it can adapt to changing user preferences.

## Map reduce and Data Parallelism

Some machine learning problems are just too big to run on one machine, sometimes maybe you just so much data you just don't ever want to run all that data through a single computer, no matter what algorithm you would use on that computer.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/mapreduce.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/multi-com.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week10/pictures/multi-core.png)
