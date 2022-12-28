#sets
#cs70 
**Definition:** A set is any well defined collection of objects, which can be anything from lists to objects to numbers. The ordering of the set does not matter.

Two sets A and B are equal if and only if for every $x$ 
$\because x \in A$
$\therefore x\in B$

# Cardinality
#cardinality
**Definition:** No of elements / Size of a set
<u>Example:</u> $A=\{1,2,3,4\}$ has cardinality $4$

# Subsets and Proper Subsets 
#subset
#propersubset
If every element of a set A is also in set B, then we say that A is a **subset** of B, written A ⊆ B. Equivalently we can write B ⊇ A, or B is a **superset** of A. 

A **proper subset** is a set A that is strictly contained in B, written as A ⊂ B, meaning that A excludes at least one element of B. For example, consider the set B = {1,2,3,4,5}. Then {1,2,3} is both a subset and a proper subset of B, while {1,2,3,4,5} is a subset but not a proper subset of B. Here are a few basic properties regarding subsets: 
- The empty set, denote by {} or $\emptyset$, is a proper subset of any nonempty set A: {} ⊂ A.
- The empty set is a subset of every set B: {} ⊆ B. 
- Every set A is a subset of itself: A ⊆ A.

# Intersections and Unions
#intersection
#union
The **intersection** of a set A with a set B, written as A∩B, is the set containing all elements which are in both A and B. Two sets are said to be **disjoint** if $A∩B = \emptyset$. The union of a set A with a set B, written as A∪B, is the set of all elements which are in either A or B or both. For example, if A is the set of all positive even numbers, and B is the set of all positive odd numbers, then $A∩B = \emptyset$, and A∪B = Z +, or the set of all positive integers. Here are a few properties of intersections and unions:
- $A∪B = B∪A$
- $A∪ \emptyset = A$
- $A∩B = B∩A$
- $A∩ \emptyset = \emptyset$

In mathematics, some sets are referred to so commonly that they are denoted by special symbols. 

These include:
- N denotes the set of all natural numbers: $\{0,1,2,3,\dots \}$. 
- Z denotes the set of all integer numbers: $\{\dots,−2,−1,0,1,2,\dots \}$. 
- Q denotes the set of all rational numbers.
- R denotes the set of all real numbers. 
- C denotes the set of all complex numbers.

# Cartesian Product
#cartesianproduct
#crossproductsets
**Definition:** Cross product between two sets $A$ and $B$ is the set of all pairs whose first component is a member of set $A$ and whose second component is a member of set $B$. 
<u>Specifically</u>
$A \times B = \{(a,b) | a \in A,b \in B\}$. 

Or we also have:
$A = \{1,2,3\}$ and $B = \{u, v\}$, then 
$A \times B = \{(1,u),(1, v),(2,u),(2, v),(3,u),(3, v)\}$.
$N\times N =$ set of all the pairs of natural numbers

Given a set $S$, the **power set** of S, denoted by $P(S)$, is the set of all subsets of $S$ For example, if S = {1,2,3}, then the power set of S is: 
$P(S) = \{\{\},\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\{1,2,3\}\}$. 
Note that, if $|S| = k$, then $|P(S)| = 2\times k$

![[chrome_15jPszZrrp.png]]


