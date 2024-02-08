import numpy as np
from functools import wraps
import time

#FAAAAALA DERICK
def memoize(func):
    memo = {}

    @wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper

#HAHAHAHHAHAH
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def matrix_multiplication(a, b):
    return np.dot(a, b)

#Me vê uma coca 2l
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result


@Timer
def long_running_function():
    time.sleep(5)

#HAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAAHAHAHAHA
if __name__ == "__main__":
    print(f"Fibonacci of 10: {fibonacci(10)}")

    matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    result_matrix = matrix_multiplication(matrix_a, matrix_b)
    print("Matrix A:")
    print(matrix_a)
    print("Matrix B:")
    print(matrix_b)
    print("Result Matrix:")
    print(result_matrix)

    long_running_function()
