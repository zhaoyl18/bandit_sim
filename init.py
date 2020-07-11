import numpy as np


def init_reward(reward, diff=0.05):
    tmp = np.ones((20))
    reward = tmp * (1-diff)
    reward[0] = 1
    return reward

def init_policy(policy, diff=0.05):
    policy = np.ones((20))
    policy[1:] += diff
    return policy
