from collections import namedtuple


def ndtuple(n):
    if n == 1:
        # refer http://xianglong.me/article/learn-python-10-defaultdict-namedtuple/
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(1, 2)
        print(p.x, p.y)
        C = namedtuple('Circle', ['x', 'y', 'r'])
        c = C(1, 2, 3)
        print(c.x, c.y, c.r)
        print(c)


def main():
    ndtuple(1)


if __name__ == '__main__':
    main()