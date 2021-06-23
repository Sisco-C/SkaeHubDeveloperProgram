def is_power_of_two(n):

    if (n == 0):
        return False
    while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
    return True   
 
 
n = int(input('Enter a number: '))
 
if is_power_of_two(n):
    print('{} is a power of four.'.format(n))
else:
    print('{} is not a power of four.'.format(n))