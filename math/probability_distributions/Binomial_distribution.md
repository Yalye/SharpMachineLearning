
Binomial distribution:

$$
\operatorname { Bin } ( m | N , \mu ) = \left( \begin{array} { c } { N } \\ { m } \end{array} \right) \mu ^ { m } ( 1 - \mu ) ^ { N - m }
$$
$$
\left( \begin{array} { l } { N } \\ { m } \end{array} \right) \equiv \frac { N ! } { ( N - m ) ! m ! }
$$
where m is the number of observations of $x = 1$, $N$ is the data set size, $\mu$ is the probability of a random variable being $x=1$.
the mean of binomial distribution:

$$
\mathbb { E } [ X ] \equiv \sum _ { m = 0 } ^ { N } m \operatorname { Bin } ( m | N , \mu ) = N \mu
$$
verification:

$$
\begin{aligned} \mathbb { E } ( X ) & = \sum _ { m = 0 } ^ { N } m \left( \begin{array} { c } { N } \\ { m } \end{array} \right) \mu ^ { m } ( 1 - \mu ) ^ { N - m } \\ & = \sum _ { m = 0 } ^ { N } m \frac { N ! } { m ! ( N - m ) ! } \mu ^ { m } ( 1 - \mu ) ^ { N - m } \\ & = \sum _ { m = 1 } ^ { N } \frac { N ! } { ( m - 1 ) ! ( N - m ) ! } \mu ^ { m } ( 1 - \mu ) ^ { N - m } \end{aligned}
$$
let $y = m - 1$ and t = N -1, we get

$$
\begin{aligned} \mathbb { E } ( X ) & = \sum _ { y = 0 } ^ { t } \frac { ( t + 1 ) ! } { y ! ( t - y ) ! } \mu ^ { y + 1 } ( 1 - \mu ) ^ { t - y } \\ & = ( t + 1 ) \mu \sum _ { y = 0 } ^ { t } \frac { t ! } { y ! ( t - y ) ! } \mu ^ { y } ( 1 - \mu ) ^ { t - y } \\ & = N \mu \sum _ { y = 0 } ^ { t } \frac { t ! } { y ! ( t - y ) ! } \mu ^ { y } ( 1 - \mu ) ^ { t - y } \end{aligned}
$$
let $a = \mu$ and $ b = 1 - \mu$.

$$
\mathbb { E } ( X ) = N \mu \sum _ { y = 0 } ^ { t } \frac { t ! } { y ! ( t - y ) ! } \mu ^ { y } ( 1 - \mu ) ^ { t - y } = N\mu (a + b)^{t} = N\mu(\mu + 1 - \mu)^{t} = N\mu
$$

the mean of binomial distribution is:

$$
\operatorname { var } [ X ] \equiv \sum _ { m = 0 } ^ { N } ( m - \mathbb { E } [ m ] ) ^ { 2 } \operatorname { Bin } ( m | N , \mu ) = N \mu ( 1 - \mu )
$$
verification:

$$
\begin{aligned} 
\operatorname { var } [ X ] & = E \left( X ^ { 2 } \right) - E ( X ) ^ { 2 } \\ &= E ( X ( X - 1 ) ) + E ( X ) - E ( X ) ^ { 2 } \\&  = \sum _ { m = 0 } ^ { N } m ( m - 1 ) \left( \begin{array} { l } { N } \\ { m } \end{array} \right) \mu ^ { m } ( 1 - \mu ) ^ { N - m }  + N\mu - (N\mu)^{2} \\&  = \sum _ { m = 0 } ^ { N } m ( m - 1 ) \frac { N ! } { m ! ( N - m ) ! } \mu ^ { m } ( 1 - \mu ) ^ { N - m } + N\mu - (N\mu)^{2}\\&= \sum _ { m = 2 } ^ { N } \frac { N ! } { ( m - 2 ) ! ( N - m ) ! } \mu ^ { m } ( 1 - \mu ) ^ { N - m } + N\mu - (N\mu)^{2}\\&= N ( N - 1 ) \mu ^ { 2 } \sum _ { y = 2 } ^ { N } \frac { ( t - 2 ) ! } { ( y - 2 ) ! ( N - y ) ! } \mu ^ { y - 2 } ( 1 - \mu ) ^ { N - y } + N\mu - (N\mu)^{2}\\&= N ( N - 1 ) \mu ^ { 2 } ( \mu + ( 1 - \mu ) ) ^ { t } + N\mu - (N\mu)^{2}\\&=N(N-1)\mu^{2} + N\mu - (N\mu)^{2} \\&= N\mu(1-\mu)
\end{aligned}
$$
