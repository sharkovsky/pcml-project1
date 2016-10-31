# Useful starting lines
import numpy as np
from functools import partial
import math

from proj1_helpers import *
from helpers import *

############ general functions ####################

# general gradient descent
def gradient_descent(y, tx, initial_x, gamma, max_iters,
                     compute_gradient, compute_loss):
    losses = []
    w = initial_w
    
    for n_iter in range(max_iters):
        gradient = compute_gradient(y, tx, w)
        loss = compute_loss(y, tx, w)
        w = w - gamma * gradient
        # print(loss)
        
        losses.append(loss)
    
    return w, losses[-1]

def stochastic_gradient_descent(y, tx, initial_w, batch_size, gamma, max_iters, seed,
                                compute_gradient, compute_loss):
    losses = []
    w = initial_w
    
    num_batches = math.floor(y.shape[0] / batch_size) 
    batches = batch_iter(y, tx, seed, batch_size, num_batches)

    for n_iter in range(max_iters):
        batch_y, batch_tx = next(batches)
        gradient = compute_gradient(batch_y, batch_tx, w)
        loss = compute_loss(y, tx, w)
        #print(loss)
        w = w - gamma * gradient
        
        losses.append(loss)
        
    return w, losses[-1]


###########  Linear regression using gradient descent ##################


# TODO: perhaps import it instead of copy?
def calculate_mse(e):
    """Calculate the mse for vector e."""
    return 1/2*np.mean(e**2)

def calculate_mae(e):
    """Calculate the mae for vector e."""
    return np.mean(np.abs(e))

def compute_loss_mse(y, tx, w):
    """Calculate the loss using mse """
    e = y - tx.dot(w)
    return calculate_mse(e)

def compute_gradient_mse(y, tx, w):
    """ compute the gradient associated to the MSE cost function"""
    e = y - (tx @ w)
    return -1/y.shape[0] * (tx.T @ e)

def least_squares_GD(y, tx, initial_w, gamma, max_iters):
    return gradient_descent(y, tx, initial_w, gamma, max_iters,
                            compute_gradient_mse, compute_loss_mse)

###########  Linear regression using stochastic gradient descent ##### 

def least_squares_SGD(y, tx, initial_w, gamma, max_iters):
    batch_size = y.shape[0]//2
    seed = 3
    
    return stochastic_gradient_descent(y, tx, initial_w, batch_size, gamma, max_iters,
                                       seed, compute_gradient_mse, compute_loss_mse)

######### Least squares regression using normal equations #####

def least_squares(y, tx):
    w = (np.linalg.inv(tx.T @ tx) @ tx.T @ y)
    loss = compute_loss_mse(y, tx, w)
    return w, loss

######## Ridge regression using normal equations ########

def ridge_regression(y, tx, lambda_):
    w = np.linalg.inv(tx.T @ tx + lambda_ * np.identity(tx.shape[1])) @ tx.T @ y
    loss = compute_loss_mse(y, tx, w)
    return w, loss

###### Logistic regression using gradient descent #######

def sigmoid(t):
    """apply sigmoid function on t."""
    return 1 / (1 + np.exp(-t))

def compute_loss_log(y, tx, w):
    """compute cost by negative log likelihood."""
    xw = tx @ w
    return np.sum(np.log(1 + np.exp(xw)) - y * xw)

def compute_gradient_log(y, tx, w):
    """compute the gradient of loss."""
    xw = tx @ w
    return tx.T @ (np.apply_along_axis(sigmoid, 0, xw) - y)

## using gradient descent
def logistic_regression(y, tx, initial_w, gamma, max_iters):
    return gradient_descent(y, tx, initial_w, gamma, max_iters,
                            compute_gradient_log, compute_loss_log)

###### Regularized  logistic  regression  using  gradient  descent or SGD ###

def compute_loss_rlog(y, tx, w, lambda_):
    return compute_loss_log(y, tx, w) + lambda_ * w.T @ w

def compute_gradient_rlog(y, tx, w, lambda_):
    return compute_gradient_log(y, tx, w) + 2 * lambda_ * w

def reg_logistic_regression(y, tx, lambda_, initial_w, gamma, max_iters):
    compute_gradient = partial(compute_gradient)
    compute_loss = partial(compute_loss_logistic, lambda_ = lambda_)
    return gradient_descent(y, tx, initial_w, gamma, max_iters,
                            compute_gradient, compute_loss)
