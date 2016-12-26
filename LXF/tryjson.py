import json


def dictjson(n):
    if n == 1:
        d = dict(name='Bob', age=20, score=88)
        j = json.dumps(d)
        print('json.dumps: ', j)

    if n == 2:
        with open('dictjson.txt', 'w') as f:
            d = dict(name='Bob', age=20, score=88)
            json.dump(d, f)

    if n == 3:
        with open('dictjson.txt', 'r') as f:
            d = json.load(f)
            print(d)

    return

def classjson(n):

    class Student(object):
        #__slots__ = ('__name', '__age', '__score')

        def __init__(self, name, age, score):
            self.__name = name
            self.__age = age
            self.__score = score

        # @property
        # def name(self):
        #     return self.__name
        #
        # @property
        # def age(self):
        #     return self.__age
        #
        # @property
        # def score(self):
        #     return self.__score

        def __getattr__(self, item):
            if item == 'name':
                return self.__name
            if item == 'age':
                return self.__age
            if item == 'score':
                return self.__score
            raise AttributeError('"Student" object has no such attribute "%s"' % item)

        def stu2dict(self):
            # not working as expected
            return {
                'name': self.__name,
                'age': self.__age,
                'score': self.__score,
            }

    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

    def dict2student(d):
        return Student(d['name'], d['age'], d['score'])

    if n == 1:
        # Should report error, for not knowing how to dump
        s = Student('Bob', 20, 88)
        print(json.dumps(s))

    if n == 2:
        # Should succeed
        s = Student('Bob', 20, 88)
        print(json.dumps(s, default=student2dict))

    if n == 3:
        s = Student('Bob', 20, 88)
        print(json.dumps(s, default=lambda obj: obj.__dict__))

    if n == 4:
        with open('dictjson.txt', 'r') as f:
            s = json.load(f, object_hook=dict2student)
            print(student2dict(s))
    return


def trychina(n):

    class chain(object):
        def __init__(self, path=''):
            self.__path = path

        def __getattr__(self, item):
            return chain('%s/%s' % (self.__path, item))

        def __str__(self):
            return self.__path

        __repr__ = __str__

    if n == 1:
        c = chain('https://www.xxx.com')
        print(c)
    if n == 2:
        c = chain('https://www.xxx.com')
        new_c = c.user
        print(new_c)


def main():
    dictjson(0)
    classjson(0)
    trychina(2)
    return

if __name__ == '__main__':
    main()