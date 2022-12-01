**Column space**:
**range** of operator = space of all outputs that the operator can map itself to
$Col(A) = \{ \vec{v} | \vec{v}  = \sum x_i\times a_i\}$

Think of **linear matrix** of $dim = N*M$ as linear function taking in vector of dimensionality **m** and outputting a vector of dimensionality **n**

So we must have the range of linear matrix = the column space of linear matrix

Dimensionality of matrix -> How many parameters required to define vectors in the column space of the matrix.
![[chrome_S5r66jT74O.png]]
Nullspace of dimension M is a subspace of $R^{M*M}$

Dimension of range of matrix;
	- Total number of linearly independent columns 
Dimension of Nullspace of matrix:
	- Total number of linearly dependent columns

$m-dim(Col(A)) = dim(N(A))$ 
$\rightarrow$ loss of dimensionality from input space to output space shows up in nullspace! Result -> Rank nullity theorem

**Computing the nullspace**
Aim: Solve equation $A\vec{x} = \vec{0}$ 
Method:
1) Choose set of linearly independent vectors and set of linearly dependent vectors in column space(which can be expressed in terms of linearly independent vectors)
	1) Choices need not be unique ... one can choose linearly independent vectors anywhere.
![[chrome_1n0tHxgb1Y 4.png]]
2) Consider each linearly dependent column individually, setting only its coefficient to 1 and all others to zero. Then doing it again with all the other linearly dependent columns
3) Generalise the coefficients, multiply them by constants, then add them together

A **basis** of a subspace is a *set of linearly independent vectors* that span the subspace, and the *dimension of a subspace* is the number of vectors in its bases





