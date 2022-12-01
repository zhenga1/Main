**Last Class**
A surprising circuit
![[chrome_vTI43Jx12i.png]]
$u_2 = \frac{R_3}{R_1+R_3} V_s$
$u_3 = \frac{R_4}{R_2+R_4} V_s$

Now we assume that:
$R_3 = kR_1$
$R_4=kR_2$ 

Power supply keeps U in wires equal to $V_s$ regardless of how many branches we have!
$u_2 = \frac{kR_1}{R_1+kR_1}V_s$
So therefore:
$u_2=\frac{k}{1+k}V_s$

So therefore we also have:
$u_2=u_3$

![[chrome_pWtmsPJ95f.png]]

![[chrome_Z6f0847pq0.png]]
![[chrome_cZUBNMhS2z.png]]
We must have
$V_{el5} = U_2-U_3$ (Voltage Def)
*Bold Assumption*
$V_{el5} = 0$
If $R_5$, the resistor between $V_{el5}$ is zero(i.e.) the thingy is a wire, then we must have that the circuit would just take the path of least resistance.

**2D Touch Screen**
![[chrome_Wzu6S0uw3u.png]]
So essentially, a *2D Touchscreen* is made via two different materials. The screen is made of a high density material(i.e. poor conductor), whilst the bottom is low density material. 

Total length(L)
$L = L_{touch} + L_{rest}$
We must have that:
$R = \frac{\rho L}{A}$
$V_{out} = U_{mid}$

So essentially there are two plates.
Bottom plate has low $\rho$ and therefore high conductivity, whilst upper plate has high $\rho$ and low conductivity.
![[EpicPen_HptjYSi0lU.png]]
$U_{left} = U_{mid} = U_{right}$
Since we have that the thing is basically just another voltage divider.
$U_{mid}=\frac{R_{touch}}{R_{rest}+R_{touch}}V_s$
$U_{mid}=\frac{pL_{touch}/A}{pL_{rest}/A+pL_{touch}/A}V_s$
So we have:
![[EpicPen_634k20rnnQ.png]]
$U_{mid} = \frac{L_{touch}}{L_{rest}+L_{touch}}V_s$
This gives us the vertical position on the screen
![[EpicPen_U1GkD8NBJM.png]]
![[EpicPen_2pf2mIRiND.png]]

The bottommost one gives the horizontal information about the $U_{mid}$

How to connect the voltmeters to measure?

**Equivalence**
Two circuits are equivalent if they have the same IV relationship
If you connect a phone to a power source, then you can measure an IV curve. If you then connect that to a box (charging box), you can also measure an IV curve. If the two IV curves are the same, then the two circuits would be equivalent.

*Example*:
Wire and Voltage source that provides zero voltage is basically equivalent. 
![[EpicPen_meWrYgm0rx.png]]

Similarly, Current Source and open circuit(current source with zero current) are equivalent.
![[EpicPen_r5aNw2kelo.png]]

As long as the IV relation is the same, circuits are equivalent!
![[EpicPen_VbwbAhx4o8.png]]

$V_{el} = V_s+V_r$
$V_{el} = V_s+I_{el}R$
$I_{el} = \frac{1}{R}V_{el}-\frac{V_s}{R}$
Current going through the loop should be $I_{el}$. Now let us isolate current in this equation

Slope of the current is $\frac{1}{R}$
$I_{el} = \frac{1}{R}(V_{el}-V_s)$
I MUST KNOW:
Thevenin and Norton Equivalent
very well.
![[EpicPen_raVur7PG5E.png]]
![[EpicPen_447lF0A8zt.png]]
**Thevenin and Norton Equivalent**
How to find $V_{Th}$: 
- Connect open-circuit -> $I=0$
- Find $R_{Th}$, done so by finding the slope of the $VI$ characteristic curve
	- zero-out independent source
![[EpicPen_zWWzfh488g.png]]

