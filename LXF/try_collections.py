from collections import namedtuple
from collections import OrderedDict


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


class LastUpdateOrderedDict(OrderedDict):
    '''
    >>> luoDict = LastUpdateOrderedDict(3)
    >>> luoDict['1'] = 1
    add: ('1', 1)
    >>> luoDict['2'] = 2
    add: ('2', 2)
    >>> luoDict['3'] = 3
    add: ('3', 3)
    >>> luoDict['2'] = 2 * 2
    set: ('2', 4)
    >>> luoDict['4'] = 4
    rm: ('1', 1)
    add: ('4', 4)
    >>> print(luoDict)
    LastUpdateOrderedDict([('3', 3), ('2', 4), ('4', 4)])

    '''
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('rm:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


def main():
    ndtuple(0)


if __name__ == '__main__':
    #main()
    import doctest
    doctest.testmod()