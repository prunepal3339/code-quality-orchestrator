from threading import Semaphore, Barrier, Thread

class H2O:
    def __init__(self):
        self.h_semaphore = Semaphore(2)
        self.o_semaphore = Semaphore(1)
        self.barrier = Barrier(3)

    def hydrogen(self, releaseHydrogen):
        self.h_semaphore.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.h_semaphore.release()

    def oxygen(self, releaseOxygen):
        self.o_semaphore.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.o_semaphore.release()

def releaseHydrogen():
    print("H", end='')

def releaseOxygen():
    print("O", end='')

def run():
    h2o = H2O()
    water = "HHO" * 5  # 5 جزيئات ماء: 10 H و 5 O
    threads = []

    for atom in water:
        if atom == 'H':
            threads.append(Thread(target=h2o.hydrogen, args=(releaseHydrogen,)))
        else:
            threads.append(Thread(target=h2o.oxygen, args=(releaseOxygen,)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print()

if __name__ == "__main__":
    run()
