Once touch occurs, we see that the device **forms capacitor between the plates**
No figure present, before the capacitance
![[WhatsApp Image 2022-10-31 at 12.16.55 PM.jpeg]]
Consider 2-dimensional capacitative touchscreen in Figure 1. Node F (green) represents the contact area of the finger with the top insulator. The finger contact area has horizontal width $w_2$ and depth (into the page) $d_1$. The 'top' metal at node $E_1$ (red) has width $w_1$ and depth $d_1$. The 'bottom' metal at node $E_2$ (grey) has width $w$ and depth $d_2$, where $w$ is much larger than $w_1,w_2$. 

![[WhatsApp Image 2022-10-31 at 12.20.33 PM.jpeg]]

We see that:
$C = \epsilon \frac{A}{d}$ , so we have $C_0 = \epsilon \frac{d_2 w_1}{t_1}$, $C_1 = \epsilon \frac{d_1 w_1}{t_2-t_1}$
$w_2-w_1$.
![[EpicPen_ej8OgKMbCo.png]]
We see that the minimum overlapping rectangle is basically the one with the smaller definitions. 

Different touchpoints are not connected in any way, so for multiple touches on the same screen they form different capacitors. 

**Capacitative Touchscreen vs Resistive touchscreen**
*Benefits of Capacitative Touchscreen*:
- Capacitative touchscreen can detect multitouch
- Capacitive touchscreens are highly responsive, because they do not require any pressure to detecct a touch. (even the slightest touch will activate the sreen )

![[WhatsApp Image 2022-10-31 at 12.34.51 PM.jpeg]]
We see that:
$V_{out}, ideal$ = $\frac{V_{DD} + V_{SS}}{2} + A((U+) - (U-))$ , but basically this is between the range $V_{DD}, V_{SS}$. 
Positive supply rail: $V_{DD}$
Negative supply rail: $V_{SS}$ 

Essentially an **op-amp** is just made of two voltage controlled voltage sources connected in series. 

**Comparator(just a special type of op-amp)**
Motion controlled light sensor:
$V_{DD}$ is the *on* section
$V_{SS}$ is the *off* section.

So basically $V_{DD} > V_{SS}$. A comparator is used in this situation.
Comparator outputs:
$V_{DD}$ if $U+ > U-$
$V_{SS}$ if $U+ < U-$

Comparators have *binary output* (purposefully)
$\rightarrow$ used everywhere (e.g. motion-controlled lights)

Important: No current flows into the input terminals of ideal op-amps
$\rightarrow$ infinite input resistance

**Comparators**
For each of the circuits shown below, plot $V_{out}$ 



