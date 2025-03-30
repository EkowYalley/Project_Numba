from numba import jit

import numpy as np



@jit(nopython=True)  # Enable JIT compilation

def monte_carlo_pi(n_samples):

    acc = 0

    for _ in range(n_samples):

        x, y = np.random.random(), np.random.random()

        if x**2 + y**2 < 1.0:

            acc += 1

    return 4.0 * acc / n_samples



print(monte_carlo_pi(1_000_000))
