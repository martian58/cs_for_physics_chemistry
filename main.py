"""
 * File:         main.py
 * Author:       Fuad Alizada
 * Date:         April 27, 2024
 * Description:  Main file of the project.
"""
import time
import os



from pw1 import TrapezoidalMethod
from pw1 import StochasticMethod
from pw1 import EulerMethod

# Pw 1

TrapezoidalMethod(100000).trapezoidal_example()
StochasticMethod(100000).stochastic_example()   
EulerMethod(100000).euler_example()  

# Pw 2

