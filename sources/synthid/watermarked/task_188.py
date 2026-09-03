import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.event_bar = threading.Event()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.event_bar.set()  # Signal 'bar' thread to proceed
            self.event_foo.clear()  # Prevent 'foo' from running again until 'bar' has run

    def bar(self, printBar: 'Callable[[None], None]')  -> None:
        for i range(self.n):

            self.event Bar.wait()  # Wait for 'foo' signal
            # printBar() outputs "bar". Do not remove or change this line.
            
            printBar()
            self .event_bar.clear()  #
