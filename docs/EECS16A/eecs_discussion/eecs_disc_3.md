#r/discussion
- Discussion notes: ![[Anish's Discussion 5A.pdf]]

# Discussion 5A
```jupyter
print("Hello world i am cool")
```


**Subspace:**
A *subspace U* of *V* is a subset of the vectors in *V* that satisfy:
1) Contains $\vec{0}$ (zero-vector)
2) Closed under vector addition -> If $\vec{u_1}, \vec{u_2} \in U$  => $\vec{u_1} + \vec{u_2} \in U$ 
3) Closed under scalar multiplication $\rightarrow$ If $\vec{u_1}\in U, \alpha \in R$, then $\alpha \vec{u_1} \in U$ 
Combined $\vec{u_1}, \vec{u_2} \in U$ 
=> We must have for any such vectors $\vec{u_1}, \vec{u_2}$, that
	$\alpha \vec{u_1} + \beta\vec{u_2} \in U$ , $\forall \alpha, \beta \in R$ 
$A = \begin{bmatrix}a_1 && a_2 && a_3&& ...&& a_n\end{bmatrix}$ 

Solve for nullspace:
$A = \begin{bmatrix} 1 && 2 && 0 && 3 && 0 \\ 1 && 3&& 0 &&4&&0 \end{bmatrix}$ -> Augumented matrix
Let the vector (nullspace) $\vec{v} = \begin{bmatrix}p\\q\\r\\s\end{bmatrix}$Free variables, let us have $(r,s)$ are the free variables.

$q+s=0$ 
$p+2q+3s=0$ 

-> $q+s=0, q=-s$ 
-> $p+2(-s) + 3(s) = 0$, $p=-s$ 

So we have:
$$\vec{v} = \begin{bmatrix}p\\q\\r\\s\end{bmatrix} =\begin{bmatrix}-s\\-s\\r\\s\end{bmatrix} =r\begin{bmatrix}0\\0\\1\\0\end{bmatrix}+s\begin{bmatrix}-1\\-1\\0\\1\end{bmatrix}$$
So nullspace of $A$ is :
	$$Null(A) = \biggl\{\vec{v} | \vec{v} = \begin{bmatrix}0\\0\\1\\0\end{bmatrix}+s\begin{bmatrix}-1\\-1\\0\\1\end{bmatrix}\biggl\}$$
	
If something is in the Nullspace, it cannot be in the column space.
Null space of the matrix always contains the $\vec{0}$ as a trivial solution
A non-trivial nullspace means that a matrix has linearly dependent columns, which also means that $A*\vec{v}=\vec{0}$ has infinitely many solutions

Rank-nullity theorem:
	$m-dim(col(A)) = dim(null(A))$,
	where *m* is the total number of columns of *A*.
	Note.. True only for square matrixes 

	