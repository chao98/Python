#!c:\Python33\python.exe -tt

'''
Try to verify the content of http://blog.csdn.net/jrgao/article/details/22248

'''

def f1(a, l = []):
    print('\nWithin f1')
    print('BEFORE, id of l : content', id(l), ' : ', l)

    l.append(a)

    print('AFTER, id of l : content', id(l), ' : ', l)

    return l

def f2(a, l = None):
    print('\nWithin f2')
    print('BEFORE, id of l : content', id(l), ' : ', l)

    if l is None:
        l = []

    print('AFTER, id of l : content', id(l), ' : ', l)
    
    l.append(a)

    print('AGAIN AFTER, id of l : content', id(l), ' : ', l)

    return l

def main():
    print('Within main()')

    print('Test for f1')
    print('----------------------')
    print('id of f1 --> ', id(f1), end = '      ')
    print('id of f1.__defaults__ : content', id(f1.__defaults__), ' : ', f1.__defaults__, end = '       ')
    print('id of f1.__defaults__[0] : content', id(f1.__defaults__[0]), ' : ', f1.__defaults__[0], end = '       ')
    print()

    print('\nCalling f1(0)')
    f1(0)
    print('\nAfter calling f1(0)')
    print('id of f1 --> ', id(f1), end = '      ')
    print('id of f1.__defaults__ : content', id(f1.__defaults__), ' : ', f1.__defaults__, end = '       ')
    print('id of f1.__defaults__[0] : content', id(f1.__defaults__[0]), ' : ', f1.__defaults__[0], end = '       ')
    print()

    print('\nCalling f1(1)')
    f1(1)
    print('\nAfter calling f1(1)')
    print('id of f1 --> ', id(f1), end = '      ')
    print('id of f1.__defaults__ : content', id(f1.__defaults__), ' : ', f1.__defaults__, end = '       ')
    print('id of f1.__defaults__[0] : content', id(f1.__defaults__[0]), ' : ', f1.__defaults__[0], end = '       ')
    print()

    print('\nCalling f1(2, [10, 9])')
    f1(2, [10, 9])
    print('\nAfter calling f1(2, [10, 9])')
    print('id of f1 --> ', id(f1), end = '      ')
    print('id of f1.__defaults__ : content', id(f1.__defaults__), ' : ', f1.__defaults__, end = '       ')
    print('id of f1.__defaults__[0] : content', id(f1.__defaults__[0]), ' : ', f1.__defaults__[0], end = '       ')
    print()

    print('\nTest for f2')
    print('----------------------')
    print('id of f2 --> ', id(f2), end = '      ')
    print('id of f2.__defaults__ : content', id(f2.__defaults__), ' : ', f2.__defaults__, end = '       ')
    print('id of f2.__defaults__[0] : content', id(f2.__defaults__[0]), ' : ', f2.__defaults__[0], end = '       ')
    print()

    print('\nCalling f2(0)')
    f2(0)
    print('\nAfter calling f2(0)')
    print('id of f2 --> ', id(f2), end = '      ')
    print('id of f2.__defaults__ : content', id(f2.__defaults__), ' : ', f2.__defaults__, end = '       ')
    print('id of f2.__defaults__[0] : content', id(f2.__defaults__[0]), ' : ', f2.__defaults__[0], end = '       ')
    print()

    print('\nCalling f2(1)')
    f2(1)
    print('\nAfter calling f2(1)')
    print('id of f2 --> ', id(f2), end = '      ')
    print('id of f2.__defaults__ : content', id(f2.__defaults__), ' : ', f2.__defaults__, end = '       ')
    print('id of f2.__defaults__[0] : content', id(f2.__defaults__[0]), ' : ', f2.__defaults__[0], end = '       ')
    print()

    print('\nCalling f2(2, [10, 9])')
    f2(2, [10, 9])
    print('\nAfter calling f2(2, [10, 9])')
    print('id of f2 --> ', id(f2), end = '      ')
    print('id of f2.__defaults__ : content', id(f2.__defaults__), ' : ', f2.__defaults__, end = '       ')
    print('id of f2.__defaults__[0] : content', id(f2.__defaults__[0]), ' : ', f2.__defaults__[0], end = '       ')
    print()

    return

''' main program starts'''
if __name__ == '__main__':
    main()


