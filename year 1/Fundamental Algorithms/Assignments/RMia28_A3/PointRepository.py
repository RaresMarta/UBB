from point import *
from utils import *
import math
from matplotlib import pyplot as plt

class PointRepository:
    def __init__(self):
        self.__points = []
        self.__counter = 0

    def get_points(self):
        '''
        :return: The list of points in the repository
        '''
        return self.__points

    def set_points(self, new_list):
        '''
        Sets the list of points to a new lists
        '''
        self.__points = new_list.copy()

    def get_counter(self):
        '''
        :return: The number of elements in the list of points
        '''
        return self.__counter

    def set_counter(self, new_crt):
        '''
        Sets the number of elements in the point list
        '''
        self.__counter = new_crt

    def add(self, x, y, c): # 1
        '''
        Description: Adds a point to the repository and increases the counter of points
        :param p: point
        '''
        p = MyPoint(x,y,c)
        self.__points.append(p)
        self.__counter += 1

    def get_all_points(self): # 2
        '''
        Description: Prints all of the points from the repository (points list)
        '''
        aux_list = []
        for p in self.__points:
            aux_list.append(p)
        return aux_list

    def get_point_at_index(self, index): # 3
        '''
        Description: Returns a point at a given index in the repository (point list)
        :param index: point location in repository
        '''
        return self.__points[index-1]

    def get_colored_points(self, color): # 4
        '''
        Description: Gets all points of a given color
        :param color:
        :return: aux_list - list of points of the desired color
        '''
        aux_list = []
        for point in filter(lambda p: p.get_color() == color, self.__points):
            aux_list.append(point)
        return aux_list

    def get_points_inside_square(self, corner, l): # 5
        '''
        Description: Gets points inside a given square
        :param corner: MyPoint object - left-up corner of square
        :param l: lenght of the square side
        :return: aux_list - list of points that are inside the square
        '''
        aux_list = []
        for point in self.__points:
            if inside_square(point, corner, l) == True:
                aux_list.append(point)
        return aux_list

    def get_min_dist_points(self): # 6 - good
        '''
        Description: Gets the minimum distance between all of the points in the repository
        :return: min - int
        '''
        min = 99999
        a = ''
        b = ''
        for p1 in self.__points:
            for p2 in self.__points:
                if p1 != p2:
                    if dist(p1,p2) < min:
                        min = dist(p1,p2)
                        a = str(p1)
                        b = str(p2)
        print(f"Distance between {a} and {b} is: ")
        return min

    def update_point_at_index(self, index, point): # 7 - good
        '''
        Description: Replaces a point with another point in the repository list
        :param index: location in the repo. list where point will be replaced
        :param point: MyPoint object that will replace the old one
        '''
        self.__points[index-1] = point

    def del_point_by_index(self, index): # 8 - good
        '''
        Description: Delets a point at a given index in the repo. list
        :param index: location of the point to be deleted
        '''
        del self.__points[index-1]
        self.__counter = self.__counter - 1

    def del_points_in_square(self, lc, lenght):  # 9 - good
        '''
        Description: Delets points located inside a square. Left-up corner and side lenght of the square are given.
        :param lc: MyPoint object, left-up corner of the square
        :param lenght: side lenght of square
        '''
        aux_list = self.get_points_inside_square(lc, lenght)
        for point in aux_list:
            self.__points.remove(point)
            self.__counter = self.__counter - 1

    def plotallpoints(self):  # 10 - good
        for point in self.__points:
            plt.plot(point.get_x(), point.get_y(), color=point.get_color(), marker='o', markersize=10)
        plt.show()

    def get_points_inside_rectangle(self, corner, L, W):  # 12
        '''
        Description: Gets all points inside a rectangle. Left-up corner, lenght and width of rectangle are given
        :param corner: MyPoint object - left-up corner of rectangle
        :param L: int - lenght of rectangle
        :param W: int - width of rectangle
        :return: aux_list - list of points
        '''
        aux_list = []
        for point in self.__points:
            if inside_rec(point, corner, L, W):
                aux_list.append(point)
        return aux_list

    def update_point_color(self, x, y, color): #15 - good
        '''
        Description: Changes the color of a given point
        :param x: int - X coordonate of desired point
        :param y: int - Y coordonate of desired point
        :param color: string - new color to replace the old one
        '''
        ok = 0
        for point in self.__points:
            if point.get_x() == x and point.get_y() == y:
                MyPoint.set_color(point, color)
                ok = 1
        if ok == 0:
            print("Point not found, try again by pressing 15")

    def del_inside_circle(self, Ox, Oy, r): # 19
        '''
        Description: Deletes points inside a circle. Coordonates of the center of the circle and radius are given
        '''
        aux_list = []
        centre = MyPoint(Ox, Oy, '')
        for point in self.__points:
            if dist(point, centre) > r:
                aux_list.append(point)
        self.__points = aux_list.copy()
        self.__counter = len(aux_list)

    # Auxiliar Functions Below

    def plot_points_in_array(self, array):
        '''
        Plots all the points from the param array
        :param array: list of points
        '''
        for point in array:
            plt.plot(point.get_x(), point.get_y(), color=point.get_color(), marker='o', markersize=10)
        plt.show()

    def get_point_color_by_coord(self, x, y):
        '''
        Gets the colour of a point given it's coordonates
        :param x: int - coord x of point
        :param y: int - coord y of point
        :return:
        '''
        for point in self.__points:
            if point.get_x() == x and point.get_y() == y:
                return point.get_color()

    def point_exist(self, x, y):
        '''
        Checks wether  point of coordonates x and y exists in the point repository
        :param x: int - coord x of point
        :param y: int - coord y of point
        :return: boolean - True or False
        '''
        for point in self.__points:
            if point.get_x() == x and point.get_y() == y:
                return True
        return False

    def load_predefined_points(self):
        '''
        Loads the repository with 10 points for example usage
        '''
        self.__points.append(MyPoint(1,1,"blue"))
        self.__points.append(MyPoint(4, 4, "green"))
        self.__points.append(MyPoint(1, 4, 'magenta'))
        self.__points.append(MyPoint(2, 3, 'blue'))
        self.__points.append(MyPoint(2, 2, 'red'))
        self.__points.append(MyPoint(0, 1, 'yellow'))
        self.__points.append(MyPoint(-3, 1, 'green'))
        self.__points.append(MyPoint(-2, 0, 'magenta'))
        self.__points.append(MyPoint(1, 5, 'red'))
        self.__points.append(MyPoint(1, -3, 'red'))
        self.__counter = 10
