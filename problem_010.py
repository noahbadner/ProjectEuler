# Noah Badner, 2024
#
# Summation of Primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all primes below two million.
#
# Completed: 2021-09-04
# Solution: 142913828922

def primes(n):
    """
    Returns a tuple containing all prime numbers below the given upper bound n sorted from smallest to largest
    Implementation: check each number for prime factors, and add to a list of primes if there are none
    Optimizations: only check odd numbers, only check for prime factors less than the square root of the candidate
    Same implementation as used in the solution to problem 3
    """
    primes_list = (2,)
    for i in range(3, int(n), 2):  # Prime numbers greater than two must be odd numbers
        for prime_factor in primes_list:
            if i % prime_factor == 0:  # Prime numbers cannot have prime factors
                break
            elif prime_factor**2 > i:  # A number's largest prime factor must be smaller than its square root
                primes_list += (i,)
                break
    return primes_list

def main():
    """Main method"""
    solution = sum(primes(2000000))
    print(solution)


if __name__ == "__main__":
    main()
