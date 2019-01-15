
### What is likelihood function ?
I like [the answer on stackexchange](https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability)<br>
Likelihood function is a function of the parameters of a statistical model, it describes the plausibility of a parameter value of the statistical model assumed to describe the observed data, given specific observed data. it's always defined as a function of $\theta$.
For discrete probability distribution, 

$$
\mathcal { L } ( \theta | x ) = p _ { \theta } ( x ) = P _ { \theta } ( X = x )
$$
the likelihood function of $\theta$ equals to the probability of $ X = x$ given the value of $\theta$. <br>
For continuous probability distribution,

$$
\mathcal { L } ( \theta | x ) = f _ { \theta } ( x )
$$
the likelihood function of $\theta$ equals to the density function of $X = x$ given the value of $\theta$. <br>

### Maximum likelihood estimation

Maximum likelihood estimation (MLE) is a method of finding the parameters values that maximize the likelihood function. <br>
For likelihood function$\mathcal { L } ( \theta ; x )$, MLE will find the parameter $\theta$ to maximize $\mathcal{L (\theta; x)}$:

$$
\hat { \theta } \in \{ \underset { \theta \in \Theta } { \arg \max } \mathcal { L } ( \theta ; x ) \}
$$
Sometime, we transform the likelihood function with natural logarithm, for log is a strictly increasing function, we call the transformed function **log-likelihood** ($\ell ( \theta ; x ) = \ln \mathcal { L } ( \theta ; x )$) or **average log-likelihood**($\hat { \ell } ( \theta ; x ) = \frac { 1 } { n } \ln \mathcal { L } ( \theta ; x )$)

If data is independent and identically distributed, the average log-likedlihood turns to

$$
\hat { \ell } ( \theta ; x ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ln f \left( x _ { i } | \theta \right)
$$

### References
https://en.wikipedia.org/wiki/Maximum_likelihood_estimation<br>
https://towardsdatascience.com/probability-concepts-explained-maximum-likelihood-estimation-c7b4342fdbb1 <br>
[answer on stackexchange](https://stats.stackexchange.com/questions/2641/what-is-the-difference-between-likelihood-and-probability)
