#r/lecture
- Lecture notes: link

# Lecture: 10/6
```jupyter
print("Hello world i am cool")
```

**Last Lecture**
- Solve circuits for the currents and node potentials
Learnt that 
Eq1: $I_1 + I_3 = 0$
Eq2: $-I_1 + I_2 = 0$
Eq3: $R_1\times I_1 - U_1+U_2 = 0$
Eq4: $R_2\times I_2 - U_2 = 0$
Eq5: $U_1 = V_s$
So, we learnt to solve the currents and the potentials
$I_1 = \frac{V_s}{R_1+R_2}, I_2 = \frac{V_s}{R_1+R_2}, I_3 = -\frac{V_s}{R_1+R_2}$
So, $U_1=V_s, U_2 = \frac{R_2}{R_1+R_2} V_s \rightarrow$ based on  Eq3.

One resistor is $48 \Omega$. 
The other resistors is $1 \Omega$
Across two resistors is $2 \Omega$ 
So we have $2V$ across those two resistors, and $1V$ across only one volts. 
So putting the system through 2 resistors, we had $3V$, but across only 1 resistor we have $1.5V$

![[WhatsApp Image 2022-10-06 at 1.03.23 PM.jpeg]]
Heat occurs because of the current that goes through the resistor.
We call the expression:
$$\frac{R_2}{R_1+R_2}$$
the operator of the matrix.

**How to think about Energy and Power in circuits?**
- **Current:** flow of charges(electrons moving from point A to B inside a material)
	- $I = dq/dt$
- It takes **energy** to move charge from A -> B Voltage
	- $V_{AB} = dE/dq$
- **Power:** the rate of change of electricity
$P = \frac{dE}{dq} * \frac{dq}{dt} = V*I$	
So we have that $V*A = W$, 
Voltage x Current = Watts

**Energy and Power**
$P_{el} = V_{el} \cdot I_{el}$
If element is a resistor
$P=V\cdot I = R\cdot I\cdot I = I^2R$
In a resistor, we know that the resistor is using/dissipating power $P$.
![[EpicPen_PpQq26vXqx.png]]
If we have:
$V_{el} = R\cdot I_{el}$
$I_{el} = \frac{V_{el}}{R}$
then we must have:
$P = V\cdot I = \frac{(V_{el})^2}{R} \geq 0$
![[EpicPen_VBa0pVuzEB.png]]
![[EpicPen_Rgk2nYZzUR.png]]

![[EpicPen_d04XRM4cXC.png]]

Power Elem load:
$P_2 = I_2\cdot V_2 (def)$
$P_L = (-I_s)\cdot V_2$
$P_L = (-I_s)\cdot V_s$
$P_s = I_s\cdot V_{el} (def)$ 
$P_s = I_s\cdot V_s$ 

Solution:
$P_L = -P_s$
$P_L+P_s = 0$

**How to measure Voltage and Current?**
![[WhatsApp Image 2022-10-06 at 1.15.36 PM.jpeg]]
![[chrome_M3LKjuh6x9.png]]

**Measuring VOLTAGE**
We will use KVL to obtain the relevant equations within the circuit.
Goal: $V_{meas} = V_{mistery}$
$V_{el1} = I \times R = I_{meas} \times R$
$KVL:V_{mystery} - V_{el1} - V_{meas} = 0$
$V_{mystery} = V_{el1}+V_{meas} = I_{meas}\times R + V_{meas}$
Only way we have $V_{mystery} = V_{meas}$ is when $V_{el1} = 0$

So, the green box, responsible for the measurement of the voltage difference, should be an open circuit.

Effectively when conneted to an open circuit, the measurement circuit is technically positive.

**Measuring CURRENT**
Our goal now is to measure $I_{mistery}$
![[chrome_M3LKjuh6x9 1.png]]

We would use KCL to measure the current. 
**KCL:** 
$I_{mistery} = I_R + I_{meas}$ 
If we let $V_{means}=0$, then we must have $I_R=0$ and therefore $I_{mistery} = I_{meas}$

**Touchscreens**
![[EpicPen_eAkPf9Iord.png]]
Indium Tin Oxide
![[EpicPen_qe8zJBWpQb.png]]
$3.7 \Omega$ 
= 0.7 Watts 
1 V and 5 Amps = 5 Wats




