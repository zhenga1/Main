![[chrome_LqqmZE49Rb.png]]
**Simple Circuit 3**
![[EpicPen_Ariqg42Qrf.png]]

$u_1=$
**Goal of EECS16A**: Solve for steady state situation

$V_c = C$, $C$ is a constant, since it is steady state
$I_c=C\frac{dV_c}{dt} = C\cdot 0$
$I_c+I_r=0$ 

Ohm's law 
$V_r = I_r\cdot R=u_1$
$u_1-0=0$, so $u_1=0$

If current $I= 0$, we basically have that the capacitor is an **open-circuit**

# Equivalent Circuits with Capacitors
Step 1: find $V_{th}$ and $I_{no}$

Step 2: We have:
$$C_{eq} = \frac{I_{elem}}{\frac{dV_{elem}}{dt}}$$
![[EpicPen_H2aBC673FK.png]]
![[EpicPen_Y3flk1ztgf.png]]

However, we know that current $I = dQ dt$ . 
Hence,
$I = C dVC dt$. (4) 
Thus, the current through a capacitor is the product of the capacitance and the rate of change of the voltage across the capacitor. 
This yields the following graph, with slope equal to C:
![[chrome_LxKzNokLZ8.png]]
An important implication of this is that current is only flowing through the capacitor if the voltage across the capacitor is changing with time. If the voltage is no longer changing, then the current through the capacitor will equal 0.

How can we solve for the voltage across the capacitor? In other words, how do we find $V_C(t)$? There are many ways to solve Equation 4, but we will use separation of variables and then integrate both sides, shown below. Note that it’s okay if you haven’t seen this technique before, it is not required for this class.
![[chrome_puiuu0CUd8.png]]
![[chrome_7axqU2AQN0.png]]
We have that by KVL:
$V_{C1} = u_1-0=V_{test}$
$V_{C2} = u_1-0=V_{test}$
![[chrome_wLeFfw5lBD.png]]
![[chrome_SQsnzAiU5L.png]]
In essence, we have:
$C = \frac{Q}{V}$
$C = \frac{Q/t}{V/t}$
$C = \frac{I}{V/t}$
**Capacitors in Series**
![[chrome_unR6pkPPy1.png]]

![[chrome_KNiXIrJz1A.png]]
