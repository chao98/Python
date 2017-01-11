class Solution(object):
    def convert(self, s, numRows):
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this,
        P   A   H   N
        A P L S I I G
        Y   I   R
        so, read line by line: "PAHNAPLSIIGYIR".
        :param s: str
        :param numRows: int
        :return: str

        >>> zigzag = Solution()
        >>> s = 'PAYPALISHIRING'
        >>> n = 3
        >>> r = zigzag.convert(s, n)
        >>> print(r)
        PAHNAPLSIIGYIR
        """
        result = [''] * numRows
        index, step = 0, 1
        for e in s:
            # print(index)
            result[index] += e
            if index == 0:
                step = 1
            if index + 1 == numRows:
                step = -1
            index += step

        return ''.join(result)


def main():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()