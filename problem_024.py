# Noah Badner, 2024
#
# Lexicographic Permutations
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2,
# 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#   012  021  102  120  201  210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# Completed: 2024-12-18
# Solution: 2783915460

def lexicographic_permutations(input_digits):
    """Returns a list of all lexicographic permutations of the given input digits as defined above"""
    return _lexicographic_permutations_helper(input_digits)

def _lexicographic_permutations_helper(digits_list):
    """Helper function that recursively returns a list of lexicographic permutations given an input list of digits"""
    if len(digits_list) == 1:
        return digits_list[0]
    elif len(digits_list) == 2:
        return [digits_list[0] + digits_list[1], digits_list[1] + digits_list[0]]
    else:
        ret_list = list()
        for digit in digits_list:
            temp_digits_list = [temp_digit for temp_digit in digits_list if temp_digit != digit]
            for rec_lex_list in _lexicographic_permutations_helper(temp_digits_list):
                ret_list.append(digit + rec_lex_list)
        return ret_list


def main():
    """Main method"""
    solution = lexicographic_permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])[999999]
    print(solution)


if __name__ == "__main__":
    main()
