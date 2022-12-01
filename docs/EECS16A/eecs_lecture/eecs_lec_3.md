eecs16a

- Last time
	- Proofs
	- Span
- Today
	- Linear (ind) dependence
	- Matrix Transformations

Span/Column Space/ Range
- Span of the columns of A is the set of all vectors b such that Ax = b has a solution
	- i.e. the set of all vectors that can be reached by all possible linear combinatinos of the columns of A
- Definition
	If (Given any ) x such that Ax = b, then b = span { cols(A)}

Proof: Span
Department of Redundant Department
Theorem: $Span\{\begin{bmatrix}1 && 1 \\ 1&&-1\end{bmatrix}\} = R^2$

Concept: pick some specific $\vec{b} = \begin{bmatrix}b_1\\b_2\end{bmatrix}$that is part of $R^2$, and show that it belongs to $S$

Need to solve:
$$a*\begin{bmatrix} 1\\1 \end{bmatrix} + b*\begin{bmatrix} 1\\-1 \end{bmatrix} = \begin{bmatrix} b1\\b2 \end{bmatrix}$$
Augumented Matrix(reduction):
$$\begin{bmatrix}1&& 1&& b_1 \\ 1 &&-1&&b_2 \end{bmatrix} = \begin{bmatrix}1&& 1&& b_1 \\ 0 &&-2&&b_2 -b_1\end{bmatrix}$$
$$=\begin{bmatrix}1&& 1&& b_1 \\ 0 &&1&&\frac{b_1-b_2}{2} \end{bmatrix} = \begin{bmatrix}1&& 0&& \frac{b_1+b_2}{2} \\ 0 &&1&&\frac{b_1-b_2}{2} \end{bmatrix}$$
Proof, as $a = \frac{(b1+b2)}{2}$  and $b = \frac{b1-b2}{2}$, we see that constructive proof is correct

Linear Dependence
$A = 	\begin{bmatrix}1 && -1 \\ 1 && -1\end{bmatrix}$ 
$a_1$ and $a_2$ are linearly dependent
$a_1 = -a_2$

- Definition 1:
A set of vectors $\{\vec{a_1},\vec{a_2},\vec{a_3},...,\vec{a_N}\}$ are linearly dependent if there exists $\{a_1,a_2,...,a_N\} \in R$ , such that:
$a_i = \sum(a_j\times \vec{a_j})$

Definition 1:
A set of vectors {a1,a2,--M } are inearly dependent if there iexists {a1,a2,..,aN} such that 
ai = {[1 1],[1,-1],[3,1]}

Linear dependence / independence
- Definition 2:
A set of vectors {a1,a2,...,aM} are linearly dependent if there exists {a1,a2,...,aM} is part of R such that:
sigma ai*vec(ai) = 0. vec(ai) is not zero.

Definition:
A set of vectors $\{ \vec{a_1},\vec{a_2},...,\vec{a_M}\}$ are linearly independent if there does not exist $(a_1, a_2,...,a_M)\neq (0,0,...,0)$
that is in $R$ such that:
$\sum a_i\times \vec{a_i} = \vec{0}$

Theorem: if the columns of matrix A are linearly dependent, then , $Ax = b$ doe snot have a unique solution.
Proof for $A$ is part of $R^{3\times 3}$
	know: columns are linearly dependent. show more than 1 solution
Concept: pick some specific solution x* and there is another one
From linear dependence Def 2
$a_1\times \vec{a_1} + a_2\times \vec{a_2} + a_3\times \vec{a_3} = \vec{0}$
$\{\vec{a_1} , \vec{a_2},  \vec{a_3}\} \times [a_1 a_2 a_3] = \vec{0}$

If you have $x = b$
From linear depndence
$a_1\times \vec(a_1) + a_2\times \vec(a_2) + a_3\times \vec(a_3) = \vec{0}$
$A*\vec{a} = 0$

Set $$x = \begin{bmatrix}1 && 0 \\ 0 && -1\end{bmatrix}	$$
This is a matrix that reflects across the x axis.

We see that the general expression for rotation matrix $\vec{R}$ :
$$R = \begin{bmatrix}\cos(\theta) && -\sin(\theta) \\ \sin(\theta) && \cos(\theta)\end{bmatrix}$$

Vecotrs can represent states of a system
Example: The state of a car at time = t
$\vec{s(t)} = \begin{bmatrix}x(t)\\y(t)\\v(t)\end{bmatrix}$, where $\{x(t),y(t)\}$ is the position and $v(t)$ is the velocity



