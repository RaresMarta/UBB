from utils import is_prime
from utils import gcd2

def add(my_list, value):
    """
    Description: Adds the element 'value' at the end of the list
    input: my_list - list
           value - int
    Output: my_list - list
    """
    my_list.append(value)
    return my_list

def insert(my_list, value, index):
    """
    Description: Inserts a value at a given index in my_list
    Input: my_list - list
           index - int
           value - int
    Output: my_list - list
    """
    my_list.insert(index, value)
    return my_list

def remove(my_list, index):
    """
    Description: Removes an element from the list located at a given index
    input: my_list - list
           index - int
    Output: my_list - list
    """
    my_list.pop(index)
    return my_list

def remove_sequence(my_list , from_index , to_index):
    """
    Description: Removes elements located between two given indexes    
    input: my_list - list
           from_index - int
           to_index - int
    output: my_list - list
    """
    for i in range(from_index, to_index+1):
        my_list.pop(from_index)
    return my_list

def replace(my_list, old, new):
    """
    Description: Replaces all old value sequences with a new value sequence
    Input: my_list - list
           old - list
           new - list
    Output: my_list - list
    """
    k = 0
    while k < len(my_list):
        i = k 
        j = 0
        while (i < len(my_list) and j < len(old)) and (my_list[i] == old[j]):
            i = i + 1
            j = j + 1
        if j == len(old):
            remove_sequence(my_list, k, i-1)
            for crt in range(len(new)-1, -1, -1):
                insert(my_list, new[crt], k)
            k = k + len(new)
        else:
            k = k + 1
    return my_list

def prime(my_list, from_index, to_index):
    """
    Description: Gets the prime numbers from the array [my_list]
                 found between indices [from_index] and [to_index]
    Input: my_list - list
           from_index - int
           to_index - int
    Output: tmp - list
    """
    tmp = []
    for i in range(from_index, to_index+1):
        if is_prime(my_list[i]) == True:
            tmp.append(my_list[i])
    return tmp

def odd(my_list, from_index, to_index):
    """
    Description: Gets the odd numbers from the array [my_list] found between
                 indices [from_index] and [to_index]
    Input: my_list - list
           from_index - int
           to_index - int
    Output: tmp - list          
    """
    tmp = []
    for i in range(from_index, to_index+1):
        if my_list[i] % 2 != 0:
            tmp.append(my_list[i])
    return tmp

def suma(my_list, from_index, to_index):
    """
    Description: Gets the sum of numbers from the array [my_list] found between
                 indices [from_index] and [to_index]
    Input: my_list - list
           from_index - int
           to_index - int
    Output: s - int          
    """
    s = 0
    for i in range(from_index, to_index+1):
        s = s + my_list[i]
    return s

def gcd(my_list, from_index, to_index):
    """
    Description: Gets the greatest common divisor of numbers from the array
                 [my_list] found between indices [from_index] and [to_index]
    Input: my_list - list
           from_index - int
           to_index - int
    Output: gcd - int          
    """
    gcd = 0
    for i in range(from_index, to_index):
        gcd = gcd2(my_list[i], my_list[i+1])
    return gcd

def max(my_list, from_index, to_index):
    """
    Description: Gets the maximum of elements between the two given index values
    Input: my_list - list
           from_index - int
           to_index - int
    Output: m - int
    """
    m = 0
    for i in range(from_index, to_index+1):
        if my_list[i] > m:
            m = my_list[i]
    return m

def filter_prime(my_list):
    """
    Description: Removes elements from the list that are not prime
    Input: my_list - list
    Output: my_list - list
    """
    i = 0
    while i < len(my_list):
        if is_prime(my_list[i]) == False:
            remove(my_list, i)
        else:
            i = i + 1
    return my_list

def filter_negative(my_list):
    """
    Description: Modifies the list by keeping only the negative numbers and removing
                 the other numbers
    Input: my_list - list
    Output: my_list - list
    """
    i = 0
    while i < len(my_list):
        if my_list[i] >= 0:
            remove(my_list, i)
        else:
            i = i + 1
    return my_list

def undo(my_list, last_option):
    """
    Description: Undo the last operation that changed the list
    Input: my_list - list
    Output: my_list - list
    """
    if last_option not in [6, 7, 8, 9, 10]:
        return my_list.pop()

def read():
    try:
        x = int(input())
        return x
    except ValueError:
        print("Only integers allowed as input, please try again")
        return read()

def list_input(crt):
    lst = []
    for i in range(0,crt):
        lst.append(read())
    return lst

