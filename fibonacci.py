#!/bin/python3
""" Fibonacci number generation

The program takes an input N from the command line
It uses a non-recursive technique to generate the value of N
Checks for conditions mentioned in the coding challenge.
"""
import math
import sys


def is_prime(n):
    """ Checks if F(n) is prime. Returns True if F(n) is prime
    It checks for all odd values of N in (3, sqrt(n))
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True


def fibonacci(n):
    """ 
    Generates N Fibonnaci numbers
    """
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

        if (c % 3 == 0) and (c % 5 == 0):
            print("FizzBuzz")
        elif c % 3 == 0:
            print("Buzz")
        elif c % 5 == 0:
            print("Fizz")
        elif is_prime(c):
            print("BuzzFizz")
        else:
            print(c)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Program expects the value of N")
        sys.exit(-1)
    try:
        n = int(sys.argv[1])
    except (ValueError, TypeError):
        print("Invalid input")
        sys.exit(-1)

    fibonacci(abs(n))
