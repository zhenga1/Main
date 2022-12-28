# Banchoff-Chmutov surfaces
[Link](https://math.stackexchange.com/questions/46212/interesting-implicit-surfaces-in-mathbbr3):

#  Goursat Tangles
[Link:](https://mathworld.wolfram.com/Tanglecube.html)

# Torus
![[Pasted image 20221002144658.png]]
Basically a circle(crossection) rotated around another circle, which is in the plane perpendicular to the first circle
[Parameterization of a torus:](https://www.youtube.com/watch?v=heFhbV5J_bY)

![[chrome_60wOqM2G3g.png]]
Let green vector above be $\vec{p} = <R\cos(\theta), R\sin(\theta),0>$ , and let the two orthogonal purple vectors be unit vectors $\vec{v_1}, \vec{v_2}$ such that:
$\vec{v_1} = <\cos(\theta), \sin(\theta),0>$
$\vec{v_2} = <0,0,1>$

We see that each point $P$ on the reddish pink curve can be uniquely defined as a parametric equation defined by the changing variables $\phi$ and $\theta$, as such:
$\vec{P} = \vec{p} + r\cos{\phi}\times \vec{v_1} + r\sin{\phi}\times \vec{v_2}$

So, the parametric equation of a torus is:
$x = R\cos(\theta) + r\cos(\phi)\cos(\theta)$ 
$y = R\sin(\theta) + r\cos(\phi)\sin(\theta)$ 
$z = r\sin(\phi)$ 

So we have sets of parametic equations that form a projection/bijection from $(\theta,\phi)$ to $(x,y,z)$ . We see that
$0\leq \theta \leq 2\pi$
$0\leq \phi \leq 2\pi$