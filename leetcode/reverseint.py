class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        >>> x = 123
        >>> s = Solution()
        >>> s.reverse(x)
        321
        >>> x = -123
        >>> s.reverse(x)
        -321
        >>> x = 1534236469
        >>> s.reverse(x)
        0
        >>> x = -2147483412
        >>> s.reverse(x)
        -2143847412
        """

        result = 0

        if x > 0x574089f4 or x == 0 or x < -1563847412:
            return 0
        y = abs(x)

        while y != 0:
            tail = y % 10
            newresult = result * 10 + tail
            if (newresult - tail)//10 != result:
                return 0
            result = newresult
            y //= 10

        return result if x > 0 else -result

if __name__ == '__main__':
    import doctest
    doctest.testmod()