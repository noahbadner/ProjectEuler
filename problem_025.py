# Noah Badner, 2024
#
# 1000-digit Fibonacci Number
# Problem 25
#
# The Fibonacci sequence is defined by the recurrence relation:
#   F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.
# Hence the first 12 terms will be:
#       F(1)  = 1
#       F(2)  = 1
#       F(3)  = 2
#       F(4)  = 3
#       F(5)  = 5
#       F(6)  = 8
#       F(7)  = 13
#       F(8)  = 21
#       F(9)  = 34
#       F(10) = 55
#       F(11) = 89
#       F(12) = 144
#
# The 12th term, F(12), is the first term to contain three digits.
# What is the index of the first term in the fibonacci sequence to contain 1000 digits?
#
# Completed: 2024-12-18
# Solution: 4782

def fibonacci_index_of_len(n):
    """Returns the index of the first Fibonacci term to contain n number of digits as defined above"""
    a, b = 1, 1
    b_index = 2
    while len(str(b)) < n:
        a, b = b, a+b
        b_index += 1
    return b_index

def main():
    """Main method"""
    solution = fibonacci_index_of_len(1000)
    print(solution)


if __name__ == "__main__":
    main()
