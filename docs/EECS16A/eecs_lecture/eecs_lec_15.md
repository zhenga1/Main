#r/lecture
- Lecture notes: link

# Lecture: 10/20
```jupyter
print("Hello world i am cool")
```

**Capacitance**
- Charge storage device (like a 'bucket' for charge)
- 2 Conductive plates -> has distance `d` from each other
![[chrome_XTpxl4ahtc.png]]
So basically we have the dielectric(which is an insulator) with width `d` between the two capacitors. 

Capacitance follows the below equation:
$C = \epsilon \frac{A}{d}$, we see that 
$\epsilon=$ permittivity
$\epsilon_0=8.85\cdot 10^{-12} F/m$ vacuum permitivity. Using dimensional analysis
$[F] = [\frac{F}{m}]\cdot \frac{m^2}{m}$

![[WhatsApp Image 2022-10-20 at 12.55.09 PM.jpeg]]
The dielectric constant depends on the material of the substance. 
$I = C\frac{dV}{dt}$
Making the dielectric very thin increases the capacitance of that device.

**In the real world, how do we make Capacitors?**
**The physics of a Capacitor**
Silicon-based capacitors are more common.
Since it is a semiconductor
- Energy is needed to move charge
	- No current across the capacitor plates
	- Voltage source provides energy needed for the flow of charges (e-)
![[chrome_No9M6eYFTr.png]]
- No current

**The physics of a capacitor**
$t_0$ is the time initial(when the bottom plate is open circuit, as seen above)
$t_1$ is the time after connection of the plates
![[chrome_oNS3keOH9E.png]]
So basically after the switch is closed, at $t_1$, we see that the top plate has more holes(i.e. positive charge), whilst the bottom plate has more electrons(i.e. negative charge). 

**When do we stop (current)?**
When the voltage across the capacitor is equal to the voltage provided by the voltage source.
![[chrome_saqoh8SzWt.png]]
So the current stops when the voltage difference is equal to voltage source. 
Electric field = Force/charge = Voltage/distance
How do you short a capacitor. 

Voltage in capacitor is equalized with the voltage of the power source
It will turn off after the zero 

One capacitor charged to $20V$, the other charged to $0V$ 
The charge moved so fast between the capacitors that basically the metal were fused together. 

**Circuit model: IV relationship**
![[chrome_saqoh8SzWt 1.png]]
**Circuit Model: IV relationship**
$Q_{elem} = C\cdot V_{elem}$ 
$[C] = [F][V]$ , so basically Coulomb = Farad $\times$ Voltage
We know:
	$I_{elem} = \frac{dQ}{dt}$, $I_{elem} = \frac{d}{dt} C\cdot V_{elem}$ , 
	assuming that $C$ is constant over time. 
$I_{elem} = C\cdot \frac{dV_{elem}}{dt}$ 
So therefore the IV relationship is as above.

**==Question: How would the IV curve look like?==**
Ex1:
Simple circuit 1:
![[EpicPen_Qk5X69eA2F.png]]
**KCL:** $I_s = I_c$
Elem Def: -> $I_c = C\cdot \frac{dV_c}{dt}$
So therefore:
$I_s = C\frac{dV_c}{dt}$
$\int^t_0 I_s dt = \int^{v_1(t)}_{v_1(0)} CdV_1$,    so    $I_st = C(v_1(t)-v_1(0))$
Solving, we get $v_1(t) = \frac{I_s}{C}\cdot t + v_1(0)$

**Attempt to draw curve to represent relation:**
![[EpicPen_YFIECoQv10.png]]
**What happenes when we have a voltage source over a capacitor?**
![[EpicPen_5UitxWgkzd.png]]
So when $V_s$ doesn't change, the current becomes zero.

**Thevenin and Norton**
- Only useful for situations in which the IV relationship is linear. 



