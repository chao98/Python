from collections import OrderedDict

def get_input():
    n = int(input())

    psw_text_pair = OrderedDict()

    for i in range(n):
        m = int(input())
        psw = tuple(input().split()[0:m])
        text = input()
        psw_text_pair[psw] = text

        if i != n-1:
            input()

    return psw_text_pair

def calc_psw(keys):
    positions = []
    for k in keys:
        a, b = 0, 0
        for i, char in enumerate(k):
            a += ord(char) & 2**i
            tmpb = ord(char) >> ((i+3)%6)
            tmpb = tmpb & 1
            b += tmpb * (2**i)

        positions.append(a)
        positions.append(b)

    return positions

def find_code(psw_text_pair):
    for k, v in psw_text_pair.items():
        positions = calc_psw(k)
        for pos in positions:
            print(v[pos], end='')
        print()

def main():
    find_code(get_input())

if __name__ == '__main__':
    # http://www.spoj.com/problems/HS12HDPW
    main()
