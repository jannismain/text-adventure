import os
import random
import sys
import time

TYPING_SPEED = 150  # wpm
immediate_print = print


def print(t, end="\n"):
    for l in str(t):
        sys.stdout.write(l)
        sys.stdout.flush()
        # if l in [',', '.', '!', '?']:
        #     time.sleep(((random.random() + 1) / 2) / 10)  # sleep in [0.05s; 0.1s]
        # else:
        time.sleep(random.random() * 10.0 / TYPING_SPEED)
    immediate_print('', end=end)
    # time.sleep(((random.random() + 1) / 2) / 10)  # sleep in [0.05s; 0.1s]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def inputn(*args, **kwargs):
    immediate_print('')
    ret = input(*args, **kwargs)
    immediate_print('')
    return ret
