#!/usr/bin/python3
import os
import sys
import random


def fork():
    fork_return = os.fork()
    if fork_return == 0:
        random_num = random.randint(5, 10)
        os.execl('./child.py', './child.py', str(random_num))
    else:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {fork_return}.')


n = int(sys.argv[1])
for i in range(n):
    fork()
while n > 0:
    child_pid, status_ind = os.wait()
    status = status_ind >> 8
    print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit status {status}.')
    if status == 0:
        n -= 1
    else:
        fork()
os._exit(os.EX_OK)
