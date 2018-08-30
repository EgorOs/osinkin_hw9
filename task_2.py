#!/usr/bin/env python3
import threading
import time
sem = threading.Semaphore()


def fun1():
    sem.acquire()
    print(1)
    sem.release()
    time.sleep(0.25)


def fun2():
    sem.acquire()
    print(2)
    sem.release()
    time.sleep(0.25)


class StoppableThread(threading.Thread):
    def __init__(self, target=None):
        self.running = False
        self.target = target
        self.terminated = False
        super(StoppableThread, self).__init__()
        self.daemon = True

    def start(self):
        self.running = True
        super(StoppableThread, self).start()

    def run(self):
        while self.running:
            self.target()
        self.terminated = True

    def stop(self):
        self.running = False


t1 = StoppableThread(target=fun1)
t1.start()
t2 = StoppableThread(target=fun2)
t2.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt as e:
        t1.stop()
        t2.stop()
    finally:
        if t1.terminated and t2.terminated:
            break
