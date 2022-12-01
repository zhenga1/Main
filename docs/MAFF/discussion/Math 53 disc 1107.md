#r/discussion
- Discussion notes: link

# Discussion 11 / 07
```jupyter
print("Hello world i am so incredibly cool")
```
In $R^3$

There are many types of functions:WE have 

functions $\rightarrow$ vector fields:
	(example $f \rightarrow \nabla f$)
vector fields $\rightarrow$ vector fields:
	(example $\vec{F} \rightarrow$ curl $\vec{F}$)
vector fields $\rightarrow$ functions
	(example $\vec{G} \rightarrow$ div $\vec{G}$ )

So, then if $\vec{F} = <P(x,yz),Q(x,y,z),R(x,y,z)>$
curl $\vec{F} = \nabla \times \vec{F} = \begin{bmatrix}i && j && k \\ \frac{d}{dx} && \frac{d}{dy} && \frac{d}{dz} \\ P && Q && R \end{bmatrix}$

div $\vec{F} = \nabla \cdot \vec{F} = <\frac{d}{dx},\frac{d}{dy}, \frac{d}{dz}> \cdot <P,Q,R>$
$= \frac{dP}{dx} + \frac{dQ}{dy} + \frac{dR}{dz}$


We have the **==Fundamental Theorem of line integrals==**. 
$f(b) - f(a) = \int_C \nabla f \cdot d\vec{r}$

Now we can introduce ==**Stokes' theorem**==
$$\int_{\partial s} \vec{F} d\vec{r} = \int_S \int curl \vec{F} \cdot d\vec{A}$$
And the ==**Divergence Theorem**==
$$\int \int_{\partial R} \vec{G} d\vec{A} = \int_R \int \int div \vec{G} dV$$
Essentially this is just the equivalence of **Fundamental theorem of Line integrals** but for higher dimensions.  You can go up even further to dimensions greater than $R^4$.

By **Clarinaut's** Theorems:
$curl (\nabla f) = 0$
$div (curl \vec{F}) = 0$

Proof: 
$curl(\nabla F) = curl <\frac{df}{dx},\frac{df}{dy}, \frac{df}{dz}>$
$=<\frac{d^2f}{dydz}-\frac{d^2f}{dzdy}, \frac{d^2f}{dxdz}-\frac{d^2f}{dzdx}, \frac{d^2f}{dxdy} - \frac{d^2f}{dydx}>$

***Divergence*** of a vector field measures how much the vector field is spreading out at each point.
***Curl*** of a vector field measures how much the vector fields is curling and around which axis. 
![[WhatsApp Image 2022-11-07 at 10.40.26 AM.jpeg]]

$\vec{F} (x,y,z) = <y^2z^3,2xyz^3, 3xy^2z^2>$
Question: Determine whether or not it is conservative and if so find $f$ so that $\vec{F} = \nabla f$
curl $\vec{F} = <6xyz^2-6xyz^2, 3y^2z^2 - 3y^2z^2, 2yz^3 - 2yz^3>=<0,0,0>$



