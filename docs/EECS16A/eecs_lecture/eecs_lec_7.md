Invertibility of Linear Transformations
- Theorem: *A* is invertible, if and only if(iff) the columsn of *A* are lineraly independent
	- 1. If columns of $A$ are lin. dep. then $A^-1$ does not exist
	- 2. If $A^{-1}$ exists, then the cols of *A* are linearly independent
- Proof concept: Assume linear dependene and invertibility and show that it is a contradiction

From linear dependence: we have that if *A* has linearly dependent columns, then there must exist $\vec{a}\neq\vec{0}$   
such that:
$A\times a = \vec{0}$

Assume $A^{-1}$ exists
$A\times a = 0$ 
Assume $A^{-1}$ exists
then we must have 
$A^{-1} \times A\times a  = A^{-1}\times \vec{0}$

We have, given a matrix A
$$A = \begin{bmatrix} a & b\\c & d\end{bmatrix}$$
the determinant is given by $a*d-b*c$

Equivalent Statements:
- Matrix A is *invertible*
- $A*x = b$     has a unique solution
- A has linearly independent columsn(A is full rank)
- A has trivial nullspace

Today and next time's Jargon:
- Rank: A matrix A is the number of linearly independent columns
- Nullspace of Matrix A is set of solutions to Ax=0
- A vector space is set of vectors connected by two operators(+,x)
- vector subspace is subset of vectors that have "nice properties"
- Basis for vector space is minimum set of vectors needed to represent all vectors in the space
- Dimension of vector space is number of basis vectors
- Column space is span(range) of columns of matrix

# Vector space:
From Merriam Webster:
- *Set of vectors along with operations of addition and multicpliation such that the set is a commutative group under addition, it includes a ...*

Vector space:

A **vector space** *V* is set of vectors made up of scalars and two operators * *, + that satisfy, given $\vec{x} \in V$ 

- $a\times x$ is part of V
- $x+y$  is part of V
- $x + (y+z) = (x+y) + z$ (associativity)
- $x+y = y+x$ (commutativity)
- $\exists0 \in V$ s.t     $x + \vec{0} = x$ (additive identity)
- $\exists (-x) \in V$ s.t. $x+(-x)=0$ (additive inverse)
- $a*(x+y) = a*x+a*y$  ( distributivity)
- $a\times(\beta x)=(\alpha \beta)\times x$
- $(\alpha + \beta)\times x = \alpha x + \beta x$
- $1\times x= x$ 

Scalars can be vector spaces,
Set:
$$\{a\in R, a \geq 0 \}$$
Is not a vector space, not because scalars cannot be vector spaces, but rather because this thingy does not satisfy additive inverse condition. 

SUBSPACE:
- A subspace U consistas of a subset of V in vector space (V,F,+, $\times$)
- $U \subset V$ and have 3 properties
1. Contains $\vec{0}$ vector, as in $\vec{0} \in U$
2. Closed under vector addition: $(v_1,v_2) \in U =>v_1 + v_2 \in U$
3. Closed under scalar multiplication: $\vec{v_1} \in U, a \in F => a\vec{v} \in U$

Consider all vectors $\vec{v}$ who's length $< 1$. Is this subspace?
NOPE
Reason: Cuz not closed under vector addition. Can add two vectors within the range and it is possible that resulting vector $\vec{r}$ :
$$\vec{r} \notin U$$
A: not closed under addition, nor scalar mult.

Q; is Span $\{\begin{bmatrix}1\\1\end{bmatrix}\}$ a subspace?
A: It is cuz it satisfies all the conditions

Q; is  $k \times \begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}-1\\0\end{bmatrix}$ a subspace?
A: It is cuz it satisfies all the conditions

$R_2$ is a vector space, and it is not a subspace of anything other than itself lol. 

All subsets that are not vector spaces are not subspaces. 

Q:  Is a cone a subspace of $R_2$?
![[chrome_39dNUnAOLZ.png]]
A: Satisfies properties 1 and 3, but not 2.

Subspaces are a *REDUCED DIMENSION* of the larger vector space. Essentially it is a *SUB* vector-space

Q: what about 2D planes in $R_3$?
![[chrome_IvMIuDrZOP.png]]

Subspaces:
Example:
We have, if :
$$W = \begin{bmatrix} a&&b\\0&&d \end{bmatrix} | a,b,d \in R ,     V = R^2$$
Question: is W subspace of V? 
Answer, Yes. 

Bases:
- Minimum set of vectors spanning vector spae
- Definition: $\forall  V$, a set of vectors $v_1,v_2,v_3,...,v_N$ is a basis of vector space if it satisfies:
	- $v_1,v_2,v_3,...,v_N$ are linearly independent
	- $v \in V$  such that $\exists \{a_1,a_2,...,a_n\} \in R$ such that $\vec{v} = a_1*v_1 + a_2*v_2 + ... + a_n*v_n$

Column space:
- Range/span/columnspace of set of vecctors is set of all possible linear combinations
	- span $\{a_1,a_2,...,a_n\}$ = all vector values $\vec{v}$ for which it is possible to have $\vec{v}=\sum b_m*\vec{a_m},    \{b_1,b_2,...,b_N\} \in R$ 

Show whether column space is subspace
A = $\begin{bmatrix}a && 0 \\ 0 && b \\ 0 && 0\end{bmatrix}$ .  If $v_1 = A*u_1, v_2 = A*u_2$ , then we have 
$(v_1,v_2)$ is in column space of *A*.  

$v_1 + v_2 = A*u_1 + A*u_2$ 
We see that all conditions are satisfied, so therefore the column space is a subspace + vector space. 

RANK:
- $A \in R ^{(N*M)}$ , Rank {A} = dim { Span {cols(A)}}
- Rank ${A}$ $\leq min(colno, rowno)$ 
- Rank of different matrixes depends on how many independent(linearly) vectors exist, excluding $\vec{0}$. 
- Rank must be less than or equal to min of column and row number count

NULL SPACE:
- Set of vectors for matrix $A \in R^{N*M}$ such that the product of matrix and vector is $\vec{0}$ 
$\vec{0}$  is the trivial nullspace.
However, some of the matrixes (with linearly dependent columns) have more than trivial nullspace. 


