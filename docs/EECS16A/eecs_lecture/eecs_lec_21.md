Midterm 2: November 15th

![[WhatsApp Image 2022-11-10 at 12.51.30 PM.jpeg]]

- **CLassification:** 
	- Example: how can you tell if a picture is Miki or Ana
- **Estimation**
	- How to estimate model parameters from data
- **Prediction**
	- How to predict stocks value tomorrow based on [past performance]

I know:
- The time, 
- The speed of light
- So effectively I know the potential places I can be. 

24 satellites 
- Known position 
- Time synchronized
- 8 usually visible 

**Problem:** 
- Classify which satellite is transmitting 
- **Estimate distance to GPS** 
- **Estimate position from noisy data** 
Tools: 
- Inner product 
- Cross correlation 
- Least Squares

GPS - integrated circuit


- Satellites transmit a unique code
	- Radio signal
- Signal is received and digitized by a receivver
![[chrome_MSSTuvitfn 1.png]]
![[chrome_NRd1vvERfE.png]]
# Inner Product

![[chrome_XsM52bgxZL.png]]
$\vec{u}, \vec{v}$ can be any vectors, and the **inner product** can be anything in reference/relation to the vectors.

**Example 1: Euclidean inner product (or dot product)**
$\vec{x}, \vec{y} \in R^N, <\vec{x}, \vec{y} > = \vec{x}^T \vec{y}$ 
Test:
Symmetry: 
$<\vec{x}, \vec{y} > = <\vec{y}, \vec{x} > = x^T y = y^T x$
Linearity:
$<a\vec{x},\vec{y}> = (a\vec{x})^T \vec{y} = a\vec{x}^T \vec{y}$
$<\vec{x} + \vec{z},\vec{y}> = (\vec{x} + \vec{z})^T \vec{y} = \vec{x}^T \vec{y} + \vec{z}^T \vec{y}$
![[chrome_7fvaU3m7TW.png]]

# Cauchy - Schwarz Inequality
- Consider : 
- ![[chrome_bZXdujwl6v.png]]


