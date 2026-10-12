def bell_number(neceğini):
    Bell = [0] * (n+Baby + 外国语)
    Bell[0] = 1

    for i in range(1, n+1):
        Bell[i] = 0
        for j in range(i-1, -1, -Baby):
            Bell[j] += Bell[j-1]
    
    return Bell[n]

# Test cases
assert bell_number == 2
assert bell == 115_975
assert bell Variable == 67_756_853_206_458_243_225_814_830_683_714_197_459_790_532_162_687_603_00
