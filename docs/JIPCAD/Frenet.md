[Super dope link explaining the concepts](https://www.youtube.com/watch?v=VIqA8U9ozIA)

For straight line described by parametric equation:
$r(x(t),y(t),z(t))$ for time $t$, we must have that:

1. Tangent vector(unit vector) $\vec{T} = \frac{\partial r}{\partial s}$ 
[Reason](https://web.mit.edu/hyperbook/Patrikalakis-Maekawa-Cho/node22.html):
	![[chrome_D5bA7KF4M1.png]]
	![[nn78KDv89S.png]]
	![[chrome_3nAuN1XpdU.png]]
	

2. Normal vector = $\vec{N} = \frac{\partial T}{\partial s}$
- Tells how normal vector itself is changing
- Always pointing towards center of circle(assuming that the path is a circle and the point is moving along the circle at fixed speed)

3. Binormal vector $\vec{B}=\vec{T} \times \vec{N}$
- Must be the normal vector to the plane created by the normal vector and tangent vector

- Tangent + Normal vectors is twisting as you go around a 3 Dimensional curve

Question: What does $\vec{B}$ tell us exactly?
$\frac{\partial B}{\partial s} = \frac{\partial TN}{\partial s} = N\frac{\partial T}{\partial s} + T\frac{\partial N}{\partial s}$
$=N\times N + T\frac{\partial N}{\partial s} = T\frac{\partial N}{\partial s}$
![[chrome_8HZg4FHGnw.png]]
![[chrome_tIY2GKkr9j.png]]
![[chrome_tsBL3tea8K.png]]

# Frenet Frame
Basically it is the moving right hand coordinate system defined by vectors $[T,N,B]$, each of them unit vectors, and each of them orthogonal to each other, oriented just like the vectors $[i,j,k]$  This coordinate system is made up of the Tangent vector, the Normal vector and the Binormal vector, and changes depending on the time $t$ of the moving particles path along any given path $r(t)$ 

Assembly: 
Is it possible?



