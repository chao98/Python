import string

def chlst(row, col):
    charbuf = '*.'

    result = []
    if row % 2 == 0:
        for i in range(col):
            result.append(charbuf[i%2])
    else:
        for i in range(col):
            result.append(charbuf[(i+1)%2])

    return ''.join(result)


def main():
    n = int(input())

    matrix = []
    for i in range(n):
        text = input()
        row, col = text.split()
        r = int(row)
        c = int(col)
        print('input r = {}, c = {}'.format(r, c))
        matrix.append((r, c))

    for i in range(n):
        for j in range(matrix[i][0]):
            print(chlst(j, matrix[i][1]))

        print()

if __name__ == '__main__':
    # http://www.spoj.com/problems/CPTTRN1
    main()