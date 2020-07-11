import numpy as np
from init import init_reward, init_policy
from update import *
import matplotlib.pyplot as plt
from sim import sim_func

r_list = list()
d_list = list()
pi_list = list()
E = 500

def sim_func2(E=E):
    reward = np.array([1, 0.9, 0])
    policy = np.array([0, 1.3863, 1.6094]) # [0.1, 0.4, 0.5]

    #begin optimization
    obj_funcs = np.ones((E))
    pi_optim = np.ones((E))
    pi_2 = np.ones((E))
    pi_3 = np.ones((E))

    for epoch in range(E):
        pi_theta = np.exp(policy)/np.sum(np.exp(policy))
        optimal_prob = pi_theta[0]
        print("epoch: ", epoch)
        print("obj func: ", obj_function(reward,policy))
        print("optimal prob: ", optimal_prob)
        obj_funcs[epoch] = obj_function(reward,policy)
        pi_optim[epoch] = optimal_prob
        pi_2[epoch] = pi_theta[1]
        pi_3[epoch] = pi_theta[2]

        update_grad(reward, policy, eta=0.4)

    return (obj_funcs, pi_optim, pi_2, pi_3)

x = np.array(range(E))

obj_funcs, pi_optim, pi_2, pi_3 = sim_func2(E)
d_funcs = 1-obj_funcs

plt.figure("delta")
plt.xlabel("epoch")
plt.ylabel("J*-J(k)")
plt.plot(x, obj_funcs, color='blue')

plt.figure("pi")
plt.xlabel("epoch")
plt.ylabel("pi(a*)")
plt.plot(x, pi_optim, color='blue')
plt.plot(x, pi_2, color='red')
plt.plot(x, pi_3, color='black')

plt.show()