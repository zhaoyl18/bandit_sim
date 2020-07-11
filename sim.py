import numpy as np
from init import init_reward, init_policy
from update import *
import matplotlib.pyplot as plt

def sim_func(E=500, r_gap=0.5, theta_gap=0.00):
    reward = np.zeros((20))
    policy = np.zeros((20))

    reward = init_reward(reward, r_gap)
    policy = init_policy(policy, theta_gap)

    #begin optimization
    obj_funcs = np.ones((E))
    pi_optim = np.ones((E))

    for epoch in range(E):
        pi_theta = np.exp(policy)/np.sum(np.exp(policy))
        optimal_prob = pi_theta[0]
        print("epoch: ", epoch)
        print("obj func: ", obj_function(reward,policy))
        print("optimal prob: ", optimal_prob)
        obj_funcs[epoch] = obj_function(reward,policy)
        pi_optim[epoch] = optimal_prob
        update_grad(reward, policy, eta=0.4)

    return (obj_funcs, pi_optim)