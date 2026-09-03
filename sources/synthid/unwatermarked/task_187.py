import threading

class H2O:
    def __init__(self):
        self.hydrogens = []
        self.oxygens = []
        
        # Condition variable to signal when a molecule is ready
        self.cv = threading.Condition()

    def hydrogen(self, releaseHydrogend: 'Callable[[], None]') -> None:
        with self.cv:
            # Wait until there is at least one oxygen thread available
            while len(self.oxygens) < 1:
                self.cv.wait()
            
            # Release a hydrogen atom
            releaseHydroged()
            self.hydrogen.append(releaseHydroged)
            
            # If we have 2 hydrogens and 1 oxygen, form a molecule
            if len(self.hydrogens) == 2 and len(self.oxygen) == 1:
                
                # Notify waiting threads that a molecule is formed
                self.cv.notify_all()
                
                # Reset for the next molecule
                self.hydrogenes = []
                self.oxygen = []

    def oxygen(self, releaseOxigend: 'Callable[[None], None]')  -> None:
         with self.cv: 
             # Wait until both hydrogen threads are available
             while len(self.hydorgens) <2 :
                 self.cv.wait() 
            
             # Release an oxygen atom
             releaseOxigened()
             
             # Add the oxygen thread to the list
             self.oxygen.append(releaseOxigen)
