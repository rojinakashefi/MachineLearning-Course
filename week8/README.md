# Week 8

#### **Clustering**

It is an unsupervised learning and we will try to find a structure within a given data so it will find clusters thats why we call it clustering algorithm. ( we have more algorithms than clusters which find structure in a data. )

#### **K-Means Algorithm**

**Separated Clusters**

This algorithm is the most used algorithm in clurstering algorithms.

1. Randomly initialize K points (number of clusters) called cluster centroids.

2. Cluster assignment step :
   
   Going through each of the examples depending on whether it's closer to the fisrt cluster centroid or the second cluster centroid, it is going to assign each of the data points to one of the two cluster centroids.
   
   we want to **find a k** which minimize to distance between our training example and our cluster centroids.
   
   <img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/cluster-assignment-1.png" alt="" width="194">
   
   Its applying cost function with respect to c(i) in this step.

3. Move centroid step :
   
   We are going to move cluster centroids to the average of the points colored the same colour (assigned to same cluster).
   
   If there is a cluster centroids which no point has been assigned to it its better to eliminate that  and have K-1 cluster centroids. or you can randomly reinitialize that cluster.
   
   Its applying cost function with respect to m(i) in this step.

We loop through second and third step.

**Non-Separated Clusters**

Run the k means clustering algorithm on the data set so we can get separated clusters.

#### **Cost function of K means algorithm**

- C(i) = index of cluster to which example x(i) is currently assigned

- M(k) = cluster centroid k

- Mc(i) = cluster centroid of cluster to which example x(i) has been assigned
  
  ![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/cost-func.png)

#### **Random Initalization K-mean**

- K ( number of cluster centroid ) < m ( number of training example )

- **Randomly pich K training examples and set m(i) equal to these K examples**.

With different randomly initialization we can have different solutions and end up at local optima. So we can try multiple randomly initialization and pick that gave the lowest cost.

If **K is small** so we have small number of cluster centroid its **more useful using multiple random initalization** than when K is big.

#### **Choosing the number of clusters**

**Elbow method**

We are going to run cost function with different number of clusters.

<img title="" src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/ellbow-method.png" alt="" width="177">

But the curve is usally more ambigious and there is no fixed elbow number.

There is another was when you run k-means to get clusters to use fot later purposes and evaluate k-means based on a metric for how well it performs for that later purpose.

#### **Dimensionality Reduction**

Needing smaller dimension for presenting our data set and make our learning algorithm run more quickly. we use **projection** on our data to put it in new dimension.

#### **Principal Component Analysis**

PCA  tries to find a lower dimensional surface, onto which to project the data so that the sum of squares of the projection error is minimized. 

If we are going to reduce n-dimension to k-dimensional we need to find k vectors and project the data onto the linear subspace spanned by this set of k vectors.

**PCA is not linear regression**

The left picture is linear regression which shows different between hypothesis value and real value and the right picture shows the projection error .

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/pca-not-lr.png" title="" alt="" width="312">

In linear regression we want to predict y.

In pca we want to find features.

#### **PCA Steps**

1. Preproccesing (Feature scaling/mean normalization)
   
   <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/mean-normalization.png" title="" alt="" width="221">
   
   <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/feature-scaling.png" title="" alt="" width="220">

2. Compute covariance matrix and eigen vectors
   
   <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/eigen-vector.png" title="" alt="" width="260">
   
   <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/u-matrix.png" title="" alt="" width="261">
   
   If we want to reduce to k dimensional we only take u(1)
   
   to u(k) column.

3. Compute Z where we want to project our data onto.
   
   <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/z-matrix.png" title="" alt="" width="349">

#### **Reconstruction from compressed Representation**

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/Reconstruction.png" title="" alt="" width="284">

#### **Choosing the number of principle components**

- Average squared projection error
  
  <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/average-squared.png" title="" alt="" width="225">

- Total variation in the data
  
  <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/variation.png" title="" alt="" width="191">

- Choose k to be smallest value which 99 of variance is retained
  
  <img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/choose-k.png" title="" alt="" width="241">

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/choosing-k.png" title="" alt="" width="250">

Another way is use different number of k until we reach >= 0.99:

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/s-matrix.png" title="" alt="" width="193">

<img src="https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week8/choosing-k-second.png" title="" alt="" width="202">

Mapping X(i) -> Z(i) should be defined by **running PCA only on the training set**. 

After **finidng parameters** such as U reduced we can apply it as well to the examples Xcv(i) and Xtest(i) in the cross validation and test sets.

If we are having overfitting it **isnt** a good idea to use **PCA** and its **better** to use **regularization** term
