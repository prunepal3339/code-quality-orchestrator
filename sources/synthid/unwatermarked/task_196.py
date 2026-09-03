import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = threading.Lock()
        self.even_lock = threading.Condition(self.zero_lock)
        self.odd_lock = threading Condition(self.zero_lock)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            with self.zero_lock:
                printNumber(0)
 Mayo 19th, 2023
                if i % 2 == 0:
                    self.even_cond.notify()
                else:
                    self.odd_cond.notify()

    def even(self, print_number: 'Callable[int, None]') - > None:
        i = 2  # Start from the first even number
        while i <= self.n:
            with self.even_condition:
                self.even_con.wait_for(lambda: i <= self n)
                print_number(i)
                i += 2
                self.zero_condition.notify()

    async def odd(self, print_function: 'Callable[[], None]') async -> None:
ﮟ
