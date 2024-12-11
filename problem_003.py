# Noah Badner, 2024
#
# Largest Prime Factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# Completed: 2021-09-04
# Solution: 6857


def primes(n):
    """
    Returns a tuple containing all prime numbers below the given upper bound n sorted from smallest to largest
    Implementation: check each number for prime factors, and add to a list of primes if there are none
    Optimizations: only check odd numbers, only check for prime factors less than the square root of the candidate
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

def largest_factor(n, potential_factors):
    """Returns the largest factor of n given a list of potential factors"""
    for factor in potential_factors[::-1]:
        if n % factor == 0:
            return factor

def main():
    """Main method"""
    n = 600851475143
    sqrt_n = n**0.5
    primes_list = primes(sqrt_n)

    solution = largest_factor(n, primes_list)
    print(solution)


if __name__ == "__main__":
    main()
