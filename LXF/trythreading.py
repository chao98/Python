import time
import threading


def loop1():
    for i in range(15):
        print('\t'*8, '<<< thread (%s/%s) is running (%d)...' % (threading.current_thread().name, threading.current_thread().ident, i))
        time.sleep(1)
    return


def dispatch(n):
    if n == 1:
        print('>>> Will start thread.')
        t = threading.Thread(target=loop1, name='Loop1')
        print('>>> Main (%s) started thread (%s).' % (threading.get_ident(), threading.current_thread().name))
        t.start()
        t.join()
        print('>>> Thread (%s/%s) ended' % (threading.current_thread().name, threading.current_thread().ident))

    if n == 2:
        t1 = threading.Thread(target=run_thread, name='t8', args=(8,))
        t2 = threading.Thread(target=run_thread, name='t5', args=(5,))
        start = time.time()
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        end = time.time()
        print('Final balance is: %d; time used is: %0.3f' % (balance, (end-start)))

    if n == 3:
        t1 = threading.Thread(target=process_thread, args=('Alice',), name='T1')
        t2 = threading.Thread(target=process_thread, args=('Bob',), name='T2')
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    return


balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    thread_name = threading.current_thread().name
    j = 5
    global balance
    printed = False
    for i in range(10**(j+1)):
        lock.acquire()
        change_it(n)
        lock.release()

        # try:
        #     change_it(n)
        # finally:
        #     lock.release()

        if printed is False:
            if thread_name == 't5' and balance not in (0, 5):
                print('\t'*0, '>>> In thread (%s) and loop is (%d), balance = %d' % (thread_name, i, balance))
                printed = True
            elif thread_name == 't8' and balance not in (0, 8):
                print('\t'*8, '*** In thread (%s) and loop is (%d), balance = %d' % (thread_name, i, balance))
                printed = True

        # if i % 10**j == 0:
        #     if thread_name == 't5':
        #         print('>>> In thread (%s), balance = %d' % (thread_name, balance))
        #     else:
        #         print('\t'*8, '>>> In thread (%s), balance = %d' % (thread_name, balance))


local_info = threading.local()


def process_student():
    std = local_info.std
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(std):
    local_info.std = std
    process_student()


def main():
    dispatch(2)


if __name__ == '__main__':
    main()