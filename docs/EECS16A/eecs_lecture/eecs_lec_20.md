![[WhatsApp Image 2022-11-08 at 12.46.27 PM.jpeg]]

# Design Procedure
**Step 1 (Specification):** Concretely restate the goals for the design. 
Frequently, a design prompt will inclddue a lot of text, so we'd like to restate all fo the most important features of our design. We'll refer to these specifications later to determine if our design is complete. 

**Step 2 (Strategy)** *Describe your strategy* (often in the form of block diagram) to achieve your goal. To do this, start by thinking about what you can measure s what you want to know

**Step 3 (Implementation)** *Implement the components described in your strategy.* This is where pattern matching is useful: remind yourself of blocks you know, (ex. voltage divider, inverting amplifier) and check if any of these can be used to implement steps of your strategy.

**Step 4 (Verification):** *Check that your design from Step 3 does what you specified in Step 1.* Check block-to-block connections, as these are the most common point for problems. Does one block load another block causing it to behave differently than expected? Are there any contradictions (ex. a voltage source with both ends connected by a wire, or a current source directed into an open circuit)?

# Cascading Blocks


# Unit Gain Buffer
Allows us to isolate circuits/blocks
![[chrome_iAYimPap4l.png]]


**Example 1**
We want this:
$V_{in} \rightarrow \frac{R_2}{R_1+R_2} \rightarrow Av = 10 \rightarrow V_{out}$ 

![[chrome_kmRdzsS29z.png]]
![[chrome_78AFfy7IkI.png]]
**Example 3**
We see that A in the above expression is basically the expression:
$$V_{out}$$

  
A **voltage follower** (also called a unity-gain amplifier, a buffer amplifier, and an isolation amplifier) is a op-amp circuit which has a voltage gain of 1.


**Floating node** capacitors always conserve capacitor charge 

A common use of an op-amp is to **convert a current signal into a voltage signal**. This configuration is called a **transresistance amplifier**, as shown in Figure 2. (Note: In the real world, we call this a transimpedance amplifier. Impedance is just a fancy word to describe resistance as a function of frequency.) Assume that VSS = −VDD for all the parts of this problem.

An ideal current source is a device which supplies constant current to any load resistor that is connected across it. An ideal current source has infinite parallel resistance connected across its terminals. Thus, the output current is independent of voltage of the source terminals as well as the value of the resistor it is providing current to. A realistic current source is a device that has some internal resistance connected across its terminals. Unlike the ideal version, the current of a real-world current source depends on the voltage of the source. The more this voltage, the smaller the current will be

The first rule holds since we assume that the input resistance for an op-amp is infinite. The second rule holds because in feedback, the input and output voltage have to be the same.