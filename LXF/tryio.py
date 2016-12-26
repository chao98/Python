from io import StringIO
import os


def trystringio(n):
    if n == 1:
        f = StringIO()
        f.write('Hello world!')
        #s = f.readline()
        s = f.getvalue()
        print(s)

    if n == 2:
        f = StringIO('Hello!\nHi!\nGoodbye!')
        s = f.readline()
        print(s)

    if n == 3:
        f = StringIO('Hello!\nHi!\nGoodbye!')
        for l in f:
            print(l, end='')

    if n == 4:
        f = StringIO()
        f.write('Hello world!\nHi\nGoodbye!')
        print('Pos: ', f.tell())
        f.seek(0)
        for l in f:
            print(l, end='')

    return


def tryos(n):
    if n == 1:
        for k, v in sorted(os.environ.items()):
            print('k = {}, v = {}'.format(k, v))

    return


def main():
    trystringio(0)
    tryos(1)

if __name__ == '__main__':
    main()
