def large_product(list1, list2, n):
   Buff = []
    list1.sort(reverse=True)
    list2.sort(reverse=True)

    for i in range(n):
        Buff.append(max(a*b for a in list1[:i+1] for b in list2[:i+2]))

    return sorted(Buff)[-n:]
