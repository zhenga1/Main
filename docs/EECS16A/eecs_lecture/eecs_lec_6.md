EECS 16A

Describe car. 
- Using position and velocity
$\vec{s(t)} = \{x(t),y(t),v(t)\}$
- Require one more parameter, which is direction, but is missing.
- So another parameter is needed

Graph Transition Matrix:
Example: Reservoir's and Pumps
Three reservoirs

Pumps move water from reservoirs $A, B, C$, using set linear equations. Can use matrix to express states of the reserviors over time(such as at the next day)

Graph transition matrix must be a square matrix, as only then will there be the notion of 'states', such as the amounts of water in $A,B,C$

Let the relevant square matrix representing the graph transition be $M$ 

Can augument $M$ to create matrix $ME$ = $[M\space E]$   ,and then gaussian elimination to reduce $M$ to row echolon form. Whatever $E$ (identity matrix) becomes then is the square inverse of matrix $M$, $M^{-1}$. 


