Announcements:
- last time:
	- Tomography
	- Linear Equations

- Today
	- Solving sets of linear equations 
		Gaussian Elimination
	- Vectors

Gaussian elimination

What is linear algebra:
- The study of linear functions and linear equations, typically using
vectors and matrices
- Linearity is not always applicable, but can be a good first-order
approximation
• There exist good fast algorithms to solve these problems

Linear Equations f is linear if it is:
	(1) Homogeneity:
	$f(ax) = af(x)$
	(2) Superposition (distributivity): if
	$x=y+z$, then
	$f(y+z) = f(y)+f(z)$

For square functions like $f(x) = ax^2$, homogeneity does not hold as f$(ax) = a^2(f(x))$ and as a result, $a*f(x)$ not equal to $f(ax)$. Homogeneity does not hold.

$f(y+z) = b(y+z)^2$
$f(y) + f(z) = by^2 + bz^2$

$f(x) = b^2x$-> this is linear
$f(ax) = b^2ax = af(x) = a*b^2x$
$f(y+z) = b^2y + b^2z$
$f(y) + f(z) = b^2y + b^2z$ 

$f(x) = ax+d$ -> its called an affine function

Linear Equations
- Definition:
Consider $f(x_1,x_2,...,x_N), (x_1,x_2,...,x_N) \in R^n$ 

$f$ is linear if the following identity holds:
1. Homogeneity:
	$f(ax_1,...,ax_N) = a\times (f(x_1,...,x_N)$
2. Superposition:
	$$f(y_1+z_1,y_2+z_2, ... y_n+z_n)$$$$ = f(y_1,y_2,y_3,...,y_n) + f(z_1,z_2,z_3,...,z_n)$$

Consider the set of M linear equations with N variables:
	$a_{11}\times x_1 + a_{12}\times x_2 + ... + a_{1N}\times x_N = b_1$
	$a_{21}\times x_1 + a_{22}\times x_2 + ... + a_{2N}\times x_N = b_2$
	...
	$a_{M1}\times x_1 + a_{M2}\times x_2 + ... + a_{MN}\times x_N = b_M$

$$\begin{bmatrix}1 &&1 &&0 &&0 		&&	4\\
0&& 0&& 1&& 1 &&			3\\
1 &&0 &&1 &&0		&&		2\\
0&& 1&& 0 &&1		&&		5\\ \sqrt2&& 0&& 0 &&\sqrt2		&&3\sqrt2\end{bmatrix}
$$

Back to tomography
How do we systematically solve it?
Basically computers would solve it, but in the past the computers were human


Algorithm for solving linear equations
- Three basic operations that don't change a solution:
	1. Multiply an equation with nonzero scalar
		$2x+3y = 4$ has same solution as $4x+6y=8$
Concept of proof: Look at explicit solution, show that they are the same (next time) .
 Also show the reverse - by applyign the reverse operations
	2. Adding a scalar constant multiple of one equation to another.

Upper triangular systems
- Consider following equations


$$x-y+2z = 1
\\
y-z=2 
\\
z=1$$
why are they esier to solve, because of the row echolon form. 


