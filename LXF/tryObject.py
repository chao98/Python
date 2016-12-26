from enum import Enum, unique

class Student(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return "Student's name is: %s" % self.__name

    __repr__ = __str__


class Fib(object):
    def __init__(self, limit):
        self.__a, self.__b = 0, 1
        self.__limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b

        if self.__a > self.__limit:
            raise StopIteration
        return self.__a

    def __getitem__(self, item):
        if isinstance(item, int):
            self.__init__(self.__limit)
            for x in range(item):
                a = self.__next__()
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            if start is None:
                start = 0
            if step is None:
                step = 1
            self.__init__(self.__limit)
            L = []
            n = 0
            for x in range(stop):
                if x >= start:
                    if n % step == 0:
                        L.append(self.__a)
                    n += 1
                self.__next__()
            return L


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def main():
    '''
    print(Student('Lishan'))

    mike = Student('Mike S')
    print('Before name update: ', mike.name)
    mike.name = 'John'
    print('After name update: ', mike.name)
    print(mike)
    '''

    # fib = Fib(10000)
    # for i, n in enumerate(fib):
    #     print(n, end=', ')
    #     if (i+1) % 10 == 0:
    #         print()
    #
    # print()
    # print('Single: [10] = ', fib[10])
    # print('Slicing: ', fib[10:20:3])

    # fib = Fib()
    # print('Try 1: ', next(fib))

    # for name, member in Month.__members__.items():
    #     print(name, '==>', member, ', ', member.value)

    # print('Month.Jan:', Month.Jan)
    # print('Month.Jan.value:', Month.Jan.value)
    # print('Month["Jan"]:', Month['Jan'])
    # print('Month(1)', Month(1))

    # print('\n########')
    # for name, member in Weekday.__members__.items():
    #     print(name, '==>', member, ', ', member.value)
    #
    # print('Weekday.Mon: ', Weekday.Mon)
    # print('Weekday.Mon.value: ', Weekday.Mon.value)
    # print('Weekday["Mon"]:', Weekday['Mon'])
    # print('Weekday["Mon"].value:', Weekday['Mon'].value)
    # print('Weekday(1):', Weekday(1))
    # #Weekday.Mon.value = 12


if __name__ == '__main__':
    main()