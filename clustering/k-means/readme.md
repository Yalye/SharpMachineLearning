
### what is k-means clustering?
K-means clustering is a method of prototype based clustering, it can group the data into k clusters in which eash data belongs to the cluster with the nearest mean.

Given the input data set $D = \left\{ \boldsymbol { x } _ { 1 } , \boldsymbol { x } _ { 2 } , \ldots , \boldsymbol { x } _ { m } \right\}$, k-means clustering will partition the $n$ observations into $k ( \leqslant m )$ set $\mathrm { S } = \left\{ S _ { 1 } , S _ { 2 } , \ldots , S _ { k } \right\}$ so as to minimize the within-cluster sum of squares.

$$
\underset { \mathbf { S } } { \arg \min } \sum _ { i = 1 } ^ { k } \sum _ { \mathbf { x } \in S _ { i } } \left\| \mathbf { x } - \boldsymbol { \mu } _ { i } \right\| ^ { 2 }
$$
where $u_{i}$ is the mean of points in $S _ { i }$.

### clustering steps
 * select $k$ random points as the class center point
 * calculate the distance between each data point and the each class center point, then classify the data point to be in the group whose center point is closest to it.
 * recompute each class center to the mean of all the vectors in the class.
 * repeat the above steps for some iterations or until the centers don't change much between iterations.

### References
https://en.wikipedia.org/wiki/K-means_clustering
https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68