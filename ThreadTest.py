from concurrent.futures import ThreadPoolExecutor
from threading import Thread


class ConsumerThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        pass


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    executor.submit()
