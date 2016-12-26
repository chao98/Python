import logging
logging.basicConfig(level=logging.INFO)

class Mydict(dict):
    '''
    Simple dict but also support access as x.y style

    >>> d1 = Mydict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Mydict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: "Mydict" object has no attribute empty

    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            #logging.exception(e)
            raise AttributeError('"Mydict" object has no attribute %s' % item)

    def __setattr__(self, key, value):
        self[key] = value


def main():
    d = Mydict(a=1, b=2)
    print(d['a'])
    print(d.a)
    #print(d.c)
    return

if __name__ == '__main__':
    #main()
    import doctest
    doctest.testmod()
