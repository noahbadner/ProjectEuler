# Noah Badner, 2024
#
# 10001st Prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
#
# Completed: 2021-09-04
# Solution: 104743

def primes(n):
    """
    Returns a tuple containing all prime numbers below the given upper bound n sorted from smallest to largest
    Implementation: check each number for prime factors, and add to a list of primes if there are none
    Optimizations: only check odd numbers, only check for prime factors less than the square root of the candidate
    Similar to the implementation in the solution to problem 3
    """
    primes_list = (2,)
    candidate = 3
    while len(primes_list) < n:  # Prime numbers greater than two must be odd numbers
        for prime_factor in primes_list:
            if candidate % prime_factor == 0:  # Prime numbers cannot have prime factors
                break
            elif prime_factor ** 2 > candidate:  # A number's largest prime factor must be smaller than its square root
                primes_list += (candidate,)
                break
        candidate += 1
    return primes_list

def main():
    """Main method"""
    solution = primes(10001)[-1]
    print(solution)


if __name__ == "__main__":
    main()
