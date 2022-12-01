**Last class 9/15**
Current: I
Voltage: V
Resistance: R

![[chrome_YdcguR629y.png]]
![[chrome_2r2VGbKUJL.png]]
TODAY:
- Rules for solving *KCL; KVL*  
- Circuit analysis
- First operator!

**Rules for circuit analysis: Kirchoff's Voltage Law KVL**
*Sum of voltages across the elements in loop equal zero*
![[chrome_kyh6f7T7ze.png]]
$V_{el1} - V_{el2} - V_{el3} - ...-V_{eln} = 0$
$+ to -$ is positive voltage (difference) between the positive side and the negative side
![[chrome_HaAyHCd2Kt.png]]

**Rule for circuit analysis: KCL within the element**
- The current flowing into an junction must equal the current flowing out
![[chrome_e9fyHZ6w79.png]]
Since the junction point cannot contain any current, we see that:
$I_{el5}+I_{el6} = I_{el7}$

# Circuit Analysis Algorithm
Voltage = difference of two potential
Find: currents through elements and potentials of inputs/outputs of each element (junctions)
We see that:
- $I_{elem}$ always goes into a (+) or go out a (-) terminal
Passive sign convention
![[chrome_axTmty8x8m.png]]
**STEP 1**
- Pick a reference node and label it as the 0 potential. All voltages measured relative to this node.
![[chrome_34M3aQUzT1.png]]
- The ground never disappears, we never run out of electrons
- Ground node tells you where the reference (for measuremnet of potential)  is
- Label the potential in the second (or other) nodes as $u_1,u_2,...u_n$
*Total freedom in the way you label currents*

Example:
![[chrome_K5gN8pTABj.png]]
- Can also change the direction of the current

**Circuit analysis Algorithm: Step 4**
Add signs + and - element voltages to each element following the passive sign convention
Have to commit to the way that the current flows. Since current always flows from + to -, the corresponding elements must always be labeled also in that direction, where the current will point from + section to - section.

Use KCL to fill as many rows of A as possible (linear independence)
$V_{el2} = i\times R_{el2}$
$V_{el2} = V_1$
$V_1 = I_2\times R_{el2}$
Hence:
$I_1-I_2 + (0)V_1=0$
$R\times I_2 +(-1)V_1=0$
$V_1=V_s$

$$\begin{bmatrix}1&& -1&& 0\\0 && R&&-1\\0 && 0 && 1\end{bmatrix} \begin{bmatrix}I_1\\I_2\\V_1\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}$$

Resistor by Ohms law, we have $R=V/I$
To get the third 

**Electrical Circuit Analysis Algorithm(tool)**
SPICE: (Simulation Program with Integrated Circuit Emphasis): started as a student project at Berkeley!

Now the basis for open-source electronic circuit simulation, to design and model device characteristics and check circuit boards
![[chrome_nBjSaN4fmB.png]]
*Cadence and Synopsis* - developed at Berkeley

Design and Simulation -> create a design, do the simulation, and afterwards sent straight to factories

Know how to code and circuits -> dominant person

Famous professor: *Alberto L. Sangiovanni-Vincentelli*

**Node voltage analysis - Voltage Divider**
(operator) -> makes circuit analysis faster

Step 1: Pick a node and label it as ground
Step 2: Label the other nodes as $u_1,u_2$
Step 3: Label the current through every non-wire element in the circuit with $I_n$
Step 4: Add +/- labels on each non-wire element, following the passive sign convention.
Current within the wire is dependant on the rest of the circuit
![[chrome_kIhIJKhl0J.png]]
**Passive sign convention:** the current enters at the positive terminal and exits are the negative terminal
Step 5: Solve for unknowns by setting up the relationship $A\vec{x} = \vec{b}$ where $\vec{x}$ consists of the unknown currents and potentials.
$\vec{x} = \begin{bmatrix}I_1\\ I_2 \\I_3 \\u_1 \\u_2\end{bmatrix}$
You need exactly 5 equations to solve for 5 unknowns.
By KCL:
$I_1 + I_3 = 0, <1,0,1,0,0>$
$I_1 = I_2, <1,-1,0,0,0>$

So, 2(linearly independent) equations have been found, with row vectors:
$<1,-1,0,0,0>, <1,0,1,0,0>$


By KVL:
$V_{el1} = U_1 - U_2$
$V_{el2} = U_2 - 0 = U_2$
$V_{el3} = U_1 - 0 = U_1 = V_s$
Element $I\times V$

We also have by OHM'S law:
$V_{el1} = R_1\cdot I_1$
$V_{el2} = R_2\cdot I_2$
$V_{el3} = V_s$

Combining the equations, we have:
Eq1: $U_1-U_2 = R_1\cdot I_1, <R_1,0,0,-1,1>$
Eq2: $U_2 = R_2\cdot I_2, <0,R_2,0,0,-1>$
Eq3: $U_1 = V_s, <0,0,0,1,0>$

The final matrix
$$\begin{bmatrix}1&&-1&&0&&0&&0\\1&&0&&1&&0&&0\\R_1&&0&&0&&-1&&1\\0&&R_2&&0&&0&&-1\\0&&0&&0&&1&&0\end{bmatrix} \begin{bmatrix}I_1\\I_2\\I_3\\U_1\\U_2\end{bmatrix} = \begin{bmatrix}0\\0\\0\\0\\V_s\end{bmatrix}$$

Then solving this difficult equation gives the desired unknowns and the answer.

![[WhatsApp Image 2022-10-04 at 1.58.55 PM.jpeg]]












