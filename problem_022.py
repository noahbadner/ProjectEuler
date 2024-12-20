# Noah Badner, 2024
#
# Names Scores
# Problem 22
#
# Using names.txt [resource file: "problem_022_names.txt"], a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# Completed: 2021-09-15
# Solution: 871198282

RESOURCE_FILE_PATH_022 = "resources/problem_022_names.txt"


def parse_file(file_path):
    """Opens a resource file containing names delimited by a ',' and returns a list"""
    with open(file_path, 'r') as file:
        ret_list = file.readline().replace('"', '').split(',')
        file.close()
    return ret_list

def alphabetical_value(name):
    """Returns the alphabetical value of a given name"""
    return sum((ord(c.upper()) - 64) for c in name)

def total_name_scores(input_list):
    """Returns the total name score for a given list of names as defined above"""
    total_score = 0
    for i, name in zip(range(len(input_list)), sorted(input_list)):
        total_score += (i + 1) * alphabetical_value(name)
    return total_score

def main():
    """Main method"""
    names_list = parse_file(RESOURCE_FILE_PATH_022)

    solution = total_name_scores(names_list)
    print(solution)


if __name__ == "__main__":
    main()
