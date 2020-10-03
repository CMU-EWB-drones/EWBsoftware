from shapely.geometry import Point, linestring
from shapely.geometry import Polygon
import re

# assuming size and overlap are both ints, assuming size = a square

def where_to_stop(A,B,C,D, size, overlap):
    accsize = size-overlap
    shape = [A, B, C, D]
    ex = set()
    stops = recur(A, shape, accsize, ex)
    print("stops: ", sorted(stops), "\nvisited: ", sorted(ex))
    return stops


def recur (center, shape, S, ex):         # s = actual size
    ex.add(center)
    cx,cy = center
    if not in_shape(cx, cy, shape, S):
        return set()
    up = set()
    if not (cx, cy+S) in ex:
        up = recur((cx, cy+S), shape, S, ex)
    down = set()
    if not (cx, cy-S) in ex:
        down = recur((cx, cy-S), shape, S, ex)
    left = set()
    if not (cx+S, cy) in ex:
        left = recur((cx+S, cy), shape, S, ex)
    right = set()
    if not (cx-S, cy) in ex:
        right = recur((cx-S, cy), shape, S, ex)
    # print({center}.union(up, down, left, right))
    return {center}.union(up, down, left)


def in_shape(cx, cy, shape, S): #assuming abcd are clockwise
    poly = Polygon(shape)
    square = Polygon(
        [(cx - S / 2, cy - S / 2), (cx + S / 2, cy - S / 2), (cx + S / 2, cy + S / 2), (cx - S / 2, cy + S / 2)])
    # print ("in shape?: ", point, shape, poly.contains(p) or (poly.boundary.distance(p) < 10**(-5)), "area? ", str(poly.area))
    return poly.intersects(square)


def main():
    spoints = input("4 points in (x,y) form please (no spaces after the comma)!  ")
    size = 0
    while size == 0:
        try:
            size = int(input("size of square: ").strip())
        except ValueError:
            print("REEEE that was not an int, why don't u try again honey.")
    overlap = 0
    while overlap == 0:
        try:
            overlap = int(input("overlap value: ").strip())
        except ValueError:
            print("REEEE that was not an int, why don't u try again honey.")
    points = re.findall(r'\(\d+,\d+\)', spoints)
    # print("---", points)
    for i in range(len(points)):
        points[i] = eval(points[i].strip())
    A, B, C, D = points

    where_to_stop(A, B, C, D, size, overlap)


main()

# (0,0) (0,10) (10,10) (10,0)
