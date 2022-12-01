![[Zoom_t1lfFrlDjy.png]]
$\int^2_1 \int^3_0(x^2y) dydx = \int^2_1 [\int^3_0 x^2y dy] dx$ 
$=\int^3_0 (x^2y)dy = \frac{x^2y^2}{2}$
![[ShareX_ledh0ok4Pq.png]]
Switching order of integration
**Fuilbini's theorem.** The order of integration of a multidimensional integral doesn't matter. 
![[ShareX_jfcbjePQhs.png]]
**Double integral over complicated regions**
![[ShareX_jfcbjePQhs 1.png]]

The order doesn't matter, but the limits of integration changes if the order changes, so you need to accomodate that to get the same area A
![[ShareX_bIrU0mPbbY.png]]

$\int^1_0 \int^1_y 2dx dy= \int^1_0 2-2y dy = 2*1-1^2=2-1=1$
![[ShareX_RuirTICYQv.png]]

$\int^2_0 \int^4_{x^2} x^2y^3dy dx = \int^2_0 \frac{x^2 y^4}{4} =$ $\int^2_0 \frac{256x^2}{4} - \frac{x^{10}}{4}=256/12*2^3-2^{11}/44$ $= 124.121212121$
![[ShareX_PRhdlz2e3i.png]]

![[ShareX_EZ9lRpL5hD.png]]

Trick **with multivariable integration** is always to think before slicing
- Set up the integral of **w(x,y) = sin(xy)** over the region A.
![[ShareX_OC8RxscNT8.png]]
Sometimes, there is a much greater advantage in integration over one direction vs integration over the other, such as when integrating over one axis is better than the other way

**Fubini's theorem**
If we have $f(x,y)$ continuous on the rectangle $R = \{(x,y) |  a\leq x \leq b, c\leq y \leq d\}$, then:
$\iint_R f(x,y) dA = \int^b_a \int^d_c f(x,y) dydx = \int^d_c \int^b_a f(x,y) dxdy$
More generally, this theorem holds true as long as $f$ is bounded on $R$, $f$ is only discontinous on a finite set of smooth curves, and the iterated integrals exist. 