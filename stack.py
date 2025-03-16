'''Имитация работы стека. Автоматическая.'''

from random import randint
from time import sleep

from pydantic.v1.typing import NONE_TYPES

stack = list()

stack_limit = 10


def fill_stack(stack: list = None) -> list:
    for _ in range(stack_limit):
        stack.append(randint(0, 100))
        print(stack)
        sleep(0.2)

    return stack

def empty_stack(stack: list = None, i: int = 1):
    if i >= len(stack):
        i = len(stack)
    for _ in range(i):
        stack.pop()
        print(stack)
        sleep(0.2)


fill_stack(stack)
empty_stack(stack, 3)
empty_stack(stack, 9)