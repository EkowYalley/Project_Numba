# Numba Evaluation Project



## Overview

Numba is a **Just-In-Time (JIT) compiler** that translates Python functions to optimized machine code at runtime. It's particularly designed for scientific computing and numerical analysis.



## Category

- **Type**: Programming tool/compiler

- **Classification**: Performance optimization middleware



## Scientific/Engineering Applications

Numba is extensively used in:

1. High-performance computing (HPC)

2. Numerical simulations (physics, chemistry)

3. Financial modeling and quantitative analysis

4. Machine learning pipelines

5. Engineering simulations (FEA, CFD)



## Key Features

- Accelerates Python code to near-C speeds

- Seamless NumPy array support

- GPU acceleration (via CUDA)

- Low-overhead Python integration

# installation step
- module load Conda/3

- pip install numba

- python -c "import numba; print(numba.__version__)" (to verify instalation)



## Usage Example

```python

from numba import jit

import numpy as np

@jit(nopython=True)

def monte_carlo_pi(nsamples):

    acc = 0

    for _ in range(nsamples):

        x = np.random.random()

        y = np.random.random()

        if (x**2 + y**2) < 1.0:

            acc += 1

    return 4.0 * acc / nsamples

print(monte_carlo_pi(1_000_000))

# How to run code

- cat slurm-52795726.out

(if needed)
- chmod +x run_numba.sb
- sbatch run_numba.sb
- cat <created slurm>

#Refrences 

https://numba.readthedocs.io/en/stable/user/installing.html

https://numba.pydata.org/numba-examples/examples/monte_carlo/index.html
