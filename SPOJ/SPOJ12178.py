atom = [
    '..*',
    '..*',
    '***'
]

def ret_line(c):
    result = ['*' + s*c for s in atom]
    return result

def ret_matrix(r, c):
    result = []
    result.append('*' + '***' * c)

    tmp = ret_line(c)
    for n in range(r):
        result.extend(tmp)

    return result

def prt_matrix(matrix):
    for s in matrix:
        print(s)

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
        prt_matrix(ret_matrix(r, c))
        print()

if __name__ == '__main__':
    # http://www.spoj.com/status/CPTTRN3,chao98/
    main()