
def main():
    n, x = [int(a) for a in input().split()]
    s = [int(b) for b in input().split()[0:n]]
    q = [int(c) for c in input().split()[0:n]]

    result = []
    for i in range(1, n+1):
        for j in range(-x, x+1):
            if 0 <= i+j-1 < n and s[i-1] == q[i+j-1]:
                result.append(i)

    print(*result)

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPSEQ6/
    main()