def is_prime(n):
    """
    Description: Checks if n is prime
    Input: n - int
    Output: True or False - boolean
    """
    from math import sqrt
    if n < 2:
        return False
    for d in range(2,int(sqrt(n))+1):
        if n % d == 0:
            return False
    return True

def gcd2(a, b):
    """
    Description: Returns the greatest common divisor of 2 numbers
    Input: a, b - int
    Output: a - int
    """
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
