At what point $(a,b)$ does $f(x,y)$ have local max/min?
If $f(x,y)$ has local max/min at $(a,b)$, then we have
$$\nabla f(a,b)=0$$
These are effectively the critical points.

How do we tell if critical point is local max or min?
$$D = f_{xx}\times f_{yy}-f_{xy}^2 = det\begin{bmatrix}f_{xx} && f_{xy}\\f_{yx} && f_{yy}\end{bmatrix}$$
If $D>0$ is true:
then if $f_{xx}>0$, we have a local minimum
otherwise, if $f_{xx}<0$,, we have a local maximum

Example:
$f(x,y)=x^4+y^4-4xy+1$
Find critical points
$\frac{\partial f}{\partial x} = 4x^3-4y = 0 \rightarrow y=x^3$
$\frac{\partial f}{\partial y} = 4y^3-4x = 0 \rightarrow x=y^3$

$D = f_{xx}f_{yy} - f_{xy}^2 = (12x^2)(12y^2)-(-4)^2=144x^2y^2-16$ 
Solutions:
$(1,,1),(-1,-1),(0,0)$ 
Solution 1: $D>0, f_{xx}>0 \rightarrow (1,1)$ is local minimum
Solution 2: $D>0, f_{xx}>0 \rightarrow (-1,-1)$ is also local minimum
Solution 3: $D<0$ ,hence $(0,0)$ isn't a minimum or maximum, and instead is a saddle point

Global max min:
Find largest and smllerst values of $f(x,y)=x^2+y^2+x^2y+4$ on the square $\{(x,y)| |x|<1,|y|<1\}$ 
Critical points:
$\frac{\partial f}{\partial x} = 2x+2xy=0 \rightarrow x=-xy \rightarrow x=0$ or $y=-1$
$\frac{\partial f}{\partial y} = 2y+x^2=0 \rightarrow x^2=-2y$
Solution -> $(0,0)$ sole critical point on square.
$D=f_{xx}f_{yy}-f_{xy}^2=(2+2y)(2)-(2x)^2=4+4y-4x^2$
$D>0$ at $(0,0)$, and $f_{xx}>0$, so hence $(0,0)$ is local min.
In the domain, since there are no other local min, $(0,0)$ is the global min.

So now we fix the boundaries and try to find the maximum.

Points to check:
$(1,1),(-1,1),(0,-1)$ 
We see:
$f(0,0)=4,f(0,-1)=5,f(1,1)=7,f(-1,1)=7$ 
So, the global max is $=7$ 

FOCUS:
The max/min within a closed domain is *always a critical point* within the domain or *along the boundary*.

Boundary:
Let $f(x,y)$ be a function and let $g(t)=f(x(t),y(t))$ 
Find exreme values of $g(t)$ on interval $[0,2\pi]$ 
With $g(t)$ representing boundary of a circle, we have:
$$x(t)=R\cos(t), y(t) = R\sin(t)$$Solving for $\frac{\partial g}{\partial t}=0$, we use the chain rule:

Problem:
$f(x,y) = x^2+y^2-2x$ . $D$ is triangle with vertices:
$(2,0),(0,2),(0,-2)$. 

Critical points:
$\frac{\partial f}{\partial x} = 2x-2=0 \rightarrow x=1$ 
$\frac{\partial f}{\partial y} = 2y=0 \rightarrow y=0$ 

Boundary lines: $x=0, y=2-x, y=x-2$
- $x=0, f(0,y)=y^2$, so we have extremes $(0,0),(0,2),(0,-2)$ 
- $y=2-x, f(x,2-x) = x^2 + (2-x)^2 -2x$ 
 $=2x^2 -6x+4, x \in [0,2]$ . The extremes are :
 $(0,2),(2,0),(3/2,1/2)$ 


