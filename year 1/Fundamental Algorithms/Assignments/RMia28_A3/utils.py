from point import *
from PointRepository import *
import math

def inside_square(p, lc, ln):
    # Checks wether a point is inside a square or not
    # Square up-left corner and side lenght are given
    x = p.get_x()
    y = p.get_y()
    xc = lc.get_x()
    yc = lc.get_y()
    if x >= xc and x <= xc + ln and y <= yc and y >= yc - ln:
        return True
    return False

def dist(p1, p2):
    #print(f"Type of p1: {type(p1)}, Type of p2: {type(p2)}")
    xa = p1.get_x()
    ya = p1.get_y()
    xb = p2.get_x()
    yb = p2.get_y()
    return math.sqrt((xb-xa)**2 + (yb-ya)**2)

def inside_rec(p, lc, le, wi):
    # Checks wether a point is inside a given rectangle or not
    x = p.get_x()
    y = p.get_y()
    xc = lc.get_x()
    yc = lc.get_y()
    if x >= xc and x <= xc + le and y <= yc and y >= yc - wi:
        return True
    return False

def read_option():
    # Input function for option in the UI
    try:
        op = int(input("Choose an option: "))
        if (op >= 0 and op <= 10) or (op in [12,15,19]):
            return op
        else:
            raise ValueError
    except ValueError:
        print("Invalid option")
        return read_option()

def read_x():
    # Reading coordonate x for a point
    try:
        x = int(input("x = "))
        return x
    except ValueError as ex:
        print("X coordonate not valid: ", ex)
        return read_x()

def read_y():
    # Reading coordonate y for a point
    try:
        y = int(input("y = "))
        return y
    except ValueError as ex:
        print("Y coordonate not valid: ", ex)
        return read_y()

def read_color():
    # Reading color attribute for a point
    try:
        c = input("color = ")
        if c not in ['red', 'green', 'blue', 'yellow', 'magenta', '']:
            raise ValueError
        else:
            return c
    except ValueError:
        print("Invalid color")
        return read_color()

