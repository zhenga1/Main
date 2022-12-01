1. $\vec{F}$ is conservative
2. $\vec{F}$ is a gradient vector field
3. $\vec{F}(x,y)=\nabla f(x,y)$ for some function $f(x,y)$
4. $\int_{C_1} \vec{F}d\vec{r} = \int_{C_2} \vec{F}d\vec{r}$, whenever $C_1,C_2$ have the same start/endpoints. 
	1. the notion of (**path independence**)
5. $\int_C \vec{F} d\vec{r}=0$ whenever $C$ is a closed curve (loop)
All of the above conditions imply that if we have;
$\vec{F}(x,y) = <P(x,y),Q(x,y)>=<\frac{\partial F}{\partial x},\frac{\partial F}{\partial y}>$
Then we have:
6. $\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$, and we have:
$$\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y}$$
(6) is the same thing as (1)-(5) on nice regions

![[WhatsApp Image 2022-10-28 at 10.34.22 AM.jpeg]]
Let $f(0,0) = 0$ 
Define $f(a,b)$ to be:
- $\int_C \vec{F} d\vec{r}$  where $C$ is a path from $(0,0)$ to $(a,b)$

We have that:
If $(1)-(5)$ are true for $\vec{F}$ , then
$$\int_C \vec{F}\cdot d\vec{r} = f(final pt)-f(initial pt)$$
where we have $f$ is simply the function that creates the graddient field

![[WhatsApp Image 2022-10-28 at 10.41.25 AM.jpeg]]
$\vec{F} = <3+2xy, x^2-3y^2>$ 
a) Show $F$ is conservative
b) Use that to find $\int_C \vec{F} d\vec{r}$, where $C$ is the upper-half of ellipse:
		$\frac{x^2}{4} + y^2=1$

We let:
$3+2xy = f_x(x,y)$ for some $f(x,y)$ 
So we have:
$f(x,y) = 3x+x^2y+k$ Now we have
$f_y(x,y) = x^2 + dk/dy = x^2 - 3y^2$
So $k = -y^3+C$, where $C\in R$ is some constant
So, hence we have:
$f(x,y) = 3x+x^2y-y^3+C$

*First Method:*
$\frac{\partial P}{\partial y} = 2x, \frac{\partial Q}{\partial x} = 2x$, This tells us $R^2$ is simply connected
*Second Method:*
$f(x,y) = 3x+x^2y+C(y)$

![[WhatsApp Image 2022-10-28 at 10.57.08 AM.jpeg]]
![[WhatsApp Image 2022-10-28 at 10.57.08 AM (1).jpeg]]

![[chrome_UfzBEwocyi.png]]





