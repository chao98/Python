import re


def simple_re(n, s='', t=''):
    '''
    :param n:
    :param s:
    :param t:
    :return:

    >>> n = 1
    >>> s = r'^\d{3}\-\d{3,8}$'
    >>> t = '010-123456789'
    >>> simple_re(n, s, t)
    False

    >>> s = r'^\d{3}\-\d{3,8}$'
    >>> t = '010-1234567'
    >>> simple_re(n, s, t)
    True

    '''

    if n == 1:

        if re.match(s, t):
            return True
        else:
            return False

    if n == 2:
        s = r'\s+'
        t = 'a b   c'
        print(t.split(' '))
        print(re.split(s, t))
        s = r'[\s\,]+'
        t = 'a,b,  c  d'
        print(re.split(s, t))
        s = r'[\s\,\;]+'
        t = 'a, b;;  c d'
        print(re.split(s, t))

    if n == 3:
        s = r'^(\d{3})-(\d{3,8})$'
        t = '010-12345'
        m = re.match(s, t)
        prt_match(m)
        s = r'^([0-9]|0[0-9]|1[0-9]|2[0-3])\:([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\:([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$'
        t = '19:05:30'
        prt_match(re.match(s, t))

    if n == 4:
        s = r'^(\d+)(0*)$'
        t = '102300'
        prt_match(re.match(s, t))
        s = r'^(\d+?)(0*)$'
        prt_match(re.match(s, t))

    if n == 5:
        s = r'^(\d{3})-(\d{3,8})$'
        t = '010-12345'
        re_tele = re.compile(s)
        prt_match(re_tele.match(t))
        t = '010-8086'
        prt_match(re_tele.match(t))


def prt_match(m):
    print()
    if m is not None:
        print(m.groups())
        i = 0
        while True:
            try:
                print(m.group(i), end=', ')
                i += 1
            except IndexError as err:
                print()
                break
    else:
        print('Not match!')


def trydict(n):
    if n == 1:
        my_dict1 = {
            1:2,
            2:3
        }

        for k, v in my_dict1.items():
            print(k, v)


def main():
    simple_re(5)
    trydict(0)


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod()