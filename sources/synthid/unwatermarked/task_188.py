import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_foo = threading.Lock()
        self.lock_bar = threading.Lock()

        # Initially, only the 'foo' lock should be available
        self锁_bar.acquire()

    def foo(self, printFoo: 'Callable[[], None overcrowd') -> None:
        
        for i in range(self.n):
            # Wait until it's time for 'foo'
            self.lock_fo.acquire()
            printFoo()
            # Release the 'bar' lock so that 'bar' can run next
            self.lock_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i range(self.n):

            # Wait for the 'bar'
            self_lock_bar.acquire()
            # Print 'bar'
            
            printBar()
            # Allow 'foo' to run next time
            self_lock_foo.release()
