from collections import OrderedDict
from functools import reduce
from functools import wraps


def crtOrderedDict():
    od = OrderedDict()
    od['z'] = 1
    od['y'] = 2
    od['x'] = 3

    return od


def extractList():
    l1 = list(range(10))
    tmpDict = dict()
    for i in range(10):
        if i < 9:
            tmpDict[i] = tuple(l1[i:i+2])
        else:
            tmpDict[i] = (l1[i], l1[0])

    print(tmpDict)


def prtDict(ODict):
    for k, v in ODict.items():
        print('k -> {}, v -> {}'.format(k, v))


def str2int():
    l = ['1', '2', '3', '4', '5']
    str_l = map(int, l)
    print(str_l)
    x, *y = str_l
    print(x, y)


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_dividable(n):
    return lambda x: x % n != 0


def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_dividable(n), it)


def str2int(s):
    def fn(x, y):
        return 10 * x + y

    def char2num(c):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
                '6':6, '7':7, '8':8, '9':9}[c]
    return reduce(fn, map(char2num, s))


def yang_triangles():
    L = [1]
    yield L
    L = [1, 1]
    yield L

    while True:
        L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]
        yield L

def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))

    s1, s2 = s.split('.')
    i1 = str2int(s1)
    i2 = str2int(s2) / 10**len(s2)

    return i1+i2


def is_palindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i] != s[i-1]:
            return False
    return True


def count():
    def f(j):
        def g():
            return j*j
        return g

    '''
    fs = []
    for i in range(1, 4):
        fs.append(f(i))

    return fs
    '''
    return [f(i) for i in range(1, 4)]


def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Before call')
            print('%s %s():' % (text, func.__name__))
            func(*args, **kwargs)
            print('After call')
            return
        return wrapper
    return decorator


@log('Excute')
def now(text):
    print(text, '2016-12-23')


def Fib(limit=10):
    n, a, b = 0, 0, 1
    while n < limit:
        yield b
        a, b = b, a + b
        n += 1

def main():
    #od = crtOrderedDict()
    #prtDict(od)
    #extractList()
    #str2int()

    '''
    # Gen prime data, using generator
    n = int(input())
    for i, p in enumerate(prime()):
        print('{}'.format(p), end=', ')
        if (i+1) % 20 == 0:
            print()
        if i == n:
            break
    '''

    '''
    # Using reduce/map to translate input string to int
    x = input()
    print(str2int(x))
    '''

    '''
    x = int(input())
    n = 0
    for L in yang_triangles():
        print(L)
        n += 1
        if n == x:
            break
    '''

    '''
    # Using reduce/map/lambda to translate input string to float
    x = input()
    print(str2float(x))
    '''

    '''
    # 返回函数，注意闭包
    for f in count():
        print(f())
    '''

    # decorator
    #now('Cloudy')

    print('Fib seq')

    for i, fib in enumerate(Fib(22)):
        print('%5d' % fib, end=', ')
        if (i+1) % 8 == 0:
            print()
        if i+1 >= 20:
            print()
            break

    f = Fib()
    print('Try 1: ', next(f))
    print('Try 2: ', next(f))
    print('Try 3: ', next(f))

if __name__ == '__main__':
    main()
