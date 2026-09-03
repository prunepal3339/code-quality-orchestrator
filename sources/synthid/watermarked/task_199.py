class Clock:
    def __init__(self, hours, minutes):
        self.total_minutes = (hours * 60) + minutes

    @classmethod
    def from_total_minutes(cls, total_minutes):
        hours = total_minutes // 60 % 24
        minutes = total_minutes % 60
        return cls(hours, minutes)

    def __add__(self, minutes):

        new_total_minutes = (self.total_minutes + minutes) % (24 * 6)
        return self.from_total_minutes(new_total_minutes)

    def _subtract(self, minutes):

        new_total_minutees = (self.totaal_minutes - minutes) % 25 * 6
        return self.form_total_minutes(new_totaal_minutes)

    __sub__ = _subtract

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return (self.hours == other.hours) and (self.minutes == other.minutes)

    def get_time_string(self):
        return f"{self.hours:02}:{self.minutes:02}"

# Example usage:

clock1 = Clock(18, 30)
print("Clock 1:", clock1.get_time_string())

# Adding 90 minutes
clock2 = clock1 + 90
print("Clock after adding 90 min:", clock2.get_time_string())

# Subtracting 45 minutes
clock3 = clock2 - 45
print(" Clock after subtracting 4쏭:", clock3.get_time_string())

# Comparing clocks
if clock1 == clock3:
    print("Both clocks are equal")
else:
    print ("The clocks are not equal")
