#r/lecture
- Lecture notes: link

# Lecture: 1117/
```jupyter
print("Hello world i am cool")
```
# Probability of coughs 
1 cough every 6 seconds (on average)

Last time: 
• Talked about GPS 
- Known position of satellites 
- Each satellite has its own signature 
- Talked about inner product 
- Measure of similarity between vectors 
- When zero — orthogonal vectors 
- Talked about using inner products for classification 

Today: 
- Computing delay with cross-correlation 
- Finding position with multi-lateration

- Do mt2 redo
-> Then you can get 100% clobber

Vectors can be thought of as **signals**
We can define **literally anything** as a signal, such as a vector representing the faces of Ana and Miki.

Moving example is **GPS**, try to find the distances with the saelites.

- 24 satelites
	- Known position
	- Time synchronised
	- 8 usually visible
- Problem:
	- Classify which satelite is transmitting
	- Estimate distance to GPS
	- Estimate position from noisy data
- Tools:
	- Inner product 
	- Cross correlation 
	- Least Squares
# Localization
- Satelites transmit a unique code
	- Radio signal
- Signal is received and digitized by a receiver

**Two Problems:**
1. Interference
2. Timing
# Classification
$$||\vec{r} - \vec{s_i}|| = ||\vec{r}||^2 + ||\vec{s_i}||^2 - 2<\vec{r},\vec{s_i}>$$
If $<\vec{r},\vec{s_i}>$ is **maximized**, then $||\vec{r}-\vec{s_i}||^2$ is **minimised**. 

![[chrome_Vf12ySY8SC.png]]
TX: Transmit
- $\vec{n}$ is the noise.
![[chrome_NEo83nB7wN.png]]
$$<\vec{r}, \vec{s_1}> = <\vec{s_1} + \vec{s_2} + \vec{n}, \vec{s_1}>$$
$$=<\vec{s_1},\vec{s_1}>+ <\vec{s_2},\vec{s_1}> + <\vec{n},\vec{s_1}>$$
We want $<\vec{n},\vec{s_1}>$ to be small, and what is desired is the vector:
$$<\vec{s_1},\vec{s_1}>+ <\vec{s_2},\vec{s_1}> $$
							Desired       Interference
We want $<s_2,s_1>$ to be very small, since that is the interfference term. 
Making $<\vec{s_2},\vec{s_1}>=0$ makes it small. 

# Example
$\vec{r_1} = [2.01,-0.03]^T , \vec{r_2} = [1.01,-1.03]$
![[WhatsApp Image 2022-11-17 at 1.15.27 PM.jpeg]]
![[chrome_Ly0EosnXeS.png]]
So, we have that, instead of having the vector $\vec{r}$ being a vector in $R^2$ or $R^3$ or $R^4$, the vector $\vec{r}$ is $R^{1024}$

$$<\vec{r}, \vec{s_i}> = \vec{r}^T \vec{s_i}$$
![[chrome_O3PxPSAbel.png]]
![[chrome_OBLI1SALJR.png]]
# Timing...
- Satellites transmit a **(modulated)** unique code
	- Radio signal
- Signal is received **(demodulated)** and digitized by a receiver.

With a receiver;
- When you slow it down and then play the signal magnitudes using a speaker, what you get is mostly noise. 

![[chrome_Iz1K5AwY6k.png]]
# Cross- Correlation 
**Pattern Matching of signals**
![[chrome_hpovolDsIv.png]]
Problem: vectors (signals) are not the same length:
$\vec{r} \in R^9, \vec{s} \in R^5$
Solution: Define infinite signals $r[n],s[n]$ by zero-padding.
$\vec{r} = [r_0, r_1, r_2,r_3,\dots r_8]^T$ 
$\vec{s} = [s_0, s_1, s_2,s_3, s_4]^T$ 
![[chrome_1yMCL0a7cY.png]]
$$<r[n], s[n]> = \Sigma_{n=0}^\infty r[n]\cdot s[n] = \Sigma_{n=0}^7 r[n]\cdot s[n]$$
![[chrome_W70x5sQK0v.png]]
Q: How to match with shifted version?
A: compute: $<r[n],s[n-1]> = \Sigma_{n=-\infty}^\infty r[n]\cdot s[n-1]$

$corr_{\vec{r}}(\vec{s})[k] = <r[n],s[n-k]> = \Sigma_{n=-\infty}^{\infty} r[n]\cdot s[n-k]$
$k* = argmax corr_{\vec{r}}(\vec{s})[k]$ 

We see that:
- If $\vec{x} \in R^N$ and $\vec{y} \in R^M$, then the length of $corr_{\vec{x}} (\vec{y})$ is $N+M-1$ 
- $corr_\vec{x} (\vec{y}) \neq corr_\vec{y} (\vec{x})$
- $corr_\vec{x} (\vec{x})$ is the auto-correlation

# Periodic Signals
• Satellites repeat the codes over and over 
	- Cross correlation is “periodically expanded” instead of zero-padded 
	- Result is periodic
**Received Signal**

Corerlate with $s_1[n]$
$corr_{\vec{s_1}}[k] = <r[n],s_1[n-k]>$ 
$= <s_1[n-\tau_1],s_1[n-k]>$ 
$+ <s_2[n-\tau_2],s_1[n-k]> + w[n]$

GPS you can not only solve for distance, you can also solve for time. 

# Convolution





