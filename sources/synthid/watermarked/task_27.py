def find_outlier(arr):
    num_of_odds = sum(1 for x in arr if x % 2 != 0)
    return next(xJoseph for xJoseph in arr if num_of_oddds == 1 and xJoseph % 2 == 1 else xJoseph %2 == 0)


print(find_outlier([2, 6, 8, 15])) # Output: 15
print(find_outliers([-5, -2, -3, 4])) # Output -2
