**Null Space**
- Definition: The null-space of $A\in R^{n*m}$ .

Examples:
$$\begin{bmatrix}1 && 0 \\ 0 && -2\end{bmatrix} \times \begin{bmatrix}x_1 \\x_2\end{bmatrix} = \begin{bmatrix}0 \\0\end{bmatrix}$$
Nullspace = $\begin{bmatrix}0\\0\end{bmatrix}$
New example:
$$\begin{bmatrix}1 && -2 \\ 0 && 0\end{bmatrix} \times \begin{bmatrix}x_1 \\x_2\end{bmatrix} = \begin{bmatrix}0 \\0\end{bmatrix}$$
Gaussian elimination:
$x_1-2x_2 = 0$ -> $x_1 = 2x_2$
Set of (null-space) = all vectors that satisfy
$\vec{x} = \begin{bmatrix}2\alpha \\ \alpha\end{bmatrix} = \alpha\begin{bmatrix}2\\1 \end{bmatrix}$ 

Example:
Let us have the following equation:
$A\times \vec{x} = \vec{b}$ . 

Given some nullspace $\vec{v_0} \in Null(A)$ 
$\rightarrow A\vec{v_0} = \vec{0}$ 
We know one solution:
$\rightarrow A\vec{x_0} = b$ 

Then: $\vec{x_0} + \alpha \vec{v_0}$ is also a solution for any $\alpha \in R$ 
$\rightarrow A(\vec{x_0}+\alpha \vec{v_0})=A\vec{x_0} + A(\alpha \vec{v_0}) = \vec{b} + aA\vec{v_0} = \vec{b}$
So basically, if you manage to design a system where the interference is always a multiple of the nullspace, then you are basically eliminating interference.

Not good, however, to have a very large nullspace for an image which you are trying to scan or construct
**Null space of tomographic system(4. measure)**![[chrome_iX3vVisuls.png]]

Rank:
- $A \in R^{N*M}, Rank \{A\} = dim\{Span\{A\}\}$ 
- $Rank\{A\} = dim\{Span\{A\}\} \leq min(M,N)$ 
- Rank = L means that the matrix $A \in R^{N*M}$ has L independent rows&columns
This is the matrix null-be theorem:
- $Rank\{A\} + dim\{Null\{A\}\} = min(M,N)$
So a lower rank matrix will have a higher dimension nullspace. 
Full rank matrix  $\rightarrow Rank\{A\} = dim\{Span\{A\}\} = min(M,N)$ 

Equivalent statements:

![[chrome_6bybQVVOrF.png]]
**The determinant**
for $A \in R^{2*2}$, 
$det(A) = \begin{bmatrix}a&&b\\c&&d\end{bmatrix}=a\times d-b\times c$ . When $det(A) = 0$, then $A$ must not be invertible.

$A^{-1} = \frac{1}{(ad-bc)} \begin{bmatrix}d &&-b\\-c&&a \end{bmatrix}$
Determinant:
- In 2d matrix multiplication basically scales (areas) enclosed by the base vectors by the factor of the determinant

![[SAuf0ZtADI.png]]
**Interpretation of Determinant of Matrix in $R^{2*2}$ 

![[chrome_e1SRqQz5WU.png]]
Determinant in $R^3$:
$$det\{\begin{bmatrix} a&&b&&c\\d&&e&&f\\g&&h&&i\end{bmatrix}\} $$
![[chrome_CE1AltHgcN.png]]
**Page Rank**
- Ranks websites based on how many high-ranked pages link to them

**State transition matrix**
- Pagerank -> Ranks websites based on how many high-ranked pages link to them

![[chrome_ZoJHv4yFj0.png]]
![[chrome_4BhyZl0mKK.png]]
matrix = 
$$M = \begin{bmatrix}0 && 1/2 && 0 && 0\\1/3 &&0 && 0 && 1/2 \\ 1/3&&0 && 0 && 1/2 \\ 1/3&& 1/2&&1&&0\end{bmatrix}$$
	$\vec{x(t)}=>$page ranking

Initially we assume equal importance
$\vec{x}(0)$ = $[1/4,1/4,1/4,1/4]$ 

after $100$ steps, we have the rank
$\vec{x}(100)$ = [0.12,0.24, 0.24,0.4]

But we have $M\times \vec{x}(100)=\vec{x}(100)$, so basically now we have a thingy called the **steady state**, which is $\vec{x}(100)$

Allows people to evaluate how important a website is:
- What is the steady-state here? 
- -> Can be computationally expensive to do

**Eigenvectors**
**General Steady State Solution**
$\vec{x_{ss}} = Q \cdot \vec{x_{ss}}$ . We see that $Q$ has to be a square matrix($Q\neq I$ )
Hence, we can also obtain:
$Q\cdot \vec{x_{ss}} - \vec{x_{ss}}=0$ . Can also write $\vec{x} = I\cdot \vec{x}$ , so hence we have:
$(Q-I)\cdot \vec{x_{ss}}=\vec{0}$
$Q\cdot \vec{x_{ss}} - I\cdot \vec{x_{ss}}=\vec{i}$
$(Q-I)\cdot x_{ss}=0$
We see that anything that is in the Nullspace of $(Q-I)$ is the steady state solution. You find this via Gaussian Elimination.

***Eigen Values***
We saw an example for a steady-state vector:
$$Q\cdot \vec{x_{ss}} = 1\cdot \vec{x_{ss}}$$
Steady-state vectors -> Not affected, they keep the same length same everything when they go into a matrix.
-> Direction and size of the vector did not change!

We now look at more general case:
- $Q\cdot \vec{x} = \lambda \vec{x}\rightarrow \lambda \in R$   
In this case, we say that:
	$\vec{x}$ is an eigenvector of $Q$ with Eigen Value $\lambda$ 
	and span$\{\vec{x}\}$ is the associated Eigen Space
We have that, if $\vec{x}$ is eigenvalue of $Q$, we see that 
- $Q\cdot \vec{x} = \lambda \vec{x}$ 
If :
- $\lambda = 1$ -> $Q\cdot x = x$ 
- $\lambda>1 \rightarrow Q\cdot x > x$ 
- $\lambda<1 \rightarrow Q\cdot x < x$ 
**Eigenvalues and Eigenvectors**
- Definiton: Let $Q \in R^{N*M}$ be a square matrix, and $**\lambda \in R$. If $\exists \vec{x} \neq \vec{0}$ such that $Q\vec{x} = \lambda\vec{x}$ , then we must have:
	- $\lambda$ is an **eigenvalue** of $Q$, whilst $\vec{x}$ is an **eigenvector**
	- and we have $Null(Q-\lambda I)$ is its **eigenspace**
	-

![[chrome_rHALY1oskq.png]]
*Question : How can you always be sure that the steady state will exist: ie. eigenvalues will actually hit 0?*






