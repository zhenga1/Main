Another type of vector field, called a force field, associates a force vector with each point in a region. An example is the gravitational force field that we will look at in:

Example 4.
==**1 Definition:**== 
Let $D$ be a set in $R^2$ (a plane region). A **vector field** on $R^2$ is a function $F$ that assigns to each point $(x, y)$ in $D$ a two-dimensional vector $F(x, y)$.

**==2 Definition:==**
Let $E$ be a subset of $R^3$. A **vector field** on $R^3$ is a function $F$
that assigns to each point $(x, y, z)$ in $E$ a three-dimensional vector $F(x, y, z)$
$$F(x, y, z) = P(x, y, z)i + Q(x, y, z)j + R(x, y, z)k$$
![[Acrobat_Nc1GAI7yZw.png]]

![[Acrobat_GXwha9H3US.png]]

![[Acrobat_t9NiFgi8ec.png]]
![[EpicPen_fDoDXa3yu8.png]]![[EpicPen_fDoDXa3yu8 1.png]]

![[Acrobat_ZdCCs7Bfou.png]]
![[Acrobat_fZR3naetjY.png]]


![[Acrobat_PKpZtNxq7I.png]]

Two other line integrals can also be obtained, they are obtained by replacing $\Delta s_i$ for either the expression  $\Delta x_i = x_i-x_{i-1}$ or $\Delta y_i = y_i-y_{i-1}$

They are called the **line integrals of *f* along *C* with respect to *x* and *y**

![[EpicPen_Jym78r1bbG.png]]

![[EpicPen_itUi2Dhxdp.png]]
**Theorem 2**
Let $C$ be a **smooth curve** in space defined by the vector valued function $\vec{r}(t) = (\vec{x}(t),\vec{y}(t))$, where $t$ ranges from $(a,b)$.   Let $f$ be a differentiable function with $2$ or $3$ variables who's gradient vector $\nabla f$ is continuous on $C$. Therefore, we have the **multidimensional equivalent** of the **fundamental theorem of calculus**. 
$$\int_C \nabla f dr = f(r(b))-f(r(a))$$

We see that, in general, the expression is:
$$\int_{C_1} F dr \neq \int_{C_2} F dr$$
However, the following expression:
$$\int_{C_1} \nabla f dr = \int_{C_2} \nabla f dr$$
is true for any such $C_1,C_2$ that have the same initial starting point and ending point.

![[EpicPen_zRsjHX23Dv.png]]
![[EpicPen_Qnmo8B9KST.png]]
Work done by a **conservative force field** (such as the **gravitational** or **electrical** field) as it moves an object around a closed path is 0.

The following theorem says that **the only vector fields that are independent of path** are **conservative**. It is stated and proved for plane curves, but there is a similar version for space curves. 

We assume that $D$ is ***open***, which means that for every point $P$ in $D$ there is a disk with center P that lies entirely in $D$. (So $D$ doesn’t contain any of its boundary points.) In addition, we assume that $D$ is connected: this means that any two points in $D$ can be joined by a path that lies in $D$.

**Simple curve:** A curve that doesn't intersect itself anywhere between its endpoints. ![[EpicPen_8IqUVtIdDQ.png]]
![[Acrobat_tAm2tF6JnL.png]]

**Green’s Theorem** gives the relationship between a line integral around a simple closed curve $C$ and a double integral over the plane region $D$ bounded by $C$. (See Figure 1. We assume that $D$ consists of all points inside $C$ as well as all points on $C$.) In stating Green’s Theorem we use the convention that the positive orientation of a simple closed curve $C$ refers to a *single counterclockwise traversal* of $C$. Thus if $C$ is given by the vector function $r(t), a \leq t \leq b$, then the region $D$ is always on the left as the point $r(t)$ traverses $C$.
![[Acrobat_s9Xlx1FHdf.png]]
(See Figure 2.)
**Counterclockwise:** or **Positive Orientation**.
Meaning: **the area** is always to the left of the closed curve

Green's theorem:
$\int_C Pdx + Qdy = \int \int_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}) dx dy$ 
![[chrome_KHEA6btt0z.png]]

![[Acrobat_T9GNOsyf6k.png]]

**Divergence:** 
- The net amount of *imagined fluid* flowing in (negative divergence) or out (positive divergence) to an infinititesimaly small neighbourhood around a point in region D. 

A region is simply connected **if every closed curve within it can be shrunk continuously to a point that is within the region**. In everyday language, a simply connected region is one that has no holes

**Definition for Simply Connectedness**
- A region $D$ is **simply connected** if:
	- Any two points $P_1,P_2$ within $D$ can be connected with a curve $C_1$ whose points are entirely in $D$
	- All points within a closed curve $C_1$ entirely within $D$ must be in $D$ as well


# Equivalence Loop
![[chrome_wbhXasexkE 1.png]]
Fundamental theorem:
![[chrome_FXculUsvRf.png]]
# Summary:
1D input $\rightarrow$ over 1D domain 
- Integral of **derivative** over **object** = **function** over **object boundary**
- $\int_a^b \frac{df}{dx} (x) dx = f(b) - f(a)$ 
2D input (vector space) $\rightarrow$ over 1D domain
- Integral of **derivative** over **object** = **function** over **object boundary**
- $\int_{t_1}^{t_2} \nabla f dr = f(r(t_2)) - f(r(t_1))$
2D input space $\rightarrow$ over 2D domain (a region)
- Greene's theorem
- $\int_{C} F d\vec{r} = \int_{C} F\cdot T ds= \int \int_D (\frac{dQ}{dx} - \frac{dP}{dy})dx dy = \int \int_D (\nabla \times F) \cdot \vec{k} dA$
- $\int_C F\cdot \vec{n} ds = \int_C <P,Q> \cdot <y'(t), -x'(t)> dt$
- $= \int_C Py'(t) - Qx'(t) dt = \int_C Pdy - Qdx$
- $= \int \int_D \frac{dP}{dx} + \frac{dQ}{dy} dx dy = \int \int_D \nabla \cdot F$

Is it possible to go higher?, integrate over 

![[chrome_E1RBZiLHC3.png]]


A surface integral of this form occurs frequently in physics, even when $F$ is not $\rho v$ , and
is called the surface integral (or lux integral) of $F$ over $S$.

Definition:  If $F$ is a  continuous vector field defined on an oriented surface $S$ with unit normal vector $n$, we have that the surface integral of $F$ over $S$ is basically:
$$\int_S \int F dS = \int_S \int F\cdot n dS$$
In other words, we have:
$$\int_S \int F dS = \int_S \int F \frac{r_u \times r_v}{|r_u| \times |r_v|}dS$$
$$=\int_S \int F \frac{r_u \times r_v}{|r_u| \times |r_v|} |r_u\times r_v| dA$$
$$=\int_S \int F \times r_u\times r_v dA$$
Another application of surface integrals occurs in the study of heat flow. Suppose the
temperature at a point $(x, y, z)$ in a body is $u(x, y, z)$. Then the heat flow is defined as the
vector field
$$F = -K\nabla u$$

**Surface integral of vector field** = **Surface integral of the Normals to the vector field**

**Positive orientation:** An orientation along a boundary curve which always keeps the interior of the curve to the left of the curve itself.





