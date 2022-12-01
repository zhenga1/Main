**EECS Change of basis**
We can see that the same vector $~u$ can be represented in multiple ways! In the standard basis $~e_1,~e_2$, the coordinates for $~u$ are $(4,3)$. In the skewed basis $~a_1,~a_2$, the coordinates for $~u$ are $(4,1)$. It’s the same vector geometrically, but with different coordinates. In general, suppose we are given a vector$~u \in R_n$ in the standard basis and want to change to a different basis with linearly independent basis vectors $~a_1,··· ,~a_n$.

If we denote the vector in the new basis as  $u_a = \begin{bmatrix} u{a_1} . . . u_{a_n} \end{bmatrix}$ we solve the following equation $A~u_a = ~u$, where A is the matrix $(a_1 ··· ~a_n)$ . Therefore the change of basis is given by: $~u_a = A^{−1} ~u$
