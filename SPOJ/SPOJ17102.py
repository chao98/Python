def main():
    x = int(input())
    list_x = [int(a) for a in input().split()[0:x]]

    y = int(input())
    list_y = [int(a) for a in input().split()[0:y]]

    print(*[x for x in list_x if x not in list_y])

    return

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPSEQ3/
    main()