Lecture 2A 
Vectors Matrices, Multiplication

Last time:
- Gaussian Elimination

Today:
- vectors
- Matrix-Matrix and Matrix-vector Multiplicaion

Reduce the matrix to row-echelon form, from left-to-right by using:
1. Multiply an equation with nonzero scalar
2. Addign a scalar constant multiple of one equation to another
3. Swapping equations.


Single solution -> If the n*n matrix can be reduced to a diagonal with all 1, and a 0 triangle thingy
Infinite solution -> 0 = 0. So basically one term can be anything, an infinite number of solutions.

Single solution -> identity matrix + the cosntants
Infinite solutions -> When the line thingy is not complete. There is one row/column that has all zero.

Vectors:
- An array of N numbers
- The notation $R_n$ 
	- Represents coordinates in an N-dimensional space
	$\vec{x} = \begin{bmatrix}x_1\\x_2\\x_3\\x_4\\...\\x_n\end{bmatrix}$
- For example:
	x=$\begin{bmatrix}3 \\ 2\end{bmatrix}$ is a part of $R_2$


Pixel color 
- x ->$\begin{bmatrix}215\\131\\25\end{bmatrix}$

Pixel values in an image
-  -> x-> $\begin{bmatrix}x1\\x2\\x3\\x4\end{bmatrix}$

C convention -> (rasteurise)Flatten the image row first
Python convention -> same as C

x = $\begin{bmatrix}x1\\x2\\x3\\x4\\x5\\...\\x120\end{bmatrix}$

0 vector = > $\begin{bmatrix}0\\0\\0\\0\\...\\0\end{bmatrix}$

1 vector = > $\begin{bmatrix}1\\1\\1\\1\\...\\1\end{bmatrix}$

For identity matrix:
$$\begin{bmatrix} 1 && 0 && ... && 0 \\ 0 && 1 && ... && 0\\&&&&...\\ 0 && 0 && ... && 1 \end{bmatrix}$$
$e_1=\begin{bmatrix}1\\0\\...\\0\end{bmatrix}$


$e_2=\begin{bmatrix}0\\1\\...\\0\end{bmatrix}$
...

$e_n=\begin{bmatrix}0\\0\\...\\1\end{bmatrix}$ 

Matrices
 - A collection of numbers in a rectangular form
	$$X = \begin{bmatrix}x11 && x12 && x13 && ... && x1M \\ x21 && x22 && x23 &&...  &&   x2M \\ x31 && x32 && x33 &&... &&    x3M \\&&&&... \\xN1 && xN2 &&xN3 && ... && xNM\end{bmatrix}$$
	A vector $X \in R^{N\times M}$ 

Properties of vector addition
- Commutativity: $x + y = y+ x$ 
- associativity: $(x+y) + z = x+ (y+z)$ 
- Additive negattive: $x+ (-x) = 0$ 
- Additive identity: $x+0 = x$ 

$x^T$ is the transpose of x
$x = \begin{bmatrix}x_1\\x_2\\x_3\\...\\x_N\end{bmatrix}$ -> Vertical vector 
-> $x^T = \begin{bmatrix}x_1^T&&x_2^T&&x_3^T&&x_4^T&&...&&x_N^T\end{bmatrix}$ -> Horizontal vector

Can you apply transpose to a matrix
Matrix Transpose
- If the elements of the matrix $A$ (is part of) $R^{NM}$ are $a_{ij}$
- The elements of $A^T$ (is part of ) $R^{MN}$ are $a_{ji}$
- Matrix Transpose is not (generally) an inverse ! 

Vector-Vector multiplication
Multiplication is valid only for specific matching dimensions!
- Width of the 1st matches length of the second

cannot multiply two matrixes like this -> Both vertical vectors (or both horizontal vectors)
But you can multiply a vertial vector and a horizontal vector. 

If I have two vectors, each one is $R^N$
$y^T\times x$ = $\begin{bmatrix}y_1&&y_2&&y_3&&...&&y_n\end{bmatrix} \times \begin{bmatrix}x_1\\x_2\\x_3\\...\\x_n\end{bmatrix}$ 
= $y_1x_1 +y_2x_2 + y_3x_3 + ... + y_nx_1$ [vector]

Vector multiplication does not commutie!
Also known as "outer product"

Scalar 1*1 -> "Inner product" -> or dot product

1. $N*N$
2. $M*N$
3. $M*M$
4. $1*M$


