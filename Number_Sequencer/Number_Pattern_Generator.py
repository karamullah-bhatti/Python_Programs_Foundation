def number_pattern(n):
    result = ''
    if not isinstance(n,int):
        return ('Argument must be an integer value.')
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    for i in range(1,n+1):
        result = result + str(i) + ' '  
    return result.strip()
print(number_pattern())
