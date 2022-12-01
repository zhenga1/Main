**Euclidean Inner product**:
- Given $\vec{x}, \vec{y} \in R^n$ 
- $<\vec{x},\vec{y}> = x^T \cdot y$

**Inner product on vector spaces**: 
We see that if $V$ is a real vector space, we say that the mapping $\vec{u},\vec{v} \in V \rightarrow <\vec{u},\vec{v}> \in R$ is an inner product if it satisfies the following properties.
1) **Symmetry:** $<\vec{u}, \vec{v}> = <\vec{v}, \vec{u}>$
2) **Linearity** $<\alpha \vec{u}, \vec{v}> = \alpha <\vec{u},\vec{v}>$  and
	1) $<\vec{u}+\vec{w}, \vec{v}>$ $= <\vec{u},\vec{v}> + <\vec{w},\vec{v}>$
	2) $\vec{u},\vec{v},\vec{w} \in V$ and $\alpha \in R$
3) **Positive-definiteness**: $<\vec{v},\vec{v}> \geq 0$ for all $\vec{v} \in V$, with equality only if $\vec{v} = 0$

Example 21.2 (Example of inner product on $R^2$ ): 
Let $Q = \begin{bmatrix}3&&1\\1&&2\end{bmatrix}$ . You can check that the following defines an inner product: 
$$<\vec{x},\vec{y}> =x^ TQ\vec{y}, \vec{x},\vec{y} \in R^2$$It turns out that such “weighted” inner products are very closely connected to eigenvalues and eigenvectors (of the matrix Q), and play a big role in **optimization and machine learning**.

**Square-integrable functions**:
- Let $V$ consist of a set of functions $f(x), x\in R$  such that:
	- $\int |f(x)|^2 dx < \infty$ 
- It turns out that this is a vector space.
- Given two sets of such functions within $V$, we see that, given $f(x), g(x)$, We see that the inner product is:
	- $<f,g> = \int f(x) g(x) dx,  f,g\in V$

![[chrome_b0TyEugy8D.png]]
# Norm 
The **Euclidean Norm** of a vector is defined as:
$$||\vec{x}|| = \sqrt{x^2_1 +x^2_2 +\dots+x^2_n} = <\vec{x},\vec{x}>$$
where the inner product on the right is the Euclidean inner product. 

**Why is the norm important?** 
The norm of a vector is also the magnitude of the vector (or length of the arrow). This corresponds to the usual notion of distance in $R^2$ or $R^3$ . It is interesting to note that the set of points with equal Euclidean norm is a circle in $R^2$ or a sphere in $R^3$ . 

More generally, any choice of inner product(assuming the more general version) will give rise to a corresponding norm via defining $||v|| := <\vec{v},\vec{v}>$. Although they can be very useful, these norms will not generally correspond to the Euclidean length that we are all familiar with. 

The following properties are true for all norms (not just the 2-norm). 

**Non-negativity:** 
For $\vec{x} \in R^n$, $||x|| ≥ 0$
![[chrome_lsyqMXO2n3.png]]

Now that we have defined the inner product, it’s time to get an intuition about what an inner product is. 
First we take the unit vector $e_1 = \begin{bmatrix}1\\0\end{bmatrix}$  and a general unit vector in $R^2$ , $\vec{x} = \begin{bmatrix}\cos\alpha \\ \sin \alpha\end{bmatrix}$ . $\vec{x}$ is a unit vector because $||x|| = \sqrt{\cos^2{\alpha} + \sin^2{\alpha}} = 1$
![[chrome_KK7I9ZhJof.png]]

The process of **localizing the receiver** is in two steps.
1. Find all distances from receiver to various beacons(satelites), based on messages received
2. Combine distance measurements to calculate the absolute distance, i.e. the absolute location of the receiver. 
We’ll use *correlation* to determine the distances, and we’ll use *trilateration* to find the position based on the distance measurements and known beacon locations. Let’s start with trilateration.

In this section, we’ll assume that we’ve already determined the distance from the receiver to each beacon (we’ll explain how to measure this distance in the next section). Let’s imagine we have a situation like the one below. We know the locations of the beacons $\vec{a_1},\vec{a_2},\vec{a_3}$ , but don’t know the location of the point at $\vec{x}$ (we’ll be trying to find out what $\vec{x}$ is). We do know the distances $d_1,d_2,d_3$. We’re trying to find the coordinates of $\vec{x}$ in this diagram:
![[chrome_Mf7BKTtziY.png]]

Rewriting these using transpose notation we get: 
![[chrome_E4qPp3pocV.png]]
![[chrome_g8tE57YK9j.png]]
# Signal
A *signal* is a message that contains information as a function of time. We call a signal a discrete-time signal if it is only defined at specific points in time (for example, every minute). In contrast, a *continuous-time signal* is defined over all time. In this class we’ll focus on discrete-time signals. 

We can represent a discrete-time signal as a list of numbers. It’s convenient to write the signal as a vector where each element is the value at a single time point – then we can use all of the concepts of matrix algebra on signals. Consider the following example: a beacon in our GPS system is sending a message using radio waves. The amplitude of the radio wave as a function of time is a signal, and we only consider discrete times (for example, every second). We can represent the signal graphically or as a vector:

Every element of the vector represents the signal value at one timestep. We’ll use the notation $s[k]$ to represent the $k$-th element of the vector where initial element is at $k = 0$. For example, in the signal $s$ above, $s[0] = 0, s[1] = 1$, etc.

![[9IM4MtADUj.png]]

![[chrome_ZaT9lZ2qVV.png]]

**Circular correlation is commutative**
