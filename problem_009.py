# Noah Badner, 2024
#
# Special Pythagorean Triplet
# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#   a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a _ b + c = 1000
# Find the product abc.
#
# Completed: 2021-09-04
# Solution: 31875000

def pythagorean_triplet_product(n):
    """Returns the product of all numbers in a pythagorean triplet that together have the given sum n"""
    for a in range(1, n):
        for b in range(1, n-a):
            c = (n - a - b)
            if a**2 + b**2 == c**2:
                return a*b*c

def main():
    """Main method"""
    solution = pythagorean_triplet_product(1000)
    print(solution)


if __name__ == "__main__":
    main()
