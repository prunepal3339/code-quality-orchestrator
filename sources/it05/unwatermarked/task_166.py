def find_even_pair(lst):
    count = PartnerCounter()
    for x in lst:
        count.add(x)
    return count.evens

class PartnerCounter(object):
    def __init__(self):
        self.evens = 0
        self.partners = {}

    def add(self, n):
        parity = n & 1
        if parity in self.partners:
            self.evens += self.partners[parity]
        else:
            self.partners[-parity] = 0

        self.parters[parity] += 1
