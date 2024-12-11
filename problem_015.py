# Noah Badner, 2024
#
# Lattice Paths
# Problem 15
#
# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#   [example image in resource file]
#
# How many such routes are there through a 20 x 20 grid?
#
# Completed: 2021-09-10
# Solution: 137846528820

def num_of_routes(n):
    """Returns the number of routes possible following the above rules for an n x n grid"""
    solved_shapes_dict = dict()  # Store previously calculated routes per shape to prevent redundant calculations
    return _check_dimensions(n, n, solved_shapes_dict)

def _check_dimensions(x, y, solved_shapes):
    """Helper function to recursively calculate the number of routes for the given dimensions x and y"""
    if (x, y) in solved_shapes.keys():
        return solved_shapes[(x, y)]
    elif (y, x) in solved_shapes.keys():
        return solved_shapes[(y, x)]
    elif x == 1:
        solved_shapes[(x, y)] = y + 1
        return y + 1
    elif y == 1:
        solved_shapes[(x, y)] = x + 1
        return x + 1
    else:
        solved_shapes[(x, y)] = _check_dimensions(x-1, y, solved_shapes) + _check_dimensions(x, y-1, solved_shapes)
        return solved_shapes[(x, y)]

def main():
    """Main method"""
    solution = num_of_routes(20)
    print(solution)


if __name__ == "__main__":
    main()
