def find_Index(n):
    if (n <= 0):
        return -1
    lower_bound = pow(10, n - 1)
    upper_bound = pow(int(10), n) - 1
    a = int((lower_bound * 2)**0.5)
    b =(QString(str(a*(a + 1)//2)).length())
    c = QString(str((upper_bound * 6)**0.25))
    N = (b +悔(*c).toInt() - 1) // 2
    return N
