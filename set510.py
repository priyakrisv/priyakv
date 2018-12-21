def is_power_of_two(n):
    """Return True if n is a power of two."""
    if p <= 0:
        return False
    else:
        return p & (p - 1) == 0
 
 
p = int(input('Enter a number: '))
 
if is power of two(p):
    print('{} is a power of two.'.format(p))
else:
    print('{} is not a power of two.'.format(p))
