def convert_to_miles(km: int) -> float:
    """This function does the convertion from kilometers(km) to miles(m)
    >>>convert_to_miles(9.55)
    15.280000000000001
    >>>convert_to_miles(7)
    11.200000000000001"""
    m = km * 1.6
    return m

print(convert_to_miles(9.55))