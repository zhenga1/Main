#r/discussion
- Discussion notes: link

# Discussion 10 /21
```jupyter
print("Hello world i am so incredibly cool")
```

If we have $R$ is the region bounded by:
$y = x^2-5x,y=x^2-5x+3,y=x+2,y=x-3$
$u = y-x^2+5x=0$
$y-x^2+5x=3$
$v = y-x = 2$
$y-x = -3$
In $uv$ space, $R'$ is the rectangle bounded by 
$u=0,u=3,v=2,v=-3$ 
So if we compute:
$\int\int_R (x-y)dxdy=\int\int_{R'}(-v)|detJ|dudv$
We first solve for 
$$detJ=\begin{bmatrix}\frac{\partial x}{\partial u}&&\frac{\partial x}{\partial 
 v} \\ \frac{\partial x}{\partial u}&&\frac{\partial x}{\partial 
 v}\end{bmatrix} $$
$\int\int\int_E dV=\int\int\int_{unit sphere}|det J|dudvdw$
$=\int\int\int_{unit sphere}abc dudvdw$ 
-> This can be changed to spherical coordinates
$=\int_0^{\pi}\int_0^{2\pi}\int_0^2abc (\rho)^2\sin(\phi)d\rho d\theta d\phi$ 
Determinant of an inverse matrix is the inverse of the determinant in the Jacobian thing


