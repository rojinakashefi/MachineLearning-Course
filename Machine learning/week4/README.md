# Week 4

**Non-linear Hypotheses**

when we have a complex training set we can apply logistic regression with a lot of nonlinear features such as polynomial terms and if we include enough polynomial terms maybe we can get a good hypotheses.

But what if we have a **lots of features** ?  if you were to include all the quadratic terms, all of these, even all of the quadratic that is the second or the polynomial terms, there would be a lot of them. So including all the quadratic features doesn't seem like it's maybe a good idea, because that is a lot of features and you might up **overfitting** the training set, and it can also be **computationally expensive**. Including these higher auto-polynomial features when your original feature set end is large this really dramatically **blows up your feature space** and this doesn't seem like a good way to come up with additional features with which to build none many classifiers when n is large. (For many machine learning problems, n will be pretty large.)

One thing you could do is include only a subset of these, then the number of features is much smaller. But this is not enough features and certainly won't let you fit complext data sets . 

So, simple logistic regression together with adding in maybe the quadratic or the cubic features that's just not a good way to learn complex nonlinear hypotheses when n is large because you just end up with too many features. Neural Networks, turns out to be a much better way to learn **complex hypotheses, complex nonlinear hypotheses** even when your input feature space, even when n is large. 



**Neural Networks** 

Neural Networks are a pretty old algorithm that was originally motivated by the goal of having machines that can mimic the brain.



**Model Representation**

1. At a very simple level, neurons are basically computational units that take inputs (**dendrites**) as electrical inputs (called "spikes") that are channeled to outputs (**axons**). 
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/neuron-in-brain.png" alt="" width="346" data-align="center">

2. In our model, our dendrites are like the input features x1​⋯xn​, and the output is the result of our hypothesis function. 

3. In this model our x0​ input node is sometimes called the "bias unit." It is always equal to 1.

4.  In neural networks, we use the same logistic function as in classification, yet we sometimes call it a sigmoid (logistic) **activation** function.

5. In this situation, our "theta" parameters are sometimes called "weights".
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/neural-network-simple.png" alt="" width="196" data-align="center">

6. Our input nodes (layer 1), also known as the "input layer", go into another node (layer 2), which finally outputs the hypothesis function, known as the "output layer".

7. We can have intermediate layers of nodes between the input and output layers called the "hidden layers."We label these intermediate or "hidden" layer nodes ​ and call them "activation units."
   
   ![](https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/theta-activation.png)
   
   If we had one hidden layer, it would look like:
   
   <img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/activation-units.png" alt="" data-align="center" width="345">

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/calculate-activation.png" alt="" data-align="center" width="333">

        We can apply it with vectorized implementation :

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/vectorized-implemention.png" alt="" width="147" data-align="center">

       In other words, for layer j=2 and node k, the variable z will be:

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/z-implementation.png" alt="" width="283" data-align="center">

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/vectorized-implementation1.png" alt="" data-align="center" width="147">

        In summary :

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/summary1.png" alt="" data-align="center" width="102">

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/summary2.png" alt="" width="133" data-align="center">

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/summary3.png" alt="" width="169" data-align="center">

8. Each layer gets its own matrix of weights, Θ(j). The dimensions of these matrices of weights is determined as follows:
   
   ![](https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/theta-dimension.png)
   
   

**Examples of computing non liner function inputs using neural network**

Neural networks can also be used to simulate all logical gates.(you should set your first weigth(theta) values wisely)

- One hidden layer
  
  1. Predicting x1​ AND x2
  
  2. Predicting x1 OR x2
  
  3. Predicting (not x1) and (not x2)

- Multiple hidden layers
  
  1. predicting x1 XNOR x2

Use g(z) values from the image below :

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/g(Z).png" alt="" width="239" data-align="center">

**Multiclass classification**

To classify data into **multiple classes**, we let our **hypothesis function return a vector of values**. Say we wanted to classify our data into one of four categories. We can define our set of resulting classes as y :

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/multiclass-y.png" alt="" width="212" data-align="center">

The inner layers, each provide us with some new information which leads to our final hypothesis function. The setup looks like:

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/setup-multiclass.png" alt="" width="288" data-align="center">

Our resulting hypothesis for one set of inputs may look like:

<img title="" src="https://github.com/rojinakashefi/Intro-to-Artificial-Intelligence/blob/main/machine%20learning/week4/pictures/result-ex.png" alt="" width="170" data-align="center">


