# Create a tuple that takes coordinates of a point in 3D space
# Write a function that takes this tuple and calculates the distance from the origin.
import math


def calc_distance(coordinates):
    x, y, z = coordinates
    distance = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    return distance


point = (3,4,5)
distance = calc_distance(point)
print(distance)