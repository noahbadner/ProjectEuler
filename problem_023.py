# Noah Badner, 2024
#
# Non-Abundant Sums
# Problem 23
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
# sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n s called deficient if ths sum of its proper divisors is less than n, and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
# Completed: 2024-12-12
# Solution: 4179871

def proper_divisors(n):
    """Returns a tuple of all proper divisors of a given number n (all factors not including the number n itself)"""
    divisors = tuple()
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors += (i,)
    return divisors

def is_abundant(n):
    """Returns a boolean value indicating if the given number is an abundant number as described above"""
    return sum(proper_divisors(n)) > n

def abundant_numbers(n):
    """Returns a list of all abundant numbers below the given upper bound n"""
    abundant_list = list()
    for i in range(1, n):
        if is_abundant(i):
            abundant_list.append(i)
    return abundant_list

def sum_of_two(input_list):
    """Returns a list of all numbers that can be found by summing two elements of the given list"""
    ret_set = set()
    for i in range(len(input_list)):
        for j in range(len(input_list)-i):
            ret_set.add(input_list[i]+input_list[i+j])
    return ret_set

def sum_not_in_set(n, input_set):
    """Returns the sum of all numbers below a given upper bound n that are not elements of a given set"""
    ret_sum = 0
    for i in range(n+1):
        if i not in input_set:
            ret_sum += i
            print(f"{i}: {ret_sum}")
    return ret_sum

def main():
    """Main method"""
    solution = sum_not_in_set(28124, sum_of_two(abundant_numbers(28124)))
    print(solution)


if __name__ == "__main__":
    main()
