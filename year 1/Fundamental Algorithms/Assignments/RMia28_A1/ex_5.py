def array(x):
    """
    Description: Determines the value of the element at index x
                 in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...
    Input: x - int
    Output: val - int
    """
    val = 1
    crt = 0
    while crt < x:
        i = 1
        while crt < x and i <= val:
            crt = crt + 1
            i = i + 1
        if crt < x:
            val = val + 1
    return val

print(array(35))
