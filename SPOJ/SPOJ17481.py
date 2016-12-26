def is_seq(seq, b=True):
    #print(seq)
    if b is False:
        seq.reverse()

    if len(seq) == 1:
        return True
    else:
        for i in range(1, len(seq)):
            if seq[i-1] >= seq[i]:
                return False

    return True

def main():
    n = int(input())
    s = [int(a) for a in input().split()[0:n]]

    #print(s)
    for i in range(n):
        s1 = is_seq(s[0:i+1], False)
        s2 = is_seq(s[i+1:n], True)

        if (s1 and s2) is True:
            print('Yes')
            return

    print('No')
    return

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPSEQ7/
    main()