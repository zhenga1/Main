A **graph** is ***planar*** if it can be drawn on the plane without crossings. For example, the first four graphs shown below are planar. Notice that the first and second graphs are the same, but drawn differently. Even though the second drawing has crossings, the graph is still considered planar since it is possible to draw it without crossings. 

The other three graphs are not planar. The first one of them is the infamous “three houses-three wells graph,” also called $$K_{3,3}$$, (This notation says there are two sets of vertices, each of size three and all edges between the two sets of vertices are present.)
I.e. this:
![[Pasted image 20221226095630.png]]

The second is the “complete” graph (every edge is present) with five nodes, or K5. The third is the four-dimensional cube. We shall soon see how to prove that all three graphs are non-planar. 
![[Pasted image 20221226095646.png]]

A useful concept is the notion of a bipartite graph, $$G = (V,E)$$ which is a graph where the vertices are split into two groups and edges only go between groups. More formally, we have $$V = L ∪ R$$ and $$E ⊆ L × R$$. Clearly, K3,3 is bipartite. Moreover, the four dimensional cube is bipartite: this follows from the fact that every cycle in the cube has even length. We will show the equivalence a bit later

### Face of a graph
When a planar graph is drawn on the plane, one can distinguish, besides its vertices (their number will be denoted v here) and edges (their number is e), **the faces** of the graph (more precisely, of the drawing). The faces are the regions into which the graph subdivides the plane. One of them is infinite, and the others are finite. The number of faces is denoted ***f*** . For example, for the first graph shown f = 4, and for the fourth (the cube) f = 6.

One basic and important fact about planar graphs is Euler’s formula, $$v+ f = e+2$$ (check it for the graphs above). 

It has an interesting story. The ancient Greeks knew that this formula held for all polyhedra (check it for the cube, the tetrahedron, and the octahedron, for example), but could not prove it. 
***How do you do induction on polyhedra?*** 
***How do you apply the induction hypothesis? 
What is a polyhedron minus a vertex, or an edge?*** 

In the 18th century Euler realized that this is an instance of the inability to prove a theorem by induction because it is too weak, something that we saw time and again when we were studying induction. To prove the theorem, one has to generalize polyhedra. And the right generalization is planar graphs. 

***Can you see why planar graphs generalize polyhedra? Why are all polyhedra (without “holes”) planar graphs?***

***Connectivity***. 
Much of what we discuss in this note revolves around the notion of *connectivity*. A graph is said to be *connected* if there is a path between any two distinct vertices. For example, our residential network $G_3$ above is connected, since one can drive from any house to any other house via some sequence of direct roads. On the other hand, the network below is disconnected.

Proof. By induction on e. It certainly holds when e = 0, and v = f = 1.
Now take any connected planar graph. Two cases: 
• If it is a tree, then f = 1 (drawing a tree on the plane does not subdivide the plane), and e = v − 1 (check homework). 
• If it is not a tree, find a cycle and delete any edge of the cycle. This amounts to reducing both e and f by one. By induction the formula is true in the smaller graph, and so it must be true in the original one.

A ***simple graph***, also called a strict graph (Tutte 1998, p. 2), is **an unweighted, undirected graph containing no graph loops or multiple edges**

![[chrome_ayiirdNu1W.png]]
(Counterexample to Kempt's proof)
