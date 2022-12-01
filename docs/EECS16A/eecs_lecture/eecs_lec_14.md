#r/lecture
- Lecture notes: link

# Lecture: 10/18
```jupyter
print("Hello world i am cool")
```
**Last Class**
![[chrome_w5sAqrwfIN.png]]
![[chrome_jb3smUUsQw.png]]
So, our steps are:
1) Find $V_{Th}$: Connect open circuit -> $I = 0$
2) Find $R_{Th}$: Find slope zero-out independent source
Thevenin is an *open-circuit*, i.e. the voltmeter behaves as an open-circuit. 

What is the current in an open circcuit? zero. 

![[chrome_kYEumD59PI.png]]

**Thevenin Eq.** - Resistance in resistive source
If all I have, if I said that the resistor is nonzero, then the entire circuit is basically conecting a voltage source with a resistor

**Norton Eq.** - Current source is zero, so all I have left is a resistor. 

**Practice - Example 1**
*Step 1:* We see that all sources(current + voltage) are zero. We have two resistors. What is $V_{th}$? We see that it obviously is $V_{th} = 0$ hence. 

*Step 2:* Find $R_{th}$. To find $R_{th}$ we must have $R_1, R_2$ .
$R_2 = \frac{V_{test}}{I_{test}}$
In series means that *the same I flows through the elements*
![[chrome_87BoHi4THi.png]]
We see that the current source drawn above fulfills the following properties:
$I_{test} = I_1 = I_2$

Take the top node as $u_1$ and make bottom node as $0, GND$ , we can use equations to solve for $u_1$.
$KVL$ ->$u_1-0=V_{test}$ 

We assume $v_1$ is the voltage that goes through $R_1$. $v_2$ is the voltage going through $R_2$

Then we have 2 equations:
$u_1-0=V_{test}$ 
$V_{test} = v_1+v_2$
$V_{test} = R_1\times I_{test} + R_2\times I_{test}$
$(R_1+R_2) = \frac{V_{test}}{I_{test}}$

**Practice: Example 2**
We already know that $V_{th} = 0$, since the other side has no resistors there.
$V_{th} = 0$

**Reason:** Because the voltage is the interesting thing
Why we did **Thevenin** and not **Norton** 
-> **Thevenin** -> Analysis of the voltage
-> **Norton** -> Analysis of the current

We are going to connect the Voltage and the Current source
![[WhatsApp Image 2022-10-18 at 1.27.19 PM.jpeg]]
So we analyze this circuit. We have:
$V_{th} = 0$
$I_{test} = I_1+I_2$
As a result, we have:
$I_1 = \frac{V_1}{R_1}$;   $I_2  = \frac{V_2}{R_2}$
$I_{test} = \frac{V_{test}}{R_1} + \frac{V_{test}}{R_2} = I_1 + I_2$. So therefore:
$I_{test} = V_{test}\cdot \frac{1}{R_1+R_2}$

So therefore, the resistance is:
$\frac{V_{test}}{I_{test}} = \frac{R_1\cdot R_2}{R_1+R_2}$ -> This is called a **parallel operator**

**Circuit Analysis Method** 
==What happenes when we have multiple Voltage or Current Sources==
$V_{out}$ is the voltage between the two points in the circuit. 
![[chrome_mUaLcoTeQl.png]]
We assume that $u_1$ represents the voltage as specified. We therefore have that 
$u_1-0 = V_{out}$

1st step:  Compute a response to $V_1$(i.e. set $V_2=0$)
Now we have this circuit, here is the question:
What is $V_{out}$? This is the voltage divider. 
So therefore:
$V_{out} = \frac{R_2}{R_1+R_2}\cdot V_1$

2nd step: Compute a response to $V_2$(i.e. set $V_1=0$).
![[chrome_AoCH8PZaHn 1.png]]
$V_{out} = \frac{R_1}{R_1+R_2}\cdot V_2$
So therefore we have:
$V_{outtotal} = \frac{R_1}{R_1+R_2}\cdot V_2 + \frac{R_2}{R_1+R_2}\cdot V_1$
But then, we have that :
$\frac{R_1}{R_1+R_2}$ and $\frac{R_2}{R_1+R_2}$ are controllable. 

Superposition: We can combine two different voltages to find the final voltage.

![[chrome_TRMdxwiEoI.png]]
![[chrome_XoR1Zw9LVn.png]]
real-world touchscreens are usually capacitive, not resistive:
- don’t need to be flexible 
- multi-touch is easier 
- more sensitive 
- increased contrast on screen
![[chrome_l8TIZHqGNv.png]]
**Current going through the capacitor**
There is no way current can ever go through a dielectric(i.e. capacitor)

**Now, Capacitors!**
- Charge storage device (like a 'bucket' for charge)
![[chrome_o7jpQRDABw.png]]
NEXT CLASS:
- Physics of a capacitor 













