class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int

        >>> s = Solution()
        >>> x = '12345'
        >>> s.myAtoi(x)
        12345

        >>> x = '0'
        >>> s.myAtoi(x)
        0

        >>> x = '-12345'
        >>> s.myAtoi(x)
        -12345

        >>> x = '123x45'
        >>> s.myAtoi(x)
        123
        >>> x = '+12345'
        >>> s.myAtoi(x)
        12345

        >>> x = "    010"
        >>> s.myAtoi(x)
        10

        >>> x = "     +004500"
        >>> s.myAtoi(x)
        4500
        """

        v = {'0': 0, '1': 1, '2': 2, '3': 3,
             '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9}
        r = 0
        m = 1
        for i, e in enumerate(str):
            if e != ' ':
                str = str[i:]
                break

        if len(str) == 0:
            return 0
        else:
            if str[0] == '-':
                m = -1
                str = str[1:]
            elif str[0] == '+':
                str = str[1:]

        for e in str:
            if e in v:
                r = r * 10 + v[e]
            else:
                break
        return r * m


if __name__ == '__main__':
    import doctest
    doctest.testmod()