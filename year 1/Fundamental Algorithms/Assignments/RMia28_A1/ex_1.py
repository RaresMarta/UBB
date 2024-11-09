
def control_digit1(x):
    """
    Description: Returns the control digit of x
    Input: x - int
    Output: control digit of x
    """
    while x > 9:
        s = 0
        while x != 0:
            s = s + x%10
            x = x // 10
        x = s
    return x

def control_digit2(x):
    if x == 0: return 0
    if x % 9 == 0: return 9
    return x % 9

print(control_digit(123))
