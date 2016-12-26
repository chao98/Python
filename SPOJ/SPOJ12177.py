
def retChar(isStar):
    charbuf = '*.'

    if isStar:
        return charbuf[0]
    else:
        return charbuf[1]

def retCharline(isTopOrBottom, n):
    if isTopOrBottom:
        return ''.join(['*' for i in range(n)])
    else:
        result = []
        for i in range(n):
            if i == 0 or i == n-1:
                result.append(retChar(True))
            else:
                result.append(retChar(False))
        return ''.join(result)

def retCharMatrix(r, c):
    result = []
    for i in range(r):
        isTopOrBottom = False
        if i == 0 or i == r-1:
            isTopOrBottom = True
        result.append(retCharline(isTopOrBottom, c))

    return result

def main():
    n = int(input())

    matrix = []
    for i in range(n):
        text = input()
        row, col = text.split()
        r = int(row)
        c = int(col)
        #print('input r = {}, c = {}'.format(r, c))
        matrix.append((r, c))

    for i in range(n):
        r = matrix[i][0]
        c = matrix[i][1]
        result = retCharMatrix(r, c)
        for j in range(r):
            print(result[j])
        print()

if __name__ == '__main__':
    # http://www.spoj.com/problems/CPTTRN2
    main()