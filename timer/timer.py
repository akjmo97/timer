import time

def add(x, y):
    return x + y


def mul(a, b):
    return a * b


class Timer:
    def __init__(self):
        self.time = 0

    def start(self):
        self.time = time.time()

    def stop(self):
        self.time = time.time() - self.time
