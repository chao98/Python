import string

def main():
    n = int(input())

    inputTextList = []

    for i in range(n):
        inputTextList.append(input())

    for i in range(n):
        text = inputTextList[i]
        print(''.join([c for c in text[0:len(text)//2:2]]))

if __name__ == '__main__':
    # http://www.spoj.com/problems/STRHH
    main()