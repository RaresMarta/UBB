from point import *
from PointRepository import *
from utils import *


def test_create_point():
    p1 = MyPoint(4, 5, 'blue')
    p2 = MyPoint(5, 7, 'yellow')
    p3 = MyPoint(1, 4, 'magenta')
    assert p1.get_x() == 4 and p1.get_y() == 5 and p1.get_color() == 'blue'
    assert p2.get_x() == 5 and p2.get_y() == 7 and p2.get_color() == 'yellow'
    assert p3.get_x() == 1 and p3.get_y() == 4 and p3.get_color() == 'magenta'

def test_add():
    repo = PointRepository()
    repo.add(1, 2, 'red')
    assert len(repo.get_points()) == 1


def test_get_all_points():
    repo = PointRepository()
    repo.load_predefined_points()
    all_points = repo.get_all_points()
    assert len(all_points) == repo.get_counter()


def test_get_point_at_index():
    repo = PointRepository()
    repo.load_predefined_points()
    point = repo.get_point_at_index(1)
    assert isinstance(point, MyPoint)


def test_get_colored_points():
    repo = PointRepository()
    repo.load_predefined_points()
    colored_points = repo.get_colored_points('blue')
    assert all(point.get_color() == 'blue' for point in colored_points)


def test_get_points_inside_square():
    repo = PointRepository()
    repo.load_predefined_points()
    corner = MyPoint(1, 1, '')
    side_length = 3
    points_inside_square = repo.get_points_inside_square(corner, side_length)
    assert all(inside_square(point, corner, side_length) for point in points_inside_square)


def test_get_min_dist_points():
    repo = PointRepository()
    repo.load_predefined_points()
    min_distance = repo.get_min_dist_points()
    assert isinstance(min_distance, float)
    assert min_distance == 1.0


def test_update_point_at_index():
    repo = PointRepository()
    repo.load_predefined_points()
    new_point = MyPoint(10, 10, 'yellow')
    repo.update_point_at_index(1, new_point)
    assert repo.get_point_at_index(1) == new_point


def test_del_point_by_index():
    repo = PointRepository()
    repo.load_predefined_points()
    repo.del_point_by_index(1)
    assert len(repo.get_points()) == 4


def test_del_points_in_square():
    repo = PointRepository()
    repo.load_predefined_points()
    corner = MyPoint(1, 1, '')
    side = 3
    repo.del_points_in_square(corner, side)
    assert len(repo.get_points()) == 4


def test_get_points_inside_rectangle():
    repo = PointRepository()
    repo.load_predefined_points()
    corner = MyPoint(1, 1, '')
    length = 3
    width = 2
    points_inside_rectangle = repo.get_points_inside_rectangle(corner, length, width)
    assert all(inside_rec(point, corner, length, width) for point in points_inside_rectangle)


def test_update_point_color():
    repo = PointRepository()
    repo.load_predefined_points()
    repo.update_point_color(1, 1, 'green')
    assert repo.get_point_color_by_coord(1, 1) == 'green'


def test_del_inside_circle():
    repo = PointRepository()
    repo.load_predefined_points()
    center_x, center_y, radius = 2, 2, 1
    repo.del_inside_circle(center_x, center_y, radius)
    assert len(repo.get_points()) == 3


test_create_point()
test_add()
test_get_all_points()
test_get_point_at_index()
test_get_colored_points()
test_get_points_inside_square()
test_get_min_dist_points()
test_update_point_at_index()
test_del_point_by_index()
test_del_points_in_square()
test_get_points_inside_rectangle()
test_update_point_color()
test_del_inside_circle()

print("All tests passed!")
