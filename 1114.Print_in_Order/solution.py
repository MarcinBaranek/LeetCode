# coding=utf-8
import time


class Foo:
    def __init__(self):
        self.called = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.called = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.called < 1:
            time.sleep(1.e-12)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.called = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.called < 2:
            time.sleep(1.e-12)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.called = 0
