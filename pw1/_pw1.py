import math
import time
import random
import numpy as np


class TrapezoidalMethod:

    def __init__(self, N: int) -> None:
        self.N = N

    def trapezoidal_pi(self, N: int) -> float:
        a = -1.0
        b = 1.0
        delta_x = (b - a) / N
        total = 0.0

        for i in range(1, N):
            x = a + i * delta_x
            total += math.sqrt(1 - x**2)

        area = (delta_x / 2) * (math.sqrt(1 - a**2) + 2 * total + math.sqrt(1 - b**2))
        pi_estimate = 2 * area 
        return pi_estimate

    def trapezoidal_example(self) -> None:
        N_values = [10, 100, 1000, 10000, 100000, 1000000]
        print("\nTrapezoidal Method:\n")
        print(f"{'N':>10} | {'Estimated π':>15} | {'Relative Error':>15} | {'Time (s)':>10}")
        print("-" * 60)
        for N in N_values:
            start_time = time.time()
            pi_val = self.trapezoidal_pi(N)
            end_time = time.time()
            relative_error = abs(math.pi - pi_val) / math.pi
            computation_time = end_time - start_time
            print(f"{N:>10} | {pi_val:>15.10f} | {relative_error:15.5e} | {computation_time:10.6f}")
        
        print("-" * 60)



class StochasticMethod:

    def __init__(self, N: int) -> None:
        self.N = N


    def stochastic_pi(self, N: int) -> float:
        inside_circle = 0
        for _ in range(N):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                inside_circle += 1
        pi_estimate = 4 * inside_circle / N
        return pi_estimate

    def stochastic_example(self):
        N_values = [10, 100, 1000, 10000, 100000, 1000000]
        print("\nStochastic Method:\n")

        print(f"{'N':>10} | {'Estimated π':>15} | {'Relative Error':>15} | {'Time (s)':>10}")
        print("-" * 60)
        for N in N_values:
            start_time = time.time()
            pi_val = self.stochastic_pi(N)
            end_time = time.time()
            relative_error = abs(math.pi - pi_val) / math.pi
            computation_time = end_time - start_time
            print(f"{N:>10} | {pi_val:>15.10f} | {relative_error:>15.5e} | {computation_time:>10.6f}")
        print("-" * 60)

        


class EulerMethod:

    def __init__(self, N: int) -> None:
        self.N = N

    def calc_pi_by_euler_numpy(self, N):
        """
        Calculate pi using Euler's method by summing the reciprocal of squares.

        Parameters:
        N (int): Number of terms in the series.

        Returns:
        float: Estimated value of pi.
        """
        i = np.arange(1, N + 1)
        num = np.sum(1 / (i ** 2))
        pi_estimate = math.sqrt(6 * num)
        return pi_estimate

    def euler_example(self):
        N_values = [10, 100, 1000, 10000, 100000, 1000000]
        print("\nEuler Method:\n")

        print(f"{'N':>10} | {'Estimated π':>15} | {'Relative Error':>15} | {'Time (s)':>10}")
        print("-" * 60)

        for N in N_values:
            start_time = time.time()
            pi_est = self.calc_pi_by_euler_numpy(N)
            end_time = time.time()

            relative_error = abs(math.pi - pi_est) / math.pi

            computation_time = end_time - start_time

            print(f"{N:>10} | {pi_est:>15.10f} | {relative_error:>15.5e} | {computation_time:>10.6f}")
        print("-" * 60)

