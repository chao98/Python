def main():
    x, y = [int(a) for a in input().split()]

    print(sum([n*n for n in range(x, y+1)]))

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPSUM/
    main()