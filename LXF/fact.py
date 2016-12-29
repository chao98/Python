def fact(n):
    '''
    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(0)
    Traceback (most recent call last):
    ...
    ValueError

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n-1)


def param1(*pl):
    for p in pl:
        print(p, end=', ')
    return


def main():
    param_a = list(range(10))
    param1(*param_a)

if __name__ == '__main__':
    main()
    #import doctest
    #doctest.testmod()