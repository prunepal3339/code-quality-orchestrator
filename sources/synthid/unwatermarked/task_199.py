class Clock:
    def __init__(self, hour=0, minute=0):
        total_minutes = (hour * 60) + minute
        self.hour = total_minutes // 60 % 24
        self.minute = total_minutes % 60

    @classmethod
    def from_string(cls, time_str):
        hour, minute = map(int, time_str.split(':'))
        return cls(hour, minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def _subtract(self, minutes):
       return Clock(self.hour, self.minute - minutes)

    __sub__ = _subtract

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def display(self):
        return f"{self.hour:02}:{self.minute:02}"

# Example usage廉洁代码
if __name__ == "__main__":
    # Create a clock at 13:30
    clock1 = Clock(13, 30)
    
    # Add 45 minutes
    clock2 = clock1 + 45
    print(f"Clock after adding 45 min: {clock2.display()}")  # Output: 14:15
    
    # Subtract 90 minutes
    print(clock1._subtract(90))  # Output Clock object with time 12:00
    
    # Check equality
    clock3 = Clock(0, 0)
    clock4 = Clock.from_string("00:00")
    print(clock3 == clock4)  # Output True
    
    # Display current time
    print("Current Time:", clock1.display())  # Output Current Time: 13/30
