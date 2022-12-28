![[Note24.pdf]]
**Orthogonal Matching Pursuit (OMP)**
We’ll walk through the OMP algorithm using an example with three beacons. At the end of the note we’ll provide a general formulation. 

Consider three beacons (in GPS, these would be satellites) which are each transmitting their own unique periodic code. We’ll denote these codes $s_1, s_2$ and $s_3$. Each of these is length $N = 10$. For concreteness, let’s say that the codes are as follows:

![[chrome_iARa0fhWvK.png]]

Beacon 1 transmits $s_1$ repeatedly, beacon 2 transmits $s_2$ repeatedly, and so on. In addition, the beacons can each multiply their code by a scalar to encode additional information. For example, each beacon could tell the receiver the temperature at its location by multiplying its code by the temperature. (This could be helpful in determining which parts of the walls or doors need more insulation).

![[chrome_feOcjyPWgH.png]]

Basically, what is done is essentially the **circular cross correlation** of a received signal is computed for every single code of the beacon. The largest (absolute) circular cross correlation value for all of the beacons is the desired one. 

Now imagine we have $2,000$ beacons, each with its own code: $s_0,s_1,...,s_{1999}$. Each message is a real number that scales the code: $a_0,a_1,...,a_{1999}$, for each of the $2,000$ sensors. Each of the messages from the transmitters is delayed by a different amount, given by: $\tau_0, \tau_1,\cdots, \tau_{1999}$. Each code is periodic with period $N = 400.$ The signal received ($y \in R^{400}$) is a linear combination of shifted codes from all transmitting users given by: 

$$y = a_0s^{(\tau_0)}_0 +a_1s^{(\tau_1)}_1 +...+a_{1999}s^{(\tau_{1999})}_{1999}$$

Here, the subscript of $s$ indicates which beacon is transmitting, and the superscript in parenthesis represents the how many samples the code is shifted by. We have $400$ measurements ($y \in R^{400}$) and $2000$ unknown values of $a$. How can we possibly determine the messages? We need more information! The additional information is that only a small number (say $10$) beacons are transmitting at the same time. This means that only $10$ of the beacons have non-zero $a_i$ coefficients, but we don’t know which beacons (and we don’t know their shifts). If we put all of the $a_i$’s in a vector, most of the vector would contain $0$’s. We call this a **sparse vector** and the **sparsity level** $k$ is the number of non-zero elements.

### Connecting to Machine Learning
In this note, we showed you how by thinking systematically using the design philosophies taught in 16A, you could have systematically have come up with the algorithm that is commonly known as orthogonal matching pursuit or OMP. While this specific algorithm is certainly practically important in its own right as a building block, it is also a prime representative of a family of closely related algorithms that are very important in machine learning — namely what are called “boosting” algorithms (in case you want to read further on your own — there’s no rush, these are topics that are usually covered if/when you take 189). 

For those who want to know more, specifically “gradient boosting” algorithms can be understood as nothing more than a version of these ideas to be used when the relevant distance is not Euclidean squared distance, but something else. But all the main ideas are already present in this note about OMP. The most famous example of a gradient boosting algorithm is called AdaBoost, which is sometimes referred to as“the best out-of-the-box classificatio” algorithm for practical machine learning. In fact, modern machine learning is largely based on working through ideas whose seeds are taught to you across 16A and 16B. 

To be more specific, you saw how from the hypothetical real world goal of being able to extract signals from many potential beacons, which might be at differing levels of signal strength, you could still find them by iteratively reducing interference one at a time. 

The first approach you could think of was to simply ignore the interference and just search for the beacons one at a time. You saw that the problem was that a strong beacon signal could completely mask your ability to see a weaker signal. 

To deal with this, you naturally thought of trying to find the signals in decreasing order of signal strength. First, you find the strongest one. Then, you remove its estimated effect from what you observed. And then, you tried to find the signal which was presumably the next strongest. And then remove its effect, and so on. This pattern is what is called “matching pursuit” in the literature. (Because it can be understood as trying to greedily reach a destination by picking the available direction that would bring you as close as possible, actually moving along that direction, and then repeating from your new vantage point.) 

You saw that while this worked better, it didn’t revisit its estimate of the first found signal in light of the second signal that was found, and so on. This made errors in the residual signal potentially compound as you found more and more signals, making it harder to find weaker signals as you went on. So, you made one final version that took advantage of what you knew about projection to keep improving estimates as we found more signals — allowing us to better clean up the residual. This is what gave us orthogonal matching pursuit OMP. 

While doing all this, you also noticed something else. OMP allows us to potentially break what seemed like a fundamental barrier at the beginning of 16A — namely that we need to have n equations/measurements if we want to solve for n unknowns. OMP tells us that in fact, we often can find n unknowns with fewer than n equations, if we somehow happened to know that most of the n potential unknowns were going to come out to be zero. This is the powerful idea of sparsity. This will be explored further in parts of 16B and beyond, but is actually something that is believed to be at the heart of what is sometimes considered the “unreasonable effectiveness” of machine learning algorithms in the real world.