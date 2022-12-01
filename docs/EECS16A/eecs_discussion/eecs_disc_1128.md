# **Discussion 14A**
**Least Squares:**
- Technique for approximately solving ***overdetermined*** systems of equations (more equations than unknowns -> tall matrices)
	- EXTREMELY IMPORTANT: serves as the fundamental idea behind data fitting and machine learning
- Can also be used to solve *noisy, inconsistent* systems where no solution exists that satisfies all equations exactly.
**Application examples:**
![[WhatsApp Image 2022-11-28 at 12.14.55 PM.jpeg]]

![[WhatsApp Image 2022-11-28 at 12.29.11 PM.jpeg]]

$\hat{x} = (A^T A)^{-1} A^T \vec{b}$   $\leftarrow$ General least squares
This only works when the matrix $A^T A$ is invertible
# Example System 1
$$A = \begin{bmatrix}-2&&1&&1\\-1&&1&&1\\1&&1&&1\\2&&1&&1\end{bmatrix}, \vec{x} = \begin{bmatrix}\alpha \\ \beta \\ \gamma\end{bmatrix}, \vec{b} = \begin{bmatrix}-1\\1\\1\\-1\end{bmatrix}$$
$$A\vec{x} = \vec{b}$$
The system is not solvable since A has linearly dependent columns (2nd and 3rd) $=> A^T A$ is not invertible.

# Example System 2
$$A = \begin{bmatrix}-2 && 4\\ -1 && 1\\1&&1\\2&&4\end{bmatrix}, \vec{x} = \begin{bmatrix}\alpha\\\beta\end{bmatrix}, \vec{b} = \begin{bmatrix}-1\\1\\1\\-1\end{bmatrix}$$
We see that this system is solvable because $A^T A$ is invertible, since the columns of $A$ are linearly independent. We also see that:
$$A^T A = \begin{bmatrix}10&&0\\0&&20\end{bmatrix}$$




