**Resistive Touch Scereens**
Squishy films -> They are for *Mechanical Actuation*
When you have a good screen, they are hard, they have glass on top. 
![[chrome_JMnEnx0URe.png]]
Film is transparent and conductive. There is usually always conditions to which the film must satisfy to be transparent and flexible and conductive. 
**Conducting lines** formed by carbon elements.
Array of lines with pads that will be connected via rigid screens. 

*Squishinesss* of the flexible top film(PET) -> allows to make connection between the top plate and the bottom plate, so there can be current/voltage measured.

![[chrome_WDL1E7z1DE.png]]
There are different materials/types of metal
*Electrical Resistivity* is the inverse of *electrical conductivity*. 
Equation $R=\frac{pL}{A}$, where 
$p =$conductivity
$L/A$ is the geometric parameters(i.e. the property of the wire)

Wire properties depend on materials choice.
We like wires cuz we know the IV characteristics of the wire.

**Modeling** of the **Resistive Touch Screen**
Problem: to find the location of touch.
![[chrome_73ir3tVzfZ.png]]
- Go from **mechanical** to **electrical** quantity
- Want to measure $\frac{L_{touch}}{L}$
- ==$L_{touch}$ unknown==
- ==Total length = $L$, also $L_{touch}+L_{rest} = L$==

Connection made between the **red** surface and the **black** surface

How to find $L_{touch}$?
- Big brain method:
	- Assume the red and black thingy (above) have fixed resistivity. Also assume that red and black ends have a fixed voltage drop. Then when the touch is activated, we have a closed circuit with resistance we can calculate w.r.t $L_{touch}$ . So then we can figure out $L_{touch}$ based on the resistivities and others.
![[chrome_ALKWySmXg7.png]]
So we have equations:
- ==(1)$R_1=p\times \frac{L_{rest}}{A}$,==
- ==(2)$R_2=p\times \frac{L_{touch}}{A}$,==
So,basically a touchscreen is kinda like a **voltage divider**
![[chrome_NWzGbfkZFb.png]]
$U_{mid} = \frac{p\cdot L_{touch}/A}{p\cdot L_{touch}/A+p\cdot L_{rest}/A}\cdot V_s$
So we have the expression:
$U_{mid} = \frac{L_{touch}}{L_{touch}+L_{rest}}V_s$
$U_{mid} = \frac{L_{touch}}{L}V_s$

![[chrome_zPhqUfefwb.png]]
Now we have conducting plate(the black thingy).
![[chrome_JTjOsDWObi.png]]

$el_1:$ wire - The box 
$el_2,el_3:$ open-circuit, the red bounded boxes on the left and right side
![[EpicPen_IWxbYhhEXD.png]]
$\rightarrow$ **Model 1**
- Add an ideal wire(assume 0 resistance) to represent bottom plate

**How to know where touch is happening given these constraints?**
Voltage Def:
$el_2, V_{el2} = U_1 - 0$
$el_1, V_{el1} = U_{mid} - U_1$
So we see that:
$U_{mid} = V_{el1}+V_{el2}$

However, we can easily see that $V_{el1}=0$ given that $V_{el1}$ is across a wire. So, we have:
$U_{mid} = V_{el2} = U_1$

$\rightarrow$ **Conclusion**
- By measuring $U_1$ or $V_{el2}$, we can get easily the voltage required for $U_{mid}$, and thereby solve for the position(L) of the touch position using the formula ==(1)==

Assume both **top** and **bottom** plates are imperfect

![[EpicPen_GHFiUxEqMz.png]]
Adding a resistor doesn't matter as there is no current flowing through anyway. So basically since its an open circuit, the voltage is the same across the resistors $R_4,R_3$ and so basically the voltage is always $U_{mid}$ 

![[EpicPen_ZGg8GXxV4Y.png]]

**A surprising circuit**
![[EpicPen_H1Xjy0xqzp.png]]
What are $u_2$ and $u_3$?
![[EpicPen_vqlOwWTtw9.png]]
We have, by the diagram above:
$u_2 - 0 = \frac{R_3}{R_1+R_3}\cdot (u_1-0)$, since $V_s = u_1$ 
$u_3 - 0 = \frac{R_4}{R_2+R_4}\cdot (u_1-0)$
$u_1-0=V_s$