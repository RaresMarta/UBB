from PointRepository import *

print("Points")
print("1. Add a point to the repository")
print("2. Get all points")
print("3. Get a point at a given index")
print("4. Get all points of a given color")
print("5. Get all points that are inside a given square (up-left corner and length given)")
print("6. Get the minimum distance between two points")
print("7. Update a point at a given index")
print("8. Delete a point by index")
print("9. Delete all points that are inside a given square")
print("10. Plot all points in a chart")
print("Bonus:")
print("12. Get all points that are inside a given rectangle (up-left corner, length and width given)")
print("15. Update the color of a point given its coordinates")
print("19. Delete all points that are inside a given circle")
print("0. Stop executing")

def ui():
    """
    Description: User interface to navigate through multiple options
    """
    repo = PointRepository()
    repo.load_predefined_points()
    option = -1
    while option != 0:
        print("")
        option = read_option()
        if option == 1:
            print("Add a point: ")
            x = read_x()
            y = read_y()
            c = read_color()
            repo.add(x,y,c)

        elif option == 2:
            l = repo.get_all_points()
            crt = 1
            for point in l:
                print(str(crt)+'.', point)
                crt = crt + 1
            repo.plotallpoints()

        elif option == 3:
            i = int(input("Index to get point from: "))
            while i > repo.get_counter():
                i = int(input("Invalid index, try again: "))
            print(repo.get_point_at_index(i))
            repo.plot_points_in_array([repo.get_point_at_index(i)])


        elif option == 4:
            print("Print all points of a given color")
            c = read_color()
            #print(repo.get_colored_points(c))
            lst = repo.get_colored_points(c)
            repo.plot_points_in_array(lst)

        elif option == 5:
            print("Get all points that are inside a given square")
            print("Input coordonates of left-up corner of square:")
            x = read_x()
            y = read_y()
            corner = MyPoint(x,y,'')
            print("Input side lenght of square: ")
            l = int(input("l = "))
            pArray = repo.get_points_inside_square(corner,l)
            repo.plot_points_in_array(pArray)                      # plot
            for i in range(len(pArray)):                           # and show in console
                print(str(i+1)+'.', str(pArray[i]))


        elif option == 6:
            print("Minimum distance between 2 points:")
            print(repo.get_min_dist_points())

        elif option == 7:
            print("Update a point at a given index")
            i = int(input("Input index: "))
            while i > repo.get_counter():
                i = int(input("Invalid index, try again: "))
            old = repo.get_point_at_index(i)
            print("Input a point")
            x = read_x()
            y = read_y()
            c = read_color()
            new = MyPoint(x, y, c)
            repo.update_point_at_index(i, new)
            if old != new:
                print("Update successful!")

        elif option == 8:
            print("Delete a point by index")
            actual_counter = repo.get_counter()
            i = int(input("Input index: "))
            while i > actual_counter:
                i = int(input("Invalid index, try again: "))
            repo.del_point_by_index(i)
            new_counter = repo.get_counter()
            if actual_counter > new_counter:
                print("Point deleted successfully!")

        elif option == 9:
            print("Delete all points inside a given square")
            print("Input left-up corner of the square")
            x = read_x()
            y = read_y()
            lc = MyPoint(x,y,'')
            lenght = int(input("Side lenght = "))
            repo.del_points_in_square(lc,lenght)

        elif option == 10:
            repo.plotallpoints()

        elif option == 12:
            print("Input left-up corner of rectangle")
            x = read_x()
            y = read_y()
            corner = MyPoint(x,y,'')
            L = int(input("Input rectangle lenght: "))
            W = int(input("Input rectangle width: "))
            pArray = repo.get_points_inside_rectangle(corner, L, W)
            repo.plot_points_in_array(pArray)                           # plot
            for i in range(len(pArray)):                                # and show in console
                print(str(i+1)+'.', str(pArray[i]))

        elif option == 15:
            print("Enter point coordonates to modify it's color")
            x = read_x()
            y = read_y()
            if repo.point_exist(x,y) == False:
                print("Invalid point, try again by pressing 15")
            else:
                print(f"Choose a new color for the point (Current color is {repo.get_point_color_by_coord(x,y)})")
                c = read_color()
                repo.update_point_color(x,y,c)
                print("Point color modified!")

        elif option == 19:
            print("Enter circle center coordonates and radius in order to delete the points from it")
            ox = read_x()
            oy = read_y()
            r = int(input("Radius: "))
            repo.del_inside_circle(ox,oy,r)
            print("Points deleted!")


ui()

