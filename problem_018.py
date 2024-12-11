# Noah Badner, 2024
#
# Maximum Path Sum I
# Problem 18
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
#
#      >3<
#    >7<  4
#   2  >4<  6
# 8   5  >9<  3
#   [included in resource files]
#
# That is, 3 + 7 + 4 + 9 = 23
# Find the maximum total from top to bottom of the triangle below:
#   [included in resource files]
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
# is the same challenge with a triangle containing one-hundred rows: it cannot be solved by brute force, and requires a
# clever method! ;o)
#
# Completed: 2021-09-11
# Solution: 1074

RESOURCE_FILE_PATH_018 = "resources/problem_018_triangle.txt"
RESOURCE_FILE_PATH_018_EX = "resources/problem_018_example.txt"

def parse_file(file_path):
    """Parses the input file and returns the triangle as a list of rows, each a list of the integers making them up"""
    ret_list = list()
    with open(file_path, 'r') as file:
        for line in file:
            ret_list.append([int(num) for num in line.split(" ")])
    return ret_list

def max_path_sum(triangle):
    """Returns the maximum path sum of a given triangle represented as a 2-dimensional array"""
    for i in range(len(triangle)):
        for j in range(len(triangle[-1-i])-1):
            triangle[-2-i][j] += max(triangle[-1-i][j], triangle[-1-i][j+1])
    return triangle[0][0]

def main():
    """Main method"""
    triangle = parse_file(RESOURCE_FILE_PATH_018)

    solution = max_path_sum(triangle)
    print(solution)


if __name__ == "__main__":
    main()
