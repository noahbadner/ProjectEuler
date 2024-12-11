# Noah Badner, 2024
#
# Large Sum
# Problem 13
#
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#   [included in resource file]
#
# Completed: 2021-09-06
# Solution: 5537376230

RESOURCE_FILE_PATH_013 = "resources/problem_013_numbers.txt"

def parse_file(file_path):
    """Parses the resource file and returns the given list of 50-digit numbers"""
    with open(file_path, 'r') as file:
        ret_list = [int(line.replace("/n","")) for line in file]
        file.close()
    return ret_list

def main():
    """Main method"""
    solution = str(sum(parse_file(RESOURCE_FILE_PATH_013)))[:10]
    print(solution)


if __name__ == "__main__":
    main()
