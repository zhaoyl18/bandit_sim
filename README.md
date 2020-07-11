# simulation on bandit case

When
$$\frac{d J}{d\theta_{a^*}}>\frac{d J}{d\theta_{a} }, \forall a$$
Then $\pi_{\theta_k}(a^*)$ is monotonically increasing

$\delta(k) = J^*-J(k)$ converges at rate of $1/k$

But before this condition is reached, increasing speed of $J(\theta)$ is rather slow, as shown in result/ folder.

#### Conjecture

When initialization is not good, optimization process seems to be a 2-phase-process, where the iterations needed at $1^{st}$ phase is to be tested.

## Setting

1. K=20 actions in total
2. Optimal action is the first one, reward is 1, other 19 actions' reward is 1-0.05
3. $\theta$ is the policy parameter to be optimized
4. Condition is worse = needs more iterations to make $\pi_\theta(a^*)$ the largest prob
5. In this setting, other 19 actions are exactly the same. So thresh of condition is $\pi_\theta(a^*)=0.05$.

## Result

In result/ folder, 4 initializations are tested.

!!! Notice, under this setting, always exists: $\frac{d J}{d\theta_{a^*}}>\frac{d J}{d\theta_{a^\prime} }$

!!! When relative rewards are more complicated, this may not hold.

blue -> red -> green -> yellow, initializaiton becomes worse($\pi_{\theta_1}(a^*)$ is smaller).

reward.png is $J(\theta)$.\
delta.png is $1 - J(\theta)$.\
pi.png is $\pi_{\theta}(a^*)$

N = Iterations of $1^{st}$ phase.

|num|blue | red | green | yellow|
|  ----  | ----  | ----| ----  | ----  |  
|$\pi_{\theta_1}(a^*)$ | 0.05 | 0.019 | 0.0116 | 0.0086|
|N | 0 | 154 | 316 | 445  
