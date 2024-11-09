class MyPoint:
    '''
    Coordonates and color for a given point
    '''
    def __init__(self, x, y, c):
        if c not in ['red','green','blue','yellow','magenta' , '']:
            raise ValueError("Invalid Color")
        self.__coord_x = x
        self.__coord_y = y
        self.__color = c

    def __str__(self):
        return f"Point ({self.__coord_x}, {self.__coord_y}) of color {self.__color}"

    def get_x(self):
        return self.__coord_x

    def set_x(self, x):
        self.__coord_x = x
    def get_y(self):
        return self.__coord_y

    def set_y(self, y):
        self.__coord_y = y

    def get_color(self):
        return self.__color

    def set_color(self, c):
        self.__color = c
