def find_divisbles(datas):
    n, x, y = [int(a) for a in datas]

    for data in range(x, n, x):
        if data % y != 0:
            print(data, end=' ')

    print()

def get_input():
    num = int(input())

    params = []
    for i in range(num):
        params.append(input().split())

    return params

def main():
    params = get_input()

    for param in params:
        find_divisbles(param)

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPDIV/
    main()