# Op- Amp in Negative feedback
1. $V_d = V+ - V- = V_{in} = V_{s}$
2. $V_{out} = A V_d$
3. $V_{fb}=\frac{R_2}{R_1+R_2} V_{out}$
Buffer circuit 
$V_{out} = A (V_{in} - f V_{out})$


$A_v = Gain =$
$V_d = \frac{V_{out}}{A}$ , $V_d = \frac{V_{in}}{1+Af}$, $V_d = 0$. In an ideal amplifier, we will always have that 
$A \rightarrow \infty$ 

If you have an **ideal operational amplifier**, the gain is infinite

$V_d = 0, V_d = (U+) - (U-)$ , $U+ = U-$

![[EpicPen_FlGcX3Ge2Y.png]]
We always have that, since there is infinite resistance (essentially an open circuit), that $I+ = I- = 0$

# Pretty Useful Table
![[WhatsApp Image 2022-11-03 at 1.04.56 PM.jpeg]]

# Checking for Negative Feedback
**==Step 1==** - Zero out all independent sources : replacing volage sources with wires and current sources with open circuits as in superposition
**==Step 2==** - Wiggle the output and check the looop - to check how the feedback loop responds to a change. 
- If the error signal decreases, the output must derease also. *The circuit is in negative feedback*
- If the error signal increses, the output must also increase. *The circuit is in positive feedback*
![[EpicPen_ZSS2sJfMmq.png]]
IN left example, we must:
Apply disturbance:
$U_3$ increases
$V_4$ increases $(V-)$
$V_3$ decreases (NFB) -> Negative feedback. 


# Lecture Notes prepared

**==Negative feedback==** is used just about everywhere, including electronics, biology, mechanics, robotics, and more. **Negative feedback** occurrs when some function of the output of a system is fed back into the input, in a way to keep the output at some finite value. 

Let’s turn this high level description into a more mathematical one. Concretely, we want to get a **certain known gain** out of our op amp. Currently we have an op-amp with some very large uncertain internal gain. 

We can describe this problem using a block diagram; a collection of drawings (mathematical in nature) that operate on *quantities of interest* using *simplified representations*.

Let’s take a look at a generic block diagram for negative feedback systems
![[EpicPen_9pOq6nxjri.png]]

**Golden rule applies**
$U+ = U-$  $I+ = I- = 0$
![[WhatsApp Image 2022-11-03 at 1.26.12 PM.jpeg]]
We see that the golden rule applies, so basically 
$U- = 0$. 
Essentially in the steady state:
$U_2 = 0$ 

1. $u_1 = V_{in}, u_2 = 0 = u-, u_3 = V_{out}$
2. Element Def 
	1. $V_{R1} = R_1 \cdot I_1$
	2. $V_{R2} = R_2 \cdot I_2$
3. Voltage Def.
	1. $V_{R1} = U_1 - U_2 = U_2$
	2. $V_{R2} = U_3 - U_2 = U_3$ 
4. KCL?. $u_2$ is the node here that is important.
	1. $I_1 + I_2 = (I-)$
	2. $I_1 = - I_2$

$V_{in} = V_1 = I_1 R_1$
$V_{out} = V_3 = I_2 R_2$
$I_1 + I_2 = 0$
$\frac{V_{in}}{R_1} + \frac{V_{out}}{R_2}=0$

![[EpicPen_JLEhVV9L5t.png]]
$GR2: U+ = U-, U_2 = U-$ 
$U+ = 0 => U_2 = 0$

So we have:
$GR1 + KCL (I_1 = I_2 + I-)$
$\frac{-U_1}{R_1} = \frac{U_3}{R_2}$
$\frac{V_{out}}{V_{in}} = -\frac{R_2}{R_1}$

**Example Circuit 2 (Trans-resistance amplifier)**
![[EpicPen_QtNDxkozDX.png]]
![[EpicPen_sAkqELsCv0.png]]
So here we are controlling the current, fixing the current across the resistor $R$ to be $I_{in}$. 
We must have:
$U+ = U-$ 
$U+ = 0 \rightarrow U- = 0$

Apply golden rule 2:
$\frac{-V_{out}}{R} + (-I_{in}) + I-=0$
$\frac{-V_{out}}{R} = I_{in}$,  $\rightarrow$  $V_{out} = -I_{in}R$

$$\frac{V_{out}}{I_{in}} = -R$$
![[WhatsApp Image 2022-11-03 at 1.55.57 PM.jpeg]]
![[WhatsApp Image 2022-11-03 at 1.58.33 PM.jpeg]]

![[WhatsApp Image 2022-11-03 at 2.02.14 PM.jpeg]]

Factor of multiplication $A$ is 

==**GAIN**== is the multiple of the **magnitude of input voltage** of **the output voltage**









