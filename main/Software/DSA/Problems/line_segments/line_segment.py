# test case 1: can draw line
import math
from testcases import get_cases

def get_angle(x, y):
    angle = math.atan2(x, y)
    return math.degrees(angle)

def can_draw_line(case):

    # transform line segments into ranges of angles
    angles = []
    for line in case:
        start = get_angle(line[0][0], line[0][1])
        end = get_angle(line[1][0],line[1][1])
        if (end - start) % 360 > 180:
            start, end = end, start
        # we want to draw a straight line so a line segment blocking one side also blocks the other
        start %= 180
        end %= 180
        angles.append([start, end])

    # flatten the circle of angles, handle the edge
    for  i, angle in enumerate(angles):
        if angle[0] > angle[1]:
            angles[i] = [angle[0], 180]
            angles.append([0,angle[1]])
    angles.sort()

    # see if there is any space to fit a line
    if angles[0][0] > 0 or angles[-1][1] < 180: return True
    mx = angles[0][1]
    for i in range(len(angles)-1):
        if angles[i][1] < angles[i+1][0] and angles[i+1][0] > mx: return True
        mx = max(mx, angles[i][1])
    return False

cases = get_cases()
for case in cases:
    print(can_draw_line(case))

