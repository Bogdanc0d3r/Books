def weeks_elapsed(day1: int, day2: int):
    """(int, int) -> int
    day1 ad day2 are days in the same year. Return the number of full weeks that have elapsed between
    the two days
    >>>weeks_elapsed(3, 20)
    2
    >>>weeks_elapsed(20, 3)
    2
    >>>weeks_elapsed(8,5)
    >>>weeks_elapsed(40,61)
    3
    """
    full_weeks = abs((day1-day2)/7)
    return int(full_weeks)

print(weeks_elapsed(40,61))