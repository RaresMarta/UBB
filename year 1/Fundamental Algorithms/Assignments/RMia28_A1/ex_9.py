
def last_digit():
    """
    Description: Prints all the numbers with maximum 2 digits of form XY with
                 the property that the last digit of (XY)^2 is Y
    Input: None
    Output: Prints the specified numbers
    """
    for i in range(1,100):
        if (i*i)%10 == i%10:
            print(i)
            
print(last_digit())
