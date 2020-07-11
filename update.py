import numpy as np

def obj_function(reward, policy):
    J = 0
    pi_theta = np.exp(policy)/np.sum(np.exp(policy))
    obj_func = np.dot(pi_theta,reward)
    return obj_func

def update_grad(reward, policy, eta=0.4):
    pi_theta = np.exp(policy)/np.sum(np.exp(policy))
    K = reward.shape[0]
    grad = np.zeros((K))
    obj_f = obj_function(reward, policy)
    for i in range(K):
        grad[i] = pi_theta[i] * (reward[i]-obj_f)
    policy += eta * grad

