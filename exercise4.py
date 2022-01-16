from audioop import avg
import random
def avg_grade(a: int, b: int) -> float:
    """This function returns the average of 3 random integers within a range, in the examples below
    the range will be (0, 100) 
    >>>avg_grade(0,100)
    41.666666666666664
    >>>avg_grade(0,100)
    18.333333333333332
    >>>avg_grade(0,100)
    53.666666666666664"""
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    num3 = random.randint(a, b)
    avg = (num1 + num2 + num3)/3
    return avg

print(avg_grade(0,100))
help(avg_grade)