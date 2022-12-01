![[Note14.pdf]]
# Power
2. What does it mean for the power of a particular component to be negative, for the following components? 
	(a) Resistor
	It means current is flowing opposing the direction of the voltage applied, which implies resistor is providing power -> impossible
	(b) Voltage source 
	It means voltage source is generating power, since current is flowing (in the case of voltage source) against the direction of potential difference
	(c) Current source
	It means the current source is generating power, forcing current to flow in a direction opposing the voltage differential
针对所有的电压电流源进行独立分析
全都是线性方程，所以就是可以相加的。所以Vs，Vb， Ia 全都是可以设为零相加的。

Voltage source = short circuit = wire
Current source = open circuit
Voltmeter = open circuit
Ammeter = short circuit = wire

All electronic devices require connections to conduct signals. These connections, or traces, are manufactured through different deposition methods such as physical vapor deposition and chemical vapor deposition. Another less traditional technique is printing. Inks can be made from metallic nanoparticles and deposited using inkjet printing, screen printing, and spray coating. A commonly printed metal ink is silver.

# Note 15
![[Note15.pdf]]
Circuit analysis can be cumbersome to do by hand, and it can be difficult to understand the high-level behavior of complicated circuits given a schematic. We need tools we can use to both lessen the burden of analysis, and help us think about circuits and understand how they behave. Ultimately, our goal is to design interesting circuits, and in this note we will build up additional tools to help us.
# Dependent Sources
At this point, we will introduce a new circuit element: dependent sources. Dependent sources act like the independent sources we’ve studied so far, but instead of a producing a single voltage/current, the voltage/current is controlled by something else in the circuit. There are four different types of dependent sources, shown below.
![[chrome_O7WvOXsbHn.png]]
I.e. Dependent source (provides voltage, current depending on another quantity of voltage/current that is being provided)
In this case, the current in the dependent source is equal a constant (gm) times the voltage vc, which is defined elsewhere in the circuit. Just like an independent current source, this dependent source will produce the same current, regardless of what is connected to it (unless vc changes – then the current will change appropriately). As we’ll see in future notes, dependent sources are useful tools for modeling many advanced circuit elements.

For each independent source k (either voltage source or current source):
- Set all other independent sources to 0 
- Voltage source: replace with a wire 
- Current source: replace with an open circuit 
- Compute the circuit voltages and currents due to this source k
- Compute Vout by summing the Vout,ks for all k

We know that the slope of the line is equal to 1/R . What happens in the limit where R trends towards infinity? Then the line becomes the x-axis, which corresponds to an open circuit as we’ve seen earlier. Now what happens in the limit where R trends towards zero? The line becomes the y-axis, which corresponds to a wire. 

To summarize, **zero voltage source and zero resistance are equivalent to wires (i.e. short circuits); zero current source and infinite resistance are equivalent to open circuits.**

Definition of **equivalence**
Two circuits are **equivalent** if they have the same I −V relationship. (An example of an I −V is that of a resistor, i.e., V = IR or I = V R ). This is exactly what we mean by equivalence; be careful not to overextend this definition or apply others. For example, equivalence tells us nothing about the power in a circuit and one should be careful not to assume it does. 

Now why is this possibly intuitively? 

Since voltage and current are governed by a linear relationship for all of the circuit elements we’ve learned about, and a line can be uniquely determined by exactly two points, we can capture the original circuit with a simplified circuit that has exactly two components: a voltage (or current) source and a resistor.

**Definition 15.1 (equivalent circuit): If we pick two terminals within a circuit, we say that another circuit is equivalent to the original circuit if it exhibits the same I −V relationship at those two terminals.**

**15.8 Summary for Finding Equivalent Resistance**
In general, there are three ways of finding the Thevenin/Norton equivalent resistance of a circuit. However, some of them only work in certain situations, so need to be used with caution. 
1. Zero out all independent sources and apply a Vtest or Itest to calculate the resulting Itest or Vtest respectively. Req = Vtest / Itest . This is the method that we described in detail in the examples above, because this method works for any circuit. When in doubt, this method is the most reliable. 
2. Zero out all independent sources and reduce the entire remaining circuit into a single resistor using the series and parallel resistor formulas that were derived in Sections 15.7.1 and 15.7.2. This method does not work if there are dependent sources. Remember that only independent sources are zeroed out, and there are no resistor formulas for dependent sources. In addition, some resistor configurations cannot be decomposed into combinations of parallel and series resistances. 
3. Calculate Vth and Ino, Req = Vth / Ino . This is an efficient method of finding Req if both the Thevenin and Norton equivalent circuits are being derived. Why does this work? Since the IV relationship is linear, we can calculate the slope (which is the reciprocal of resistance) from any two points. Vth and Ino are the points where the IV curve crosses the V and I axes, respectively (see the left-hand figure below). However, this method does not work if Vth and Ino do not provide two unique points on the IV curve (see the right-hand figure below). Specifically, this method only works if there is at least one independent source in the circuit. When there are no independent sources, Vth = Ino = 0 which does not provide enough information to calculate Req.