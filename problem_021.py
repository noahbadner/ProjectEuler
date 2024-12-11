# Noah Badner, 2024
#
# Amicable Numbers
# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
# proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# Completed: 2021-09-12
# Solution: 31626

def divisor_sum(n):
    """Returns the sum of the proper divisors of a given number n (excludes n)"""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        sum_of_divisors = 1
        sqrt_n = n**0.5
        for i in range(2, int(sqrt_n)+1):
            if n % i == 0:
                sum_of_divisors += i + (n / i)
        sum_of_divisors += sqrt_n if sqrt_n.is_integer() else 0
    return sum_of_divisors

def is_amicable(n):
    """Returns a boolean value indicating whether the given number n is an amicable number as defined above"""
    div_sum_n = divisor_sum(n)
    return n == divisor_sum(div_sum_n) and n != div_sum_n

def sum_amicable_numbers_below(n):
    """Returns the sum of all amicable numbers below a given upper bound n"""
    amicable_sum = 0
    for i in range(n):
        amicable_sum += i if is_amicable(i) else 0
    return amicable_sum

def main():
    """Main method"""
    solution = sum_amicable_numbers_below(10000)
    print(solution)


if __name__ == "__main__":
    main()
