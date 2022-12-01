#r/discussion
- Discussion notes: link

# Discussion 6B
```jupyter
print("Hello world i am cool")
```
**Node voltage Analysis(NVA)**

1) Ground Node
2) Label all Node Voltages
3) Label all currents and voltages for each element following passive sign convention
4) Use current+voltage sources to label nodes/branch currents
5) Use KCL, Ohm's Law to write equations
6) SOlve using substitution,/Gaussian Elimination

*Review:*
Voltage Sources:

Current Sources:

Unknowns: Node potentials and element currents

**Passive Sign Convention:**
- Current flows into the positive terminal and out of the negative terminal of any circuit element

**Ohm's Law**
![[EpicPen_b1MXeotTvW.png]]
$V_R = I*R$

**Kirchoff's Current Law(KCL):**
The sum of all currrents coming into a node is equivalent to the sum of all urrents leaving a node.
![[EpicPen_Zskpo6p6aC.png]]

So we must have:
$I_1+I_2+I_3+I_4=0$

**Kirchoff's Voltage Law(KVL)**
Sum of voltage gains across all elements in a closed loop is zero
-> aka. sum of voltage drop is zero.

What I always do (by personal convention):
1) Currents flowing downward through vertical components
2) Currents flowing rightward through horizontal components

(d) Draw the +/- labels on every element. What convention should be followed?
**Must follow passive sign convention.**
-> Current flows into positive terminal and out of negative terminal

We *usually do not* perform KCL calculations on the ground node, typically just the other nodes.

This is because whatever equation can be obtained using KCL on the ground node is likely already going to be obtained with the KCL equations on the other nodes.

No of KCL equations = No of non-reference ndoes
From circuit above, we have 1 KCL equation

KCL on node $u_1: I_0 = I_1 + I_2$
(Current entering = Current leaving)

$I_0 = I_s$($I_0$ in the same direction as $I_s$)
$V_1 = I_1R_1$
$V_2 = I_2R_2$
$V_0 = 0-u_1 = -u_1$

$I_0 - I_1 - I_2 = 0$ { from part e}
$I_s - \frac{u_1}{R_1}-\frac{u_1}{R_2}=0$ { from part f}
$5A - \frac{u_1}{5}-\frac{u_1}{10}$ 
$5A = \frac{u_1}{5}+\frac{u_1}{10} = u_1(\frac{1}{5} + \frac{1}{10}) = u_1 \frac{3}{10}$
$u_1 = 5(\frac{10}{3}) = \frac{50}{3} = 16.67V$
