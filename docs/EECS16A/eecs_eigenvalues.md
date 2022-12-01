![[chrome_uLbhifs3m6.png]]
This system is only useful to us if the values of $~x(k)$ converge to some stable fractions, i.e. the fraction of people on each webpage does not change at every timestep.

**Eigenvectors** cannot be zero vector $\vec{0}$  by default, because we see that the pair of eigenvectors//eigenvalues:
$$\lambda = 0, \vec{v} = 0$$
is the trivial pair for every possible matrix.
So we usually *do not like it.*

**Eigenspace:**
If there are two eigenvectors, they form an *eigenspace*, which is the space of all vectors $~v$ for which $A~v$ = $λ~v$

**Repeated Eigenvalues:** 
For $2\times 2$ matrix, it is possible that *two eigenvalues can end up with the same value.* 
This phenomenon is known as the *Repeated Eigenvalue*

This *repeated eigenvalue* can have either 1 or 2 associated vectors. 
Example:
$A = \begin{bmatrix}\lambda && 0 \\ 0 && \lambda \end{bmatrix}$ has a *repeated eigenvalue* of $\lambda$  
The *eigenspace* of this matrix is all of $R^2$ since for any vector $\vec{v} \in R^2, A\vec{v} = \lambda \vec{v}$ 


![[chrome_WbKCyhvylf.png]]
Since the above quadratic equation has real coefficients, we know that there are three possible cases to consider: 
1. There are two, real, distinct eigenvalues $λ_1$ and $λ_2$ that satisfy the equation. 
2. There is a single (repeated) eigenvalue of λ that satisfies the equation. 
3. There are two, complex, distinct eigenvalues $λ_1$ and $λ_2$ that satisfy the equation

All eigenvectors with different eigenvalues are linearly independent! More formally, we claim:

Theorem 9.2: Let $~v_1,~v_2,...,~v_m$ be eigenvectors of an $n×n$ matrix with distinct eigenvalues. It is the case that all the $~v_i$ are linearly independent from one another

**General Initial States**
All we’ve considered so far are steady states of the form $~x[0] = ~v$ where $~v$ is an eigenvector of the transformation matrix $A$. What if we have an arbitrary initial state, which in general may not be an eigenvector of $A$?

*Assumption:* Matrixes of eigenvector form a basis : spans all base spaces -> i.e. spans the entire column space

$A$ is $n×n$, then any initial state $~x[0]$ can be written as a linear combination $~x[0] = α_1~v_1 +α_2~v_2 +...+α_n~v_n$

We have:
$$x[t] = A^t ~x[0]$$

![[chrome_CyO02ssqOT.png]]

We solve for the equation:
![[chrome_5R7QWUAnQN.png]] 
*Solution:*
![[chrome_2Gzawdsuwp.png]]
**CRITERIA FOR CONVERGENCE:**
![[chrome_afkzet3K0B.png]]


![[chrome_si4su3BKAi.png]]
*Cool Fact: Eigenvector of 3D rotation is axis of rotation! Why is this the case?*
*Reason:* The eigenvectors of a 3D rotation doesn't get knocked off its span, as it doesn't change after the (rotation matrix $R$) is being applied. 
	**Problem:** However, this eigenvector is only the eigenvector $v_1$ that has eigenvalue $\lambda>0$, since it can't really be flipped. If eigenvalue $\lambda <0$, then the eigenvector $v_2$ is the normal to the rotation axis I think. 

Under linear transformations like these, vetors typically get knocked off their span; however, some remain on their orignal span.
-> These vectors, who are only scaled by the transformation and thus remain on their original span are called "eigenvectors"

**Eigenvalues and eigenvectors** come in pairs. 

Solving for eigenvalues of matrix $A: det(A-\lambda I) = 0$ 
Solving for corresponding Eigenvectors: $\vec{v} \in Null(A-\lambda I)$ 

Let matrix $A = \begin{bmatrix}a&&b\\c&&d\end{bmatrix}$ 
Characteristic polynomia of $A$:
$ad-d\lambda -a\lambda +(\lambda)^2 -bc=0$ -> So at most 2 solutions for eigenvalues. 

So basically for first problem, we have:
$$M=\begin{bmatrix}1&&0\\0&&9\end{bmatrix}, \lambda = 1, 9$$
We have:
$$M-1(I) = \begin{bmatrix}0 && 0 \\ 0 && 8\end{bmatrix}$$
Using augumented matrix vector form:
$$\begin{bmatrix}0 && 0 && 0 \\ 0 && 8 && 0\end{bmatrix} = \begin{bmatrix}0 && 0 && 0 \\ 0 && 1 && 0\end{bmatrix}$$
So we let solution be $[x,y]$ , we have $0\cdot x = 0, y = 0$ , so hence the span of eigenvectors = $\alpha \cdot \begin{bmatrix}1\\0\end{bmatrix}$ 

The **steady-state frequency** (i.e. fraction of visitors in steady-state) for a graph of websites is related to the **eigenspace associated with eigenvalue 1 for the “transition matrix” of the graph.** Once computed, **an eigenvector with eigenvalue 1** will have values which *correspond to the steady-state frequency* for the fraction of people for each webpage. When the *elements of this eigenvector are made to sum to one (to conserve population)*, the i'th element of the eigenvector will correspond to the fraction of people on the i th website.
