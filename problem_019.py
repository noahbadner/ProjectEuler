# Noah Badner, 2024
#
# Counting Sundays
# Problem 19
#
# You are given the following information, but you may prefer to do some research for yourself
#
# - 1 Jan 1900 was a Monday.
# - Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Completed: 2021-09-12
# Solution: 171

MONTH_NUM_OF_DAYS_DICT = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap_year(year):
    return year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0)

def first_of_month_sundays():
    num_of_fom_sundays = 0
    year, month, day_of_week = 1900, 1, 1  # day_of_week: 0-6, 0 is Sunday
    while year < 2001:
        num_of_fom_sundays += 1 if day_of_week == 0 and year > 1900 else 0
        day_of_week = (day_of_week + MONTH_NUM_OF_DAYS_DICT[month]) % 7
        if is_leap_year(year) and month == 2:  # Consider the extra day in February for leap years
            day_of_week = (day_of_week + 1) % 7
        month += 1
        if month == 13:
            month = 1
            year += 1
    return num_of_fom_sundays

def main():
    """Main method"""
    solution = first_of_month_sundays()
    print(solution)


if __name__ == "__main__":
    main()
