import sys
from os import path
sys.path.append(path.join(path.dirname(path.abspath(__file__)), ".."))


import timer.timer as t


def test_add():
    assert t.add(2, 4) == 6


def test_mul():
    assert t.mul(3, 5) == 15
