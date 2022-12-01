#r/discussion
- Discussion notes: 8B![[Anish's Discussion 8B.pdf]]

# Discussion 8B 10/19
```jupyter
print("Hello world i am cool")
```

**Main Idea** - simplify circuits in order to ease circuit analysis and 

**Resistor Equivalence**
All elements in series with each other have the same current(I) flowing through them. 
![[EpicPen_MH7q30NlVq.png]]
So, we see that the equivvalent resistance of the 4 resistors is $R*$, where:
$R* = R_1+R_2+R_3+R_4$

However, for the other example:
![[EpicPen_yc3kI4WZxa.png]]
We see that resistors in parallel, the three resistors can be written as an equivalent resistance $R_p$, where

$R_p = R_1 || R_2 || R_3$. We have $||$ is the parallel operator

Hence,
$\frac{1}{R_p} = \frac{1}{R_1} +\frac{1}{R_2} + \frac{1}{R_3}$
Its very difficult to solve circuit components with only the KCL and KVL rules

# Superposition
**Motivation:** Break down circuit with multiple sources into several simpler circuits -> another tool for circuit analysis
1. Identify each independent current/voltage source within the circuit
2. For each source identified in step (1), draw an equivalent circuit by zeroing out all other independent sources.
	1. Zeroing out voltage source: 
		1. $V_s$ . Assuming $V_s=0$, then the voltage source turns into a wire
	2. Zeroing out current source:
		1. $I_s$. Assuming $I_s=0$, then the current source turns into an open circuit
![[WhatsApp Image 2022-10-19 at 12.22.15 PM.jpeg]]
So then, through superposition theorem, we have that we can let $I_s$ just simply be an open circuit.

So then the voltage we want to find due to the component $V_s$
$V_{R1}=\frac{R_1}{R_1+R_2}$ . Assuming $I_s$ is zeroed out, we have:
$V_{R2}=\frac{R_2}{R_1+R_2}$, $V_{R3}=0$

Now we must zero out the $V_s$, making $V_s=0$, so now we have:
![[WhatsApp Image 2022-10-19 at 12.27.57 PM.jpeg]]
So therefore we have: $(R_1,R_2)$ are in parallel.
So therefore we have:
$V_{R3} = I_sR_3$, ($R_3$ is in series with $I_s$)
$I_1 = \frac{R_2}{R1+R2}I_s$  (Current divider)
$V_{R1} = -V_{R2}$ (Parallel resistors with opposite polarity)
$I_2 = -\frac{R_1}{R_1+R_2}I_s$

So therefore:(by ohms law)
$V_{R1} = I_1R_1$
$V_{R2} = I_2R_2$

$V_{R1} = \frac{R_1R_2}{R_1+R_2} V_s$ 

**Thevenin and Norton equivlent**
**==Thevenin== To solve:**
1. Find $V_{th}$ by finding $V_{AB}$ in a given circuit.
	1. $V_{th} = V_{ab}$ , and $V_{AB}$ is the open circuit voltage
2. Zero out all independent sources and apply a test current $I_{test}$ through the terminal or $V_{test}$ around it
	1. $R_{th} = \frac{V_{test}}{I_{test}}$
**==Norton== To solve:**
1. Find $I_{no}$ by finding $I_{AB}$ in given circuit
	1. $I_{no} = I_{sc}$ 
2. Zero out all independent sources and apply a test current $I_{test}$ through a terminal or $V_{test}$ across it
	1. $R_{th} = \frac{V_{test}}{I_{test}}$
Biggest drawback here:
- Don't have access to certain node voltages and currents, which we previously could have access to/solve for before the Thevenin/Norton assumption
![[WhatsApp Image 2022-10-19 at 12.49.05 PM.jpeg]]
We see that $V_{ab} = u_a-u_b=u_a-0=u_a=\frac{0.5}{1+0.5}\cdot 5V=1.67V$

Norton equivalent:
By Ohm's law, we have 












