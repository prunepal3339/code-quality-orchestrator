def find_missing_letter(arr):
    return chr(ord(arr[0]) + [i for i in range(len(arr)) if arr[i] != chr(ord(arr[0]) + i)][0])
