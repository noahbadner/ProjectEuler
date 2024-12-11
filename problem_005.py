# Noah Badner, 2024
#
# Smallest Multiple
# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Completed: 2023-09-03
# Solution: 232792560
#
# TODO: optimize runtime leveraging prime factors?

def smallest_multiple(n):
    """Returns the smallest number that is divisible by each natural number at or below n"""
    factors = [i for i in range(1, n + 1)]
    while True:
        could_be_smallest_multiple = True
        for j in factors:
            if n % j != 0:
                could_be_smallest_multiple = False
                break
        if could_be_smallest_multiple:
            break
        n += 1
        # if n % 10000000 == 0:
        #     print(n)
    return n

def main():
    """Main method"""
    solution = smallest_multiple(20)
    print(solution)


if __name__ == "__main__":
    main()
