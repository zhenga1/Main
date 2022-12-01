**Announcements**

**LESSON PROGRESSION SO FAR:**
1. Set of Eqns
2. Matrix vector multiplication
3. Gaussian Elimination
4. Span, linear independence
5. Matrices as transformations
6. Matrix inversion
7. Column space, null space
8. Eigenvalues; Eigenspace

# Eigenvalues and Eigenvectors
$A\vec{v} = \lambda \vec{v} \rightarrow$ Eq 1. 
$A$ must be a square matrix, since result must be different size. $\lambda$ can be any real, even complex (16B)
If $\vec{v}=0$, then it is trivial, so $\vec{v}\neq0$ 

- Definition: Let $A\in R^{N\times N}$ be a square matrix, and$\lambda \in R$. If $\exists \vec{v} \neq 0$ such that $A\vec{v} = \lambda \vec{v}$


**Disciplined Approach:**
1. Form $B_{\lambda} = A-\lambda I$ 
So, we can convert Eq 1 to $(A-\lambda I)\vec{v}=\vec{0}$ 
2. Find all the $\lambda$ that would give a non-trivial nullspace (i.e., linearly dependent columns)
	1. Solve: $det(B_{\lambda})=0$
	2. $N^{th}$ order characeristic polynomial with $N$ solutions
	3. Each solution of $\lambda$ is an eigenvalue!
3. For each $\lambda$ solve for eigenvector

*Solution for Characteristic Polynomial*
$$A = \begin{bmatrix}a&&b\\c&&d\end{bmatrix}$$
$det(A-\lambda I) = det(\begin{bmatrix}a-\lambda&&b\\c&&d-\lambda\end{bmatrix})=(a-\lambda)(d-\lambda)-bc=0$ 
$\lambda^2 - (a+d)\lambda + (ad-bc)=0$

Three cases:
- 2 real eigenvalues
- 1 real eigenvalue(repeated)
- 2 complex eigenvalues

Theorem: Let $A\in R^{N*M}$, with M distinct eigenvalues and corresponding eigenvectors $\vec{\lambda_i},\vec{v_i} | 1\leq i \leq M$ It is the case that all $\vec{v_i}$ are linearly independent
- If $A\in R^{2x2}$ has two distinct eigenvalues, then::
	- $\vec{v_1},\vec{v_2}$ are linearly independent

**Eigenvalue Decomposition**
$A = \begin{bmatrix}1&&0\\0&&2\end{bmatrix}$
$det(A-\lambda I) = \begin{bmatrix}1-\lambda&&0\\0&&2-\lambda \end{bmatrix}=(1-\lambda)(2-\lambda)-0=0$

![[chrome_3hTwYERycd.png]]
$A = \begin{bmatrix}1/2&&0\\1/2&&1\end{bmatrix}, \vec{v_1} \in Span\{\begin{bmatrix}1\\-1\end{bmatrix}\}, \vec{v_2} \in Span\{\begin{bmatrix}0\\1\end{bmatrix}\}$
- $\vec{v_1},\vec{v_2}$ are linearly independent -> Basis for $R^2$
$\vec{v_3} = \vec{v_1} + \vec{v_2}$ 
Want to compute $A\vec{v_3} = 2A\vec{v_1}+4A\vec{v_2}=2(1/2\vec{v_1}) + 4(1\cdot\vec{v_2})=\vec{v_1}+4\vec{v_2}$
$=\begin{bmatrix}1\\-1\end{bmatrix}  + 4\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}1\\3\end{bmatrix}$ 
**Repeated Eigenvalue**
If $A$ is $2*I$, then we can have eigenspace multidimensional, since there is multiplicity of the specific eigenvalue.

![[chrome_aa74LXojDs.png]]
![[chrome_glWAUL4iFq.png]]
![[chrome_04Vwyu7rxV.png]]
**General initialization for a Transition Matrix System**
$$\vec{x}(t+1) = A\vec{x}(t)$$
Assume $\lambda_i|1\leq i \leq N$ are distinct$\rightarrow Span\{\vec{v_i} | 1\leq i\leq N\}=R^N$. Also assume:
$\vec{x}(0)=(\alpha_1\vec{v_1} + ... + \alpha_n\vec{v_N})$ for $\alpha_1 ... \alpha_n \in R$
$\vec{x}(1) = A\vec{x}(0)$
$=A(\alpha_1\vec{v_1} + ... + \alpha_n\vec{v_N})$ 
$=\alpha_1A(\vec{v_1}) + ... + \alpha_nA(\vec{v_N})$
$=\alpha_1 \lambda_1(\vec{v_1}) + ... + \alpha_n \lambda_n(\vec{v_N})$ 
So we basically have:
$x(2)=\alpha_1 (\lambda_1)^2(\vec{v_1}) + ... + \alpha_n (\lambda_n)^2(\vec{v_N})$
$x(3)=\alpha_1 (\lambda_1)^3(\vec{v_1}) + ... + \alpha_n (\lambda_n)^3(\vec{v_N})$
...
$x(t)=\alpha_1 (\lambda_1)^t(\vec{v_1}) + ... + \alpha_n (\lambda_n)^t(\vec{v_N})$

Now we wanna get the infinite answer, the steady state
$\lim_{t \to \infty} \vec{x}(t) =$
![[chrome_ZJW5uGZoP3.png]]

