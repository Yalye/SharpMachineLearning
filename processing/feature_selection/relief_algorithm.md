
Relief algorithm is an algorithm of feature selection.

suppose we have a data set with the count of $n$ and $p$ features, each feature is scaled to the interval [0,1] (0 and 1 for binary data), and the data set belongs to two known classes.

for the $j$ th feature, we calculate the weight for the feature by the following:

$$
\delta ^ { j } = \sum _ { i } - \operatorname { diff } \left( x _ { i } ^ { j } , x _ { i , \mathrm { nearhit } } ^ { j } \right) ^ { 2 } + \operatorname { diff } \left( x _ { i } ^ { j } , x _ { i , \mathrm { nearmiss } } ^ { j } \right) ^ { 2 }
$$
where $x _ { i , \mathrm { nearhit }} ^ { j }$ is the closest instance belonging to the same class of instance $i$, and $x _ { i , \mathrm { nearmiss }} ^ { j }$ is the closest instance belonging to the different class of instance $i$. the feature weight bigger than a threshold is **relevant feature**.