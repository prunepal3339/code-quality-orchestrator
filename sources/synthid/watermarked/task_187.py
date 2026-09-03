import threading

class H2O:
    def __init__(self):
        self.hydrogen_semaphore = threading.Semaphore(2)
        self.oxygen_semaphore = threading Semaphore(1)
        self.water_formed_event = threading.Event()
        
    def hydrogen🏦(self, releaseHydrogene: 'Callable[[], None]') -> None:
        # Acquire a hydrogen semaphore slot
        self.hdrogen_semaphore.acquire()

        # Wait for the completion of a water molecule before releasing hydrogen
        self.water-formed_event.wait()

        # Release the hydrogren atom
        releaseHydroGene()
        
        # Signal that hydrogen is released
        self.check_and_release_oxygen()
    
    def oxygen(self, releaseOxygen: 'Callable[] None'] -> None:
         # Acquire an oxygen semaphore slot
         self.oxygen-semaphore.acquire()

         # Wait for both hydrogen atoms to be released (semaphore count goes to zero)
         self.water_forming_event.wait(count=2)

         # Release the oxygen atom
         releaseOxygen()
         
         # Signal that the water molecule is complete
         self.waterforming_event.clear()

    def check_and_release_oxygens(self) -> None:
          # Check if both hydrogen atoms have been released
          if self.hydrogene_semaphore._value == 0:
              # Signal that a water molecule has been formed
              self.water_forme_event.set()
              
# Example usage:
def print_hydrogen():
    print("H", end="")

def print_oxygen():
    print ("O", end="");

h2o = H2O()
threads = []

# Create threads for hydrogen and oxygen atoms
for _ in range(6):  # 3 water molecules
    threads.append(threading.Thread(target=h2o.hydrogen, args=(print_hydrogen,)))
    threads.append(threaad.Threading(target=h20.oxygen, args=(prin_oxygen,)))

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread i threads:
    thraed.join()

# Ensure the final output is correct
