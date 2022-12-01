# Towards the Least Squares Algorithm
Fact: 
We have measurements: $\vec{b}$
We have matrix $A$ and unknowns $\vec{x}$
No solution for :
$A\vec{x} = \vec{b}$

What to do?
Use least squares

**Example: Sclaar problems:**
$\begin{bmatrix}a_1\\a_2\end{bmatrix} x = \begin{bmatrix}b_1\\b_2\end{bmatrix}$ . 
This is an equation with one unknown and two equation 
**What do we do?**
We project the vector and we find the solution $\hat{x}$ such that the smallest error is being found:
$$||\vec{e}|| = ||\vec{a}\hat{x}-\vec{b}|| \leq ||\vec{a}x-\vec{b}||$$
![[chrome_4zlO5TFrXE.png]]
Given vectors $\vec{a},\vec{b}$ , we say that the orthogonal projection of $\vec{b}$  onto $\vec{a}$ is:
![[chrome_ZQSYLQvHmq.png]]

# Example 2D
3 equations 2 unknowns
![[chrome_m0NbACzCI6.png]]

Theorem: Consider matrix $A$, and $y \in colspace(A)$. If $\exists \vec{z}$, such that $<\vec{z},\vec{a_i}>=0$, then $<\vec{z},\vec{y}> = 0$
Proof:
Know: $\vec{y} = c_1\vec{a_1}+c_2\vec{a_2}+\dots+c_n\vec{a_n}$
Show: $<\vec{z}, \vec{y}> = 0$
# Least Squares
The thing we wanna minimise is basially
$argmin_{\vec{x}}||\vec{e}|| = ||A\vec{x} - \vec{b}||$
$\vec{e} = \vec{b} - \hat{b}$
$A = \begin{bmatrix} \vec{a_1} && \vec{a_1} &&\dots && \vec{a_N}\end{bmatrix}$
$A\vec{x} \in colspace(A)$
Find $\vec{b} = A\hat{x}$
![[chrome_Nfsz2m5IXE.png]]
![[chrome_QfIB0AHbh5.png]]
![[chrome_NujmNycKCi.png]]
$A^T (\vec{b} - A\hat{x})=0$ 

$A^T\vec{b} - A^T A \hat{x} = 0$
$A^T A \hat{x} = A^T \vec{b}$
So therefore we have:
$\hat{x} = (A^T A)^{-1} A^T \vec{b}$
$\hat{b} = A(A^T A)^{-1} A^T \vec{b}$

**Example 1**
$A\vec{x} = \vec{b}$
$\begin{bmatrix}2\\1\end{bmatrix}^x = \begin{bmatrix}1\\1\end{bmatrix}$
by module 1, we have
$\begin{bmatrix}2&&1\\1&&1\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}= \begin{bmatrix}1&&\frac{1}{2}\\0&&\frac{1}{2}\end{bmatrix}$
This is impossible, no solution by **module 1**
but by module 2 we can have:
$$\hat{x} = (A^T A)^{-1}A^T\vec{b}$$
$$\hat{x} = (1/5) \begin{bmatrix}2&1\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}=(1/5)\times 3 = \frac{3}{5}$$
![[chrome_VT5xKhVMNO.png]]
![[chrome_gJhyOOJ5Ui.png]]
![[chrome_AgUdj0I4Cw.png]]
![[chrome_9CUXq70VgO.png]]

We see that, for nonsquare matrixes with dimension $a\times b$, as such:
$$A = \begin{bmatrix}a_{11}&&a_{12}&&a_{13} \dots a_{1b} \\ a_{21}&&a_{22}&&a_{23} \dots a_{2b} \end{bmatrix}$$

**Least squares are used for solving an overdetermined set of equations**
Basically, we have that the solution to 
$A\vec{x} = \vec{b}$ by least squares is basically the projection of $\vec{b}$ onto the column space of $A$. So in other words, we can basically have:
$\vec{x} = proj_{col(A)}{\vec{b}} = (A^T A)^{-1} A^T \vec{b}$

**Orthogonal basis**
- A basis for **V** whose vectors are *mutually orthogonal*. 