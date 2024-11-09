def form_number(x):
    """
    Description: Forms another number using the digits of x found at odd positions
    Input: x - int
    Output: nr - int
    """
    digit = []
    while x != 0:           #"""puts the digit of x in an array"""
        digit.append(x%10)
        x = x // 10
    k = len(digit)
    for i in range(0,int(k/2)):#    """reverses the order of elements in the array"""
        aux = digit[i]
        digit[i] = digit[k-i-1]
        digit[k-i-1] = aux
    nr = 0
    for i in range(0,k):        #"""creates the number"""
        if (i+1) % 2 != 0:
            nr = nr * 10 + digit[i]
    return nr

print(form_number(1234))
