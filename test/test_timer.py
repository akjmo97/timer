import sys
from os import path
sys.path.append(path.join(path.dirname(path.abspath(__file__)), ".."))


import timer.timer as t
import time


def test_add():
    assert t.add(2, 4) == 6


def test_mul():
    assert t.mul(3, 5) == 15


def test_time():
    timer = t.Timer()

    timer.start()
    time.sleep(2.3)
    timer.stop()

    assert 2 < timer.time < 3
