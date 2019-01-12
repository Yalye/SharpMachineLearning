
### what is hierarchical clustering ?
hierarchical clustering is a method of clustering, the strategies for it generally fall into two types:
 * Agglomerative. It's a **bottom-up** algorithm. it treat each data point as a single cluster at the outset, then merge pairs of clusters until all clusters have been merged into a single cluster that contains all data points. the hierarchy of clusters is represented as a tree.
 * Divisive. It's a **top-down** clustering method. we start with all documents in one cluster, then split using a flat clustering algorithm. repeat the step until each point is in a single cluster.
 
### How does agglomerative hierarchical clustering work?
 * 1. in the beginning, we treat each point as a single cluster.
 * 2. calculate a distance metric that measures the distance between every two clusters. we can use **average linkage** as the measurement.
 * 3. combine two clusters having the smallest distance in the distance metric into one cluster.
 * 4. repeat step 2 and 3 until there is only one cluster containing all the data points. In this way we can get how many clusters we want simply by choosing when to stop combining the clusters.
 

### References
https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68
