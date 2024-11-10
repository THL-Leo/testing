import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))

# Example usage
n = 10
print(f"Fibonacci number at position {n} is {fibonacci(n)}")