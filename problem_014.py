# Noah Badner, 2024
#
# Longest Collatz Sequence
# Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#   n -> n/2 (n is even)
#   n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#   13 -> 40 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 items. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Completed: 2021-09-06
# Solution: 837799

# TODO: Optimize collatz chain search by noticing that collatz chains computed already terminate, so if a value below
#   'n' is reached, it must terminate in exactly the length of the previously calculated collatz_chain(n)

def collatz_chain(n):
    """Returns a recursively calculated Collatz sequence"""
    if n == 1:
        return (1,)
    elif n % 2 == 0:
        return (n,) + collatz_chain(n//2)
    else:
        return (n,) + collatz_chain(3*n + 1)

def longest_collatz_seed_below(n):
    """Returns the seed value below the given upper bound n that produces the longest Collatz sequence"""
    longest_collatz = (1, 1)  # (seed, length)
    for i in range(2, n):
        temp_length = len(collatz_chain(i))
        if temp_length > longest_collatz[1]:
            longest_collatz = (i, temp_length)
    return longest_collatz[0]

def main():
    """Main method"""
    solution = longest_collatz_seed_below(1000000)
    print(solution)


if __name__ == "__main__":
    main()
