**Last Class**
Problem: We don't have a **capaci-meter**
We want to measure capacitance between **c** and **g**
![[chrome_82kyS0NiTK.png]]
**Measuring Capaciance Models - Atempt #1**
- Add power sources
![[chrome_E4F1ZOZEtF.png]]
**If there is touch:** $V_c = V_s$ 
**If there is no touch:** $V_c = V_s$
So we have $V_{out}$ does not change! So we **need a better idea**...
Assume $C_{eq}$ starts out discharged
$V_{out} (t=0) = 0$

**Measuring Capacitance Models - Attempt #2 - add switches and a reference capacitor**
![[chrome_ad1eJWeYFd.png]]
If $S_1, S_2$ are both closed?
We want to charge $C_{ref}$ and measure $V_{out}$ as $C_{ref}$ discharges

**Phase 1**
Close $S_1$, open $S_2$
$C_{eq}$ charges
$Q = C_{eq} \cdot V_s$ , (charge accumulates on capacitor plates)

**Phase 2**
Close $S_2$; Open $S_1$
- There is a path for charge to move.
- $C_{eq}$ provides the energy needed for current

Charge will **be shared** between $C_{eq}$ and $C_{ref}$,:: **Charge sharing**

**Measuring Capacitance Models - Attempt #3 - known initial condition**
![[chrome_o76DBALE23.png]]
So if we do this:
**Phase 1**
$S_3+S_1$ closed, $S_2$ open
$V_{out} = 0$
$q = C_{req}V_{out} \rightarrow 0$
$C_{eq} \rightarrow charges$
$q = C_{eq} V_s$
![[WhatsApp Image 2022-10-27 at 1.14.01 PM.jpeg]]
$C_{eq} \cdot V_s = C_{eq} V_{out} + C_{ref} \cdot V_{out}$
![[chrome_hIpTByaGwI.png]]

# Effect of Touch on total Capacitancce
![[chrome_VxcxJ4vJPM.png]]
$C_0 + \frac{C_1 C_2}{C_1+C_2}$
$C_{\Delta} =\frac{C_1 C_2}{C_1+C_2}$
![[chrome_SNLYvmAk2O.png]]
**Comparator:** A device that will **compare** two devices.
We need to choose a voltage that we call: Threshold Voltage ($V_{th}$)
- Above $V_{th}$ $\rightarrow$ 1( touch)
- Below $V_{th}\rightarrow$ 0(touch)

**Battery** = independent voltage source
There are other sources called **dependent voltage source**
![[chrome_DgyRcpXP4e.png]]
We need to compare Voltages to determine if **1** or **0** 
![[chrome_cKB1Myd2lk.png]]
Black box assumption of the cirrcuit. 
Small changes in the transistor output doesn't affect the result of the transistor

# **Operational Amplifier**
An op-amp(**operational amplifier**) is a device that transforms a small voltage difference into a very large voltage difference.
![[chrome_Mod1fI1Swt.png]]
![[chrome_euYIctaRvM.png]]
$U+$ is an input terminal with potential $U+$
$U-$ is an input terminal with potential $U-$
$V_{DD}$ is an independent voltage source that is directly connected to ground.
$V_{SS}$ is an independent voltage source that we will attach to the lead of the operational amplifier.

Voltage differential $V_d$ is equal to $(U+) - (U-)$ 

**Whats inside of black box?**
![[chrome_SUqpBOHtxg.png]]
$A$ from the above is the **gain** of the operational amplifier
So the *operational amplifier* simplifies to the series combination of two *voltage controlled voltage sources*

![[chrome_LUNcFE1LX9.png]]
So the **minute differences** between the differences in capacitance from touch 



