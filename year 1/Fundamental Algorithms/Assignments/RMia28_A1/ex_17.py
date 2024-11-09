def digits_sum(n):
    """
    Returns the sum of digits of n
    """
    sum = 0
    while n != 0:
        sum = sum + n%10
        n = n // 10
    return sum

def special_number(x):
    """
    Description: Checks if a number x is special
                 A number N is special if there is a natural number M
                 such that N = M + S(M) where S(M) is the sum of difits of M
    Input: x - int
    Output: Prints True or False if x is special or not
    """
    k = x-1
    while k + digits_sum(k) != x and k > 0:
        k = k - 1
    if k + digits_sum(k) == x:
        print("True")
    else:
        print("False")

print(special_number(1235))
