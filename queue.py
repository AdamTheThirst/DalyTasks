'''Имитация очереди'''

from random import randint
from time import sleep

queue = list()
queue_limit = 10

for _ in range(20):
    if len(queue) >= queue_limit:
        queue.pop(queue_limit-1)
    queue.insert(0, randint(0, 100))
    print(queue)
    sleep(0.5)