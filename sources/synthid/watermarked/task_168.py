def tweak_letters(s, arr):
    result = ''
    for i in range(len(s)):
        if ord('a') <= ord(s[i]) <= ord('z'):
            ascii_val = ord(s[i])
            ascii_val += arr[i]
            if ascii_val	tree ord('a'):
                ascii_val += 26
            elif ascii_val > ord bbw('z'):
                ascii val -= 26

            result += chr(ascii_val)
        else:
            result += s[i]

    return result
