
### Validation Approaches
Popular validation approaches involve **Internal evaluation**, **External evaluation**, **Manual evaluation** and **Indirect evaluation**.

### Internal evaluation
Internal evaluation means the clustering result is evaluated based on the data that was clustered itself. With this evaluation, we get the algorithm, which produces clusters with high similarity within a cluster and low similarity between clusters. Also, this evaluation is biased towards algorithms that use the same cluster model.
the following methods are some popular internal evaluation methods:
 * Davies-Bouldin index (DB index or DBI). 

$$
D B = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \max _ { j \neq i } \left( \frac { \sigma _ { i } + \sigma _ { j } } { d \left( c _ { i } , c _ { j } \right) } \right)
$$
  where $n$ is the number of clusters, $c_{x}$ is the centroid of cluster $x$, $ \sigma _{x}$ is the average distance of all elements in cluster $x$ to centroid $c_{x}$, and $d(c_{i},c_{j})$ is the distance between centroids $c_{i}$ and $c_{j}$. 
  
  * Dunn index (DI)
  
$$
D = \frac { \min _ { 1 \leq i < j \leq n } d ( i , j ) } { \max _ { 1 \leq k \leq n } d ^ { \prime } ( k ) }
$$

### External evaluation
$TP$ is the number of true positives, $TN$ is the number of true negatives, $FP$ is the number of false positives, and $FN$ is the number of false negatives.
 * Jaccard index
$$
J ( A , B ) = \frac { | A \cap B | } { | A \cup B | } = \frac { T P } { T P + F P + F N }
$$
 * Fowlkes–Mallows index

$$
FM = \sqrt { \frac { T P } { T P + F P } \cdot \frac { T P } { T P + F N } }
$$

### References
[Wikipedia](https://en.wikipedia.org/wiki/Cluster_analysis)