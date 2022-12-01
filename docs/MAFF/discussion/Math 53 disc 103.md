# Lagrange Multipliers
Purpose: Find extreme values of the function $f(x,y,z)$ subject to the contraint curve $g(x,y,z)=k$. IN other words, find points on the set $g(x,y,z)=k$ for which $f(x,y,z)$ is an extreme. 

**Process**
1. Set $\nabla f = \lambda \nabla g$ .
This gives a set of equations for $x,y,z,\lambda$
2. Add the constraint equation:
	1. $g(x,y,z)=k$
3. Solve the above equations for $x,y,z$ 

It is *really important* to know how to solve the problem conceptually

The following are equivalent:
- $\nabla f = \lambda \nabla g$ 
- $\nabla f$ and $\nabla g$ are the same up to scaling, up to some scalar $\lambda$
- Level set of $f$ and $g$ have the same tangent plane at some point $P$
	- because the tangent planes have the same normal vector $\nabla f$ and $\nabla g$ up to scaling.

Tangent plane ot the constraint $g(x,y,z) = k$

If tangent planes cut, then basically you can go through the direction of the tangent plane of the constraint curve $g(x,y,z)=c$ The tangent plane of the constraint curve **cuts through** the level sets of $f(x,y,z)$ As you travel along that direction (some direction perpendicular to the gradient vector of g) , the answer obtained on the $f(x,y,z)$ curve can change, whether increase or decrease(depending on the side fo the tangent plane you are traveling). So, we see that in this situation, the point on $f(x,y,z)$ is not an extreme point

![[WhatsApp Image 2022-10-03 at 10.35.15 AM.jpeg]]

It is possible that $\lambda$ is $0$, which is a degenerate case. Basically it means that the constraint curve intersects the curve we wanna find max min for, $f(x,y,z)$, literally at the critical point of $f(x,y,z)$, so a potential local or global max min of $f(x,y,z)$. 
- It is a weird case but usually when I solve problems I neglect the $\lambda=0$ case

![[WhatsApp Image 2022-10-03 at 10.40.02 AM.jpeg]]

Sign of $\lambda$ cannot tell or inform of whether or not the curve is a maximum or minimum, as the constraint function $g(x,y,z)$ is not given, and $\nabla g$ can point in any direction

*Problem:*
Maximize/minimize $f(x,y,z) = e^{xyz}$ subject to constraint $2x^2+y^2+z^2=24$

$\nabla f = <yz\times e^{xyz},xz\times e^{xyz},xy\times e^{xyz}>$
$\nabla g = <4x,2y,2z>$

$yz\times e^{xyz}=\lambda 4x$
$xz\times e^{xyz}=\lambda 2y$
$xy\times e^{xyz}=\lambda 2z$
$2x^2+y^2+z^2=24$




