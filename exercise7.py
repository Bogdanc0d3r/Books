def repeat(s: str, n: int) -> str:
    """ Return s repeated n times, if n is negative, return an empty string.
    
    >>>repeat('yes', 4)
    'yesyesyesyes'
    >>>repeat('no', 0)
    
    >>>repeat('no', -2)
    
    >>>repeat('yesnomaybe')
    'yesnomaybeyesnomaybeyesnomaybe' """
    if n > 0:
        return s*n
    else:
        return print('') 


print(repeat('bughi ', 5))