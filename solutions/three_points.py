"""
For this challenge you will be plotting a line on a Cartesian grid.

Have the function ThreePoints(strArr) read the array of strings stored in strArr which will
always contain 3 elements and be in the form: ["(x1,y1)", "(x2,y2)", "(x3,y3)"]. Your goal
is to first create a line formed by the first two points (that starts from the first point
and moves in the direction of the second point and that stretches in both directions through
the two points), and then determine what side of the line point 3 is on. The result will either
be right, left, or neither. For example: if strArr is ["(1,1)", "(3,3)", "(2,0)"] then your
program should return the string right because the third point lies to the right of the line
formed by the first two points.
"""


def ThreePointsDeterminant(strArr):
    new_list = list()
    for string in strArr:
        tmp = list()
        for i in string:
            if i.isdigit():
                tmp.append(i)
        new_list.append(tmp)
    x1, y1 = new_list[0]  # A(x1, y1)
    x2, y2 = new_list[1]  # B(x2, y2)
    x3, y3 = new_list[2]  # C(x3, y3) -- query point
    # determinant of vectors (AB, AC)
    position = (int(x2) - int(x1)) * (int(y3) - int(y1)) - \
               (int(y2) - int(y1)) * (int(x3) - int(x1))
    # compared to directed line starting from A
    if position > 0:
        return "left"
    elif position < 0:
        return "right"
    else:
        return "neither"


def ThreePointsPhysics(strArr):
    new_list = list()
    for string in strArr:
        tmp = list()
        for i in string:
            if i.isdigit():
                tmp.append(i)
        new_list.append(tmp)
    x1, y1 = new_list[0]
    x2, y2 = new_list[1]
    x3, y3 = new_list[2]
    fx = int(x2) - int(x1)
    fy = int(y2) - int(y1)
    torque = fx * (int(y3) - int(y1)) - \
             fy * (int(x3) - int(x1))
    if torque > 0:
        # torque is positive (ccw)
        return "left"
    elif torque < 0:
        # torque is negative (cw)
        return "right"
    else:
        return "neither"


print(ThreePointsDeterminant(["(1,1)", "(3,3)", "(2,0)"]))
print(ThreePointsPhysics(["(1,1)", "(3,3)", "(2,0)"]))
