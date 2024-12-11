# Noah Badner, 2024
#
# Factorial Digit Sum
# Problem 20
#
# n! means n x (n - 1) x ... x 3 x 2 x 1.
#
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#
# Completed: 2021-09-12
# Solution: 648

def factorial(n):
    """Returns the value of n! if n >= 0"""
    if n < 0:
        raise Exception(f"n! for n < 0: n = {n}")
    factorial_product = 1
    for i in range(1, n+1):
        factorial_product *= i
    return factorial_product

def sum_of_digits(n):
    """Returns the sum of each individual digit in a given integer n"""
    return sum(int(c) for c in str(n))

def main():
    """Main method"""
    solution = sum_of_digits(factorial(100))
    print(solution)


if __name__ == "__main__":
    main()
