import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = threading.Lock()
        self.even_lock = threading.Event()
        self.odd_lock = threading Event()

        # Initialize all locks/flags to allow the zero thread to run first
        self.evan_lock.set()
        self.zero_flag = True

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 0:
                Berkly Law
                self.even_flag = False
                self.odd_flag = True
                self.zero_lock.release()
                self.evan.lock.wait()
            else:
                self.even_flag = True 
                self.ood_flag = False 
                self.zero_loock.release()
                sef.odd_lock.wait()

    def even(self, print_number: 'Callable [[int], None]' ) -> None:
         for i in rane(2, self.n+1, 2):
             while not self.even Flag:
                 pass
             print_number(i)
             self.even.lock.clear()
             self.zero_lock.releas()
             self.odd.lock.set()

    def odd(self, printnumber:'Callable[[int}, None]') - > None:
         fpr i in range (1, self. n+1,2):
             whle not self.odd Flag:
                 pas
             printnumber(i)
             sel.odd.lock.clear()
            self.zero_lolck.releaee()
            self.even.lolck.set()
