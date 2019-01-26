
The beta distribution is distribution of probabilities.

$$
\operatorname { Beta } ( \mu | a , b ) = \frac { \Gamma ( a + b ) } { \Gamma ( a ) \Gamma ( b ) } \mu ^ { a - 1 } ( 1 - \mu ) ^ { b - 1 }
$$
where the $\Gamma$ is the gamma function：$\Gamma ( n ) = ( n - 1 ) !$

### It's normalized
verification:
to verify it's normalized, i.e. 

$$
\int _ { 0 } ^ { 1 } Beta(\mu|a, b)  d\mu = 1
$$
so, 
$$
\int _ { 0 } ^ { 1 } \mu ^ { a - 1 } ( 1 - \mu ) ^ { b - 1 } \mathrm { d } \mu = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}
$$
that's what we want to derive. <br>


$$
\begin{aligned} \Gamma ( a ) \Gamma ( b ) & = \int _ { 0 } ^ { \infty } e ^ {- x } x ^ { a - 1 } d x \int _ { 0 } ^ { \infty } e ^ {- y } y ^ { b - 1 } d y \\ & = \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } e ^{ - x } x ^ { a - 1 } e^ { - y } y ^ { b - 1 } d x d y \\ & = \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } e ^ { - t } x ^ { a - 1 } ( t - x ) ^ { b - 1 } d t d x \\ &\\ & \stackrel{t=x + y}{=}  \int _ { 0 } ^ { \infty } e^ {- t } \left( \int _ { 0 } ^ { t } x ^ { a - 1 } ( t - x ) ^ { b - 1 } \mathrm { d } x \right) \mathrm { d } t  \\ & \stackrel{x=\mu t}{=}   \int_{0}^{\infty} e^{-t}\left( \int_{0} ^{t} {(\mu t)}^{a-1}{(t - \mu t)}^{b-1} \mathrm{d}x\right) \mathrm{d}t \\&= \int_{0}^{\infty} e^{-t}\left( {( t)}^{a + b -1} \int_{0} ^{t} {(\mu)}^{a-1}{(1 - \mu)}^{b-1} \mathrm{d}\mu\right) \mathrm{d}t
\\&=\int _ { 0 } ^ { \infty } t ^ { a + b - 1 } \mathrm { e } ^ { - t } \mathrm { d } t \cdot \int _ { 0 } ^ { 1 } \mu ^ { a - 1 } ( 1 - \mu ) ^ { b - 1 } \mathrm { d } \mu \\&= \Gamma(a+b) \int _ { 0 } ^ { 1 } \mu ^ { a - 1 } ( 1 - \mu ) ^ { b - 1 } \mathrm { d } \mu \end{aligned} 
$$
so, the beta distribution is normalized.

### Beta distribution's mean is $\frac { a } { a + b }$
verification:

$$
\begin{aligned}\mathrm {E}[X] &= \int_{-\infty}^{\infty}\mu\operatorname{Beta}(\mu|a,b)d\mu \\ &= \int_{-\infty}^{\infty}\mu \frac { \Gamma ( a + b ) } { \Gamma ( a ) \Gamma ( b ) }\mu ^ { a - 1 } ( 1 - \mu ) ^ { b - 1 }d\mu \\&=\frac { \Gamma ( a + b ) } { \Gamma ( a ) \Gamma ( b ) }\int_{0}^{1} \mu^{(a + 1 -1)}(1-\mu)^{b-1}d\mu \\&= \frac { \Gamma ( a + b ) } { \Gamma ( a ) \Gamma ( b ) } \frac { \Gamma ( a + 1) \Gamma ( b ) }{ \Gamma ( a + b + 1) } \int_{0}^{1}\operatorname {Beta}(\mu|a+1,b)d\mu\\&=\frac { \Gamma ( a + b )\Gamma ( a + 1 ) }{\Gamma ( a )\Gamma ( a + b + 1)}\\&=\frac{a}{a+b}
\end{aligned}
$$
### Beta distribution's variance is $\frac { a b } { ( a + b ) ^ { 2 } ( a + b + 1 ) }$
verification:

$$
\begin{aligned}\mathrm {E}[X^{2}] &= \int_{-\infty}^{\infty}\mu^{2}\operatorname{Beta}(\mu|a,b)d\mu \\ &= \int_{-\infty}^{\infty}\mu^{2} \frac { \Gamma ( a + b ) } { \Gamma ( a ) \Gamma ( b ) }\mu ^ { a - 1 } ( 1 - \mu ) ^ { b - 1 }d\mu\\&=\frac { \Gamma ( a + b ) } { \Gamma ( a ) \Gamma ( b ) }\int_{0}^{1} \mu^{(a + 2 -1)}(1-\mu)^{b-1}d\mu \\&=\frac { \Gamma ( a + b ) } { \Gamma ( a ) \Gamma ( b ) } \frac { \Gamma ( a + 2) \Gamma ( b ) }{ \Gamma ( a + b + 2) } \\&=\frac{(a+1)a}{(a+b+1)(a+b)}\end{aligned}
$$

$$
\begin{aligned}{\mathrm {E}[X]}^{2} &= {\left(\frac{a}{a+b}\right)}^2 \end{aligned}
$$

$$
\begin{aligned} \mathrm Var[X] &= \mathrm {E}[X^{2}] - {\mathrm {E}[X]}^{2} \\&=\frac { a b } { ( a + b ) ^ { 2 } ( a + b + 1 ) }\end{aligned}
$$

### Ref
https://stats.stackexchange.com/questions/47771/what-is-the-intuition-behind-beta-distribution <br>
http://rads.stackoverflow.com/amzn/click/0387310738