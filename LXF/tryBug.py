import pdb
import logging
logging.basicConfig(level=logging.INFO)

def zero_div():
    try:
        print('try...')
        n = 0
        #assert n != 0, 'Error, divided by zero!'
        logging.info('n = %d' % n)
        #pdb.set_trace()
        r = 10 / n
        print('result: ', r)
    except ZeroDivisionError as err:
        print('except: ', err)
        logging.exception(err)
    except ValueError as err:
        print('except: ', err)
    else:
        print('No error!')
    finally:
        print('finally...')
    print('END')


class Mydict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            logging.exception(e)
            raise AttributeError('"Mydict" object has no attribute %s' % item)

    def __setattr__(self, key, value):
        self[key] = value


def main():
    # zero_div()

    d = Mydict(a=1, b=2)
    print(d['a'])
    print(d.a)
    print(d.c)
    return

if __name__ == '__main__':
    main()