#r/discussion
- Discussion notes: ![[Anish's Discussion 6A 2.pdf]]

# Discussion 6A
```jupyter
print("Hello world i am cool")
```

**Transition Matrix**
$\vec{x}[k+1] = A\vec{x}[k]$
$\{\vec{x}[k]\}$is the state of the system at timestep $k$

Statement: $\vec{x}[k] = A^{n} \vec{x}[0]$ 
Proof: $\vec{x}[1] = A\vec{x}[0]$
$\vec{x}[2] = A\vec{x}[1] = A^2\vec{x}[0]$
$\vec{x}[1] = A\vec{x}[0] = A(\alpha_1*\vec{v_1} ... \alpha_n*\vec{v_n})=A(\alpha_1*\lambda_1 ... \alpha_n*\lambda_n)$ 

# Eigenvector Steady State Theorem 1
For every eigenvector, we have that:
$A*\vec{v} = \lambda \vec{v}$. So, this can be extended to
$A^k*\vec{v} = \lambda^k \vec{v}$

Proof:
Given: $A*\vec{v} = \lambda \vec{v}$
We have: $A^2\vec{v}=A*A*\vec{v} = A\lambda \vec{v} = \lambda A\vec{v} = \lambda^2 \vec{v}$
So on so forth

Therefore:
$x[k] = A^k \vec{x}[0] = A^k (\alpha_1*\vec{v_1} ... \alpha_n*\vec{v_n}) = \alpha_1 A^k\vec{v_1} + ... +\alpha_n A^k\vec{v_n}$  

![[WhatsApp Image 2022-10-03 at 12.28.58 PM.jpeg]]

If we have matrix $M$ with one of the eigenvectors $\vec{v_2}$ having eigenvalue $\lambda_2>1$, and the ability to express a vector $\vec{x} = \alpha \vec{v_1} + \beta \vec{v_2}$, where $\beta$ is nonzero, we must have that the steady state will blow up by **theorem 1**

For any eigenvalue $\lambda$ of Matrix A, we must have that the corresponding eigenvector has the properties:
$\vec{v_n} \in span\{null(A-\lambda_n I)\}$

![[WhatsApp Image 2022-10-03 at 12.50.17 PM.jpeg]]

$x[0] = <150,250,200>$ 
By previous calculations, we know that the steady state must exist in some form of $\alpha \times <1,1,1>$ 
However, we also know that, since the matrix is conservative(Reservoir analogy - water never exits or enters the system), we must know that there must in total be $150+250+200=600$

Scale entire vector by $200$, so we have the steady state:

= $200*<1,1,1> = <200,200,200>$
You must (usually) normalize the values, meaning:
- Make the sum of elements of $(x,y,z)$ as $1$.





