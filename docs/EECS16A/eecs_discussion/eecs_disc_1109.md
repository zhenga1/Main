**==Voltage summer:==**
![[Pasted image 20221109121311.png]]
Adding the voltage **contributions** of each voltage source to the output voltage $V_{out}$

==**Unity Gain Buffer**==
![[Pasted image 20221109121623.png]]
$V_{in} = V_{out}$ by the golden rule. 

We see that this form of buffer is incredibly useful when we want to:
- Use a voltage
- Avoid current loading

==**Non-inverting**==
$V_{out} = V_{in}(1+ \frac{R_{top}}{R_{bottom}}) - V_{ref} \frac{R_{top}}{R_{bottom}}$

*Designing methods:*
1. Read spec *carefully*
	1. What are the input and outputs 
		1. Pay attention to specific numbers
	2. What components can we use?
	3. Other constraitns?
2. Plan your approach (block diagram)
3. Implement: choose component
4. Check your design 
	1. Check for loading

First multiply by 1/2, keep that result, keep the loading block $V_x$, then 
![[WhatsApp Image 2022-11-09 at 12.24.36 PM.jpeg]]
