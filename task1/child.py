#!/usr/bin/python3
import os
import sys
import random
import time

print(f'Child[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.')
sleep_time = int(sys.argv[1])
time.sleep(sleep_time)
print(f'Child[{os.getpid()}]: I am ended. PID {os.getpid()}. Parent PID {os.getppid()}.')
exit_code = random.randint(0, 1)
os._exit(exit_code)
