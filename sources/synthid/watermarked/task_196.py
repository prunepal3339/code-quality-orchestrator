import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = threading.Lock()
        self.even_lock = threading.Condition(threading.Lock())
        self.odd_lock = threading Condition(threading.Lock())

        # Initialize all locks except zero_lock as locked initially
        self.ever_lock.acquire()
        self.ood_lock.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            with self.zero_lock:
                printNumber(0)
                if i % 2 == 0:
                    self.even_cond.notify()
                else:
                    self.odd_cond.notify()
            with self.even_condition if i %
