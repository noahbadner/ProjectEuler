# Noah Badner, 2024
#
# Power Digit Sum
# Problem 16
#
# 2^15 = 32768 adn the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#
# Completed 2021-09-10
# Solution: 1366

def sum_of_digits(n):
    """Returns the sum of each individual digit in a given integer n"""
    return sum(int(c) for c in str(n))

def main():
    """Main method"""
    solution = sum_of_digits(2**1000)
    print(solution)


if __name__ == "__main__":
    main()
