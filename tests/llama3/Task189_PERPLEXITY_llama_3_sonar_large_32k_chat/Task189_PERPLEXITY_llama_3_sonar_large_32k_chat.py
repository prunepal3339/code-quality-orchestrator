import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        self.state = 0  # 0: zero, 1: even, 2: odd
        self.count = 1  # counter from 1 to n

    def zero(self, printNumber):
        for _ in range(self.n):
            with self.cond:
                while self.state != 0:
                    self.cond.wait()
                printNumber(0)
                self.state = 2 if self.count % 2 == 1 else 1
                self.cond.notify_all()

    def even(self, printNumber):
        while self.count <= self.n:
            with self.cond:
                while self.state != 1:
                    self.cond.wait()
                if self.count > self.n:
                    self.cond.notify_all()
                    break
                printNumber(self.count)
                self.count += 1
                self.state = 0
                self.cond.notify_all()

    def odd(self, printNumber):
        while self.count <= self.n:
            with self.cond:
                while self.state != 2:
                    self.cond.wait()
                if self.count > self.n:
                    self.cond.notify_all()
                    break
                printNumber(self.count)
                self.count += 1
                self.state = 0
                self.cond.notify_all()


def printNumber(x):
    print(x, end='')

def run():
    n = 5
    zeo = ZeroEvenOdd(n)

    t_zero = threading.Thread(target=zeo.zero, args=(printNumber,))
    t_even = threading.Thread(target=zeo.even, args=(printNumber,))
    t_odd = threading.Thread(target=zeo.odd, args=(printNumber,))

    t_zero.start()
    t_even.start()
    t_odd.start()

    t_zero.join()
    t_even.join()
    t_odd.join()
    print()

if __name__ == "__main__":
    run()
