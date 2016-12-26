def split_list(alist, c):
    found = False
    start, end = -1, -1

    splitted = []
    for i, elem in enumerate(alist):
        if elem != c and found is False:
            start = i
            found = True
        if (elem == c or i == len(alist)-1) and found is True:
            if i == len(alist) - 1:
                end = i + 1
            else:
                end = i
            found = False
            splitted.append(alist[start:end])

    return splitted

def main():
    n = int(input())

    for i in range(n):
        c, *s = input().split()
        print(s)
        print(split_list(s, c))

if __name__ == '__main__':
    main()