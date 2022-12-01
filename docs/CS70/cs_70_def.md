**Set** - a well defined collection of objects

These **objects** are called **elements** or **members** of the set, and they can be anything, including *numbers, letters, people, cities, and even other sets*
- Properties
	- Unique (each element in a set cannot be repeated, just like the python **set()**

Two sets $A$ and $B$ are said to be equal, written as $A = B$, if they have the same elements. The order and repetition of elements do not matter, so $\{red, white, blue\} = \{blue, white, red\} = \{red, white, white, blue\}$ 
**Cardinality**
Size of a set(number of elements/members within a set).  
Ex: If A = {1,2,3,4}, then the cardinality of A, denoted by |A|, is 4. It is possible for the cardinality of a set to be 0. There is a unique such set, called the empty set, denoted by the symbol $\emptyset$. A set can also have an infinite number of elements, such as the set of all integers, prime numbers, or odd numbers.

**Subsets and Proper Subsets**
<p style="text-align:center;">If every element of a set A is also in set B, then we say that A is a subset of B, written A ⊆ B.  We can also write B ⊇ A, or B is a superset of A.</p>

<p style="text-align:center">A proper subset is a set A that is strictly contained in B, written as A ⊂ B, meaning that A excludes at least one element of B. For example, consider the set B = {1,2,3,4,5}. Then {1,2,3} is both a subset and a proper subset of B, while {1,2,3,4,5} is a subset but not a proper subset of B. Here are a few basic properties regarding subsets</p>

1) Two sets are said to be **disjoint** if A∩B = $\emptyset$
2) The union of a set A with a set B, written as A∪B, is the set of all elements which are in either A or B or both.

- A∪B = B∪A 
- A∪$\emptyset$ = A
- A∩B = B∩A 
- A∩ $\emptyset$ = $\emptyset$

If A and B are two sets, then the relative complement of A in B, or the set difference between B and A, written as B − A or B \ A, is the set of elements in B, but not in A. 
**B \ A = {x ∈ B | x ∈/ A}**. 

For example, if B = {1,2,3} and A = {3,4,5}, then B\A = {1,2}. For another example, if R is the set of real numbers and Q is the set of rational numbers, then R \Q is the set of irrational numbers. Here are some important properties of complements:

- A\A = $\emptyset$
- A\ $\emptyset$ = A 
- $\emptyset$ \A = $\emptyset$

The Cartesian product (also called the cross product) of two sets A and B, written as A × B, is the set of all pairs whose first component is an element of A and whose second component is an element of B. In set notation, 
$$A × B = {(a,b) | a ∈ A,b ∈ B}$$

For example, if A = {1,2,3} and B = {u, v}, then 
$$A × B = {(1,u),(1, v),(2,u),(2, v),(3,u),(3, v)}$$

And 
$$N × N = {(0,0),(1,0),(0,1),(1,1),(2,0),...}$$
is the set of all pairs of natural numbers.

The most important and subtle propositional form is an **implication**:
**Implication**: P ⇒ Q (“P implies Q”). This is the same as **“If P, then Q.”**
Example:
- If you stand in the rain, then you’ll get wet. 
- If you passed the class, you received a certificate.
An **implication** P =⇒ Q is false only when P is true and Q is false.
