![[chrome_h48vFUr3HH.png]]
$I_{in} = I_f = C \frac{dV_C}{dt}$
We see that, by properties of integration:
$\frac{dV_C}{dt} = \frac{I_{in}}{C}$, $V_C = \int \frac{I_{in}(t)}{C} dt =  \int_{t_0}^t \frac{I_{in}(t)}{C}dt + V(t_0)$
Where $V(t_0)$ is the total voltage at iniital time $t_0$.

We see that, therefore:
$V_{out} = 0 - V_C = -\int_{t_0}^t \frac{I_{in}(t)}{C}dt - V(t_0)= - \int_{t_0}^t \frac{V_{in}(t)}{C\times {R_{in}}} - V(t_0)$
$= - \frac{1}{C\times R_{in}} \int_{t_0}^t V_{in}(t) - V(t_0)$

So if we let the capacitor to be set to charged in the beginning, then we must have that:
$V(t_0)=0$
Then, we have:
$V_{out} = - \frac{1}{C\times R_{in}} \int_{t_0}^t V_{in}(t)$ 





