import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a_point, b_point):
	ax = a_point.x
	ay = a_point.y
	bx = b_point.x
	by = b_point.y
	return f'{math.sqrt((bx - ax)**2 + (by - ay)**2)}'


points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]


def all_distance(dict_points):
	sum_distance = 0 
	for i in range(0, len(points) - 1):
		sum_distance += float(distance(points[i], points[i+1]))
	return sum_distance


print("Длина ломаной линии = ", all_distance(points))


##Андреев Арсений
