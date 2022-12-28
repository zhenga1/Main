The converse of Theorem 5 is true only for a special type of region. To explain this, we first need to explain the concept of a **simple curve**, which is a curve that doesn’t intersect itself anywhere between its endpoints. 
![[Acrobat_MsRdwTVFJB.png]]


In Theorem 4 we needed an open connected region. For the next theorem we need a stronger condition. A **simply-connected region** in the plane is a connected region $D$ such that every simple closed curve in $D$ encloses *only* points that are in $D$. 

Notice from Figure 7 that, intuitively speaking, a simply-connected region contains no hole and can’t consist of two separate pieces.


We have that:
$\because r_u \times r_v = -r_v \times r_u$
$\therefore \int_S \int F \cdot dS = \int_S \int F \cdot (r_u \times r_v) = -\int_S \int F \cdot (r_v \times r_u)$
But ==shouldn't the above be a contradiction?==
