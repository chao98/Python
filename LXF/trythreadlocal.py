import threading
import logging
local_info = threading.local()


class Student(object):
    def __init__(self, name, age, score, tID=None):
        self.__name = name
        self.__age = age
        self.__score = score
        self.__tID = None

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('Score must btw. 0~100!')

        self.__score = score

    @property
    def tID(self):
        return self.__tID

    @tID.setter
    def tID(self, tID):
        self.__tID = tID

    # def __getattr__(self, item):
    #     if item == 'tID':
    #         return self.__tID

    # def __setattr__(self, key, value):
    #     if key == 'tID':
    #         self.__tID = value

    def stud2dict(self):
        return {
            'name': self.__name,
            'age': self.__age,
            'score': self.__score,
            'tID': self.__tID
        }


def process_stud():
    n = 10**6
    for i in range(n):
        stud = local_info.stud
        if stud.name == 'Alice':
            score_adjust = 8
            stud.score -= score_adjust
            #stud.score += score_adjust

        if stud.name == 'Bob':
            score_adjust = 5
            stud.score += score_adjust
            stud.score -= score_adjust


def process_thread(stud):
    tmp = threading.current_thread().name + '/' + str(threading.get_ident())
    stud.tID = tmp
    local_info.stud = stud

    try:
        process_stud()
    except ValueError as ve:
        logging.exception(ve)


def main():
    stud_a = Student('Alice', 20, 99)
    stud_b = Student('Bob', 18, 92)

    t1 = threading.Thread(target=process_thread, args=(stud_a,), name='T1')
    t2 = threading.Thread(target=process_thread, args=(stud_b,), name='T2')

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('Alice:', stud_a.stud2dict())
    print('Bob', stud_b.stud2dict())


if __name__ == '__main__':
    main()