import numpy as np
def gauss1d_nan(y, sigma):
    if sigma <= 0:
        return y
    r = int(3*sigma)+1
    k = np.exp(-0.5*(np.arange(-r, r+1)/sigma)**2); k /= k.sum()
    pad = np.pad(y, r, mode='edge')
    return np.convolve(pad, k, mode='valid')
