# Noah Badner, 2024
#
# Largest Palindrome Product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
#   9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Completed: 2021-09-03
# Solution: 906609

def is_palindromic_number(n):
    """Returns a boolean indicating if a given integer is a palindromic number (e.g. 9009, 12321)"""
    int_string = str(n)
    for i in range(len(int_string)//2):
        if int_string[i] != int_string[-i-1]:  # If a left character does not equal the corresponding right character
            return False
    return True

def largest_product_palindrome(n):
    """Returns the largest palindrome given an upper bound n and lower bound m for its factors"""
    largest_palindrome = 0
    for i in range(1, n):
        for j in range(1, n):
            product = i * j
            if product > largest_palindrome and is_palindromic_number(product):
                largest_palindrome = product
    return largest_palindrome

def main():
    """Main method"""
    solution = largest_product_palindrome(1000)
    print(solution)


if __name__ == "__main__":
    main()
