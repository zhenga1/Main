#cs70
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

**Multiset** - A set in which the same element is allowed to appear more than once.

**Incident:**
Moving on with our example, we say that
		edge e = {u, v} (or e = (u, v)) 
is *incident* on vertices u and v, and that u and v are *neighbors* or *adjacent*.

If *G* is undirected, then the *degree* of vertex u ∈ V is the number of edges incident to u, i.e., $degree(u) = |\{v ∈ V : \{u, v\} ∈ E\}|$. 

A vertex u whose degree is 0 is called an **Isolated Vertex**, since there is no edge which connects u to the rest of the graph.

A directed graph, on the other hand, has two different notions of degree due to the directions on the edges. Specifically, the *in-degree* of a vertex u is the number of edges from other vertices to u, and the *out-degree* of u is the number of edges from u to other vertices.

**Simple path**
In this class, we assume a path is ***simple***, meaning $v_1,\dots, v_n$ are distinct. Let $G = (V,E)$ be an undirected graph. A path in $G$ is a sequence of edges ${v_1, v_2},{v_2, v_3},...,{v_{n−2}, v_{n−1}},{v_{n−1}, v_n}$. In this case we say that there is a path between $v_1$ and $v_n$. For example, suppose the graph $G_3$ below models a residential neighborhood in which each vertex corresponds to a house, and two houses u and v are neighbors if there exists a direct road from u to v.

**Cycle**
A ***cycle*** (or circuit) is a sequence of edges {v1, v2},{v2, v3},...,{vn−2, vn−1},{vn−1, vn},{vn, v1}, where v1,..., vn are distinct

Suppose now that your aim is not to go from 1 to 3 as quickly as possible, but to take a *leisurely stroll* from 1 to 3 via the sequence ${1,2},{2,1},{1,4},{4,3}$. A sequence of edges with possibly repeated vertices, such as this one, is called a *walk* from $1$ to $3$.

Analogous to the relationship between paths and cycles, a *tour* is a walk which starts and ends at the same vertex. For example, ${1,2},{2,3},{3,1}$ is a tour.

==**Summary of terms**==
![[chrome_tEWGha4SuB.png]]

**Connectivity.**
Much of what we discuss in this note revolves around the notion of connectivity. A graph is said to be *connected* if there is a path between any two distinct vertices. For example, our residential network $G_3$ above is connected, since one can drive from any house to any other house via *some* sequence of direct roads. On the other hand, the network below is *disconnected*.
![[chrome_BRFQZZV9gL.png]]
Note that any graph (even a disconnected one) always consists of a collection of connected components, i.e., sets V1,...,Vk of vertices, such that all vertices in a set Vi are connected. For example, the graph above is not connected, but nevertheless consists of three connected components: V1 = {1,2,3}, V2 = {4}, and V3 = {5,6,7}.


Given a graph G (in this case, G is an abstraction of Königsberg), is there a walk in G that uses each edge exactly once? We call any such walk in a graph an *Eulerian walk*. (In contrast, by definition a walk can normally visit each edge or vertex as many times as desired.) Moreover, if an Eulerian walk is closed, i.e., it ends at its starting point, then it is called an Eulerian tour. Thus, the Seven Bridges of Königsberg asks: Given a graph G, does it have an Eulerian tour? We now give a precise characterization of this in terms of simpler properties of the graph G. For this, define an even degree graph as a graph in which all vertices have even degree.


We start with a useful subroutine, FINDTOUR(G,s), which finds a tour (not necessarily Eulerian) in G. FINDTOUR is very simple: it just starts walking from a vertex s ∈ V, at each step choosing any untraversed edge incident to the current vertex, until it gets stuck because there is no more adjacent untraversed edge. We now prove that FINDTOUR must in fact get stuck at the original vertex s. Claim: FINDTOUR(G,s) must get stuck at s

Theorem 5.1 (Euler’s Theorem (1736)). An undirected graph G = (V,E) *has an Eulerian tour* iff G is even degree, and connected (except possibly for isolated vertices).