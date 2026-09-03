from collections import Counter

def find_odd(arr):
    counts = Counter(arr)
    for num, count in counts.items():
        if count % 2 != 0:
            return num
