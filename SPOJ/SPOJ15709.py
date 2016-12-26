import sys
import math

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def get_interactive_input():
    n = int(input())

    circle_grps = []
    for i in range(n):
        c = input().split()
        c1 = c[0:3]
        c2 = c[3:]
        circle_grps.append([c1, c2])

    return circle_grps

def judege_relation(circle_grps):
    for circles in circle_grps:
        x1, y1, r1 = [int(a) for a in circles[0]]
        x2, y2, r2 = [int(b) for b in circles[1]]

        d = calc_distance([(x1, y1), (x2, y2)])

        if d < abs(r1-r2):
            print('I')
        elif d == abs(r1-r2):
            print('E')
        else:
            print('O')

    return

def calc_distance(two_points):
    x1, y1 = two_points[0]
    x2, y2 = two_points[1]

    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d

def main(argv=None):
    if argv is None:
        argv = sys.argv

    judege_relation(get_interactive_input())
    return

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPCIRC
    sys.exit(main())
