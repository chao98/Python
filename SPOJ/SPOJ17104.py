def main():
    x = int(input())
    list_x = [int(a) for a in input().split()[0:x]]

    y = int(input())
    list_y = [int(a) for a in input().split()[0:y]]

    list_x_y = zip(list_x, list_y)

    for i, elem in enumerate(list_x_y):
        if elem[0] == elem[1]:
            print(i+1, end=' ')

    return

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPSEQ5/
    main()