def prt_matrix(matrix):
    for elem in matrix:
        print(*elem)


def substitute_matrix(matrix, ci, cj):
    for elem in matrix:
        elem[cj-1] = '*'

    matrix[ci-1] = '*' * len(matrix[ci-1])

    return matrix


def draw_matrix(matrix):
    m, n, ci, cj = matrix

    picture = [['.' for i in range(n)] for j in range(m)]
    return substitute_matrix(picture, ci, cj)


def get_input():
    n = int(input())

    matrix_grps = []
    for i in range(n):
        matrix = map(int, input().split())
        matrix_grps.append(matrix)

    return matrix_grps


def main():
    for matrix in get_input():
        prt_matrix(draw_matrix(matrix))
        print()


if __name__ == '__main__':
    # http://www.spoj.com/problems/PCROSS1/
    main()
