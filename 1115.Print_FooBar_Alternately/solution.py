# coding=utf-8
from typing import Callable
import time

class FooBar:
    def __init__(self, n):
        self.n = n
        self.n_called_foo = 0
        self.n_called_bar = 0

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            printFoo()
            self.n_called_foo += 1
            while self.n_called_foo > self.n_called_bar:
                time.sleep(1.e-10)

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            while self.n_called_foo == self.n_called_bar:
                time.sleep(1.e-10)
            printBar()
            self.n_called_bar += 1

