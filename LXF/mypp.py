import random
import copy


def pdict(d, ident=2):
    for k, v in d.items():
        print(''*ident, k, ': ', end='')
        if not isinstance(v, dict):
            print(v)
        else:
            pdict(v, ident+2)


def mypp(des='', data=None, ident=2):
    print(des, ': ')
    #print(type(data))
    if not isinstance(data, dict):
        print(data)
    else:
        pdict(data)


def rands(n):
    a, b = ord('0'), ord('~')
    if n >= 0:
        c = map(chr, [random.randrange(a, b) for i in range(n)])
        return ''.join(c)
    else:
        return ''


def main():
    c = rands(10)
    mypp('random string', c)

    d = {'1': 1, '2': 2, '3': 3}
    mypp('a dict: ', d)

    dd = copy.deepcopy(d)
    dd['1'] = d
    mypp('2 level dict: ', dd)



if __name__ == '__main__':
    main()