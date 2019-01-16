
### Bernoulli distribution
Bernoulli distribution is the discrete probability distribution of a random variable which takes the value 1 with probability $u$ and the value 0 with probability $v = 1-u$. i.e.
$p ( x = 1 | \mu ) = \mu$ where $0 \leqslant \mu \leqslant 1$, and from that we get $v = p(x=0|\mu) = 1-\mu$. so the probability distribution over $x$ can be writter in the following form:

$$
\operatorname { Bern } ( x | \mu ) = \mu ^ { x } ( 1 - \mu ) ^ { 1 - x }
$$
this is the Bernoulli distribution.

### mean of Bernoulli distribution is $\mathbb { E } [ x ] = \mu$
Verification:

$$
\mathbb {E}[x] = p(x=1|\mu) * 1 + p(x = 0|\mu) * 0 = \mu * 1 + v * 0 = \mu
$$

### variance of Bernoulli distribution is $\operatorname { var } [ x ] = \mu ( 1 - \mu )$
Verification:

$$
\mathbb { E } \left[ x ^ { 2 } \right] = p(x=1|\mu) * 1^{2} + p(x = 0|\mu) * 0^{2} = \mu * 1 + v * 0 = \mu

\operatorname {var}[x] = \mathbb { E } \left[ x ^ { 2 } \right] - \mathbb { E } [ x ] ^ { 2 } = \mu - \mu^{2} = \mu(1-\mu)
$$

