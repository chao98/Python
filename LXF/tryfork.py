from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
import os
import time
import random
import subprocess

def tryforkunix(n):
    if n == 1:
        print('Must run on Unix')
        print('Process (%s) start ...' % (os.getpid()))

        pid = os.fork()
        if pid == 0:
            print('I am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid()))
        else:
            print('I (%s) just created a child process (%s).') % (os.getpid(), pid)

    return


def run_proc(name, sec):
    print('>>> Run child process (%s) with pid = %s' % (name, os.getpid()))
    print('>>> Parent process pid = %s' % os.getppid())
    while True:
        print('\t'*10, '>>> Child (%s) sleep for (%s) sec.' % (os.getpid(), sec))
        time.sleep(sec)
    return


def long_time_task(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task [%s] runs %0.3f sec.' % (name, (end - start)))


def q_write(q):
    print('>>> Process to write: %s' % os.getpid())
    for v in (chr(n) for n in range(ord('A'), ord('A')+25)):
        print('>>> Process (%s) puts %s to queue ...' % (os.getpid(), v))
        q.put(v)
        time.sleep(random.random())


def q_read(q):
    print('>>> Process to read %s' % os.getpid())
    while True:
        v = q.get(True)
        print('\t'*10, '&&& Process (%s) gets %s from queue.' % (os.getpid(), v))
        time.sleep(1)


def tryforkwindows(n):
    if n == 1:
        print('Parent process %s.' % os.getpid())
        sec = 3
        p = Process(target=run_proc, args=('test', sec))
        print('Child process will start ...')
        p.start()
        childlast = 15
        while childlast >= 0:
            print('# Parent (%s) and its child (%s).' % (os.getpid(), p.pid))
            time.sleep(1)
            childlast -= 1

        # Not successful!
        # os.kill(p.pid, signal.CTRL_C_EVENT)
        # p.join()

        print('Parent (%s) kills child (%s)' % (os.getpid(), p.pid))
        p.terminate()
        print('Child process end.')

    if n == 2:
        print('Parent process %s.' % os.getpid())
        process_num = 16
        p = Pool(process_num)
        for i in range(process_num):
            p.apply_async(long_time_task, args=(i,))

        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')

    if n == 3:
        cmd = 'ping www.baidu.com'
        print(cmd)
        r = subprocess.call(cmd.split())
        print('Exit code = ', r)

    if n == 4:
        q = Queue()
        pw = Process(target=q_write, args=(q,))
        pr = Process(target=q_read, args=(q,))
        pr.start()
        pw.start()
        pw.join()
        pr.terminate()

    return


def main():
    tryforkunix(0)
    tryforkwindows(2)
    return


if __name__ == '__main__':
    main()