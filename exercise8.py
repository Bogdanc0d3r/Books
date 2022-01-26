def total_length(s1: str, s2: str)-> int:
    """Return the sum of the lengths of s1 and s2.
    
    >>>total_length('yes','no')
    5
    >>>total_length('yes','')
    3
    >>>total_length('YES!!!!', 'Noooooo')
    15"""

    full_length = len(s1) + len(s2)
    return full_length

print(total_length('bughi', 'ermurachi'))