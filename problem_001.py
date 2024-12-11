# Noah Badner, 2024
#
# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these
# multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Completed: 2021-09-03
# Solution: 233168

def is_multiple(i, factors):
    """Returns a boolean value indicating if the given variable i is a multiple of the given factors"""
    for factor in factors:
        if i % factor == 0:
            return True
    return False

def multiples_sum(n, factors):
    """Returns the sum of all multiples of the given factors below the upper bound n"""
    sum_of_multiples = 0
    for i in range(n):
        sum_of_multiples += i if is_multiple(i, factors) else 0
    return sum_of_multiples

def main():
    """Main method"""
    solution = multiples_sum(1000, [3,5])
    print(solution)


if __name__ == "__main__":
    main()
