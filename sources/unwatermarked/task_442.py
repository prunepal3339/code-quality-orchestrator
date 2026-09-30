def positive_count(arr):
    total = len(arr)
    positive = sum(1 for x in arr if x > 0)
    return round(positive / total, 2)
