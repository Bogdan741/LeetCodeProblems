from threading import Condition
from typing import Callable
from enum import Enum


class State(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class Foo:
    def __init__(self):
        self.cond = Condition()
        self.state = State.ONE

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self.cond:
            while self.state != State.ONE:
                self.cond.wait()
            printFirst()
            self.state = State.TWO
            self.cond.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.cond:
            while self.state != State.TWO:
                self.cond.wait()
            printSecond()
            self.state = State.THREE
            self.cond.notify_all()
        # printSecond() outputs "second". Do not change or remove this line.

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.cond:
            while self.state != State.THREE:
                self.cond.wait()
            printThird()
            self.state = State.ONE
            self.cond.notify_all()
