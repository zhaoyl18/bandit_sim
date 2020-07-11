import numpy as np
from init import init_reward, init_policy
from update import *
import matplotlib.pyplot as plt
from sim import sim_func

r_list = list()
d_list = list()
pi_list = list()

E = 700

x = np.array(range(E))
for theta in [0, 1, 1.5, 1.8]:
    obj_funcs, pi_optim = sim_func(E, r_gap=0.5, theta_gap=theta)
    d_funcs = 1-obj_funcs
    r_list.append(obj_funcs)
    d_list.append(d_funcs)
    pi_list.append(pi_optim)

plt.figure("delta")
plt.xlabel("epoch")
plt.ylabel("J*-J(k)")
plt.plot(x, d_list[0], color='blue')
plt.plot(x, d_list[1], color='red')
plt.plot(x, d_list[2], color='green')
plt.plot(x, d_list[3], color='yellow')

plt.figure("pi")
plt.xlabel("epoch")
plt.ylabel("pi(a*)")
plt.plot(x, pi_list[0], color='blue')
plt.plot(x, pi_list[1], color='red')
plt.plot(x, pi_list[2], color='green')
plt.plot(x, pi_list[3], color='yellow')


plt.show()