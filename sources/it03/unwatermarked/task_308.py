def large_product(list1, list2, N):
    result = []
    for i in range(N):
        max_product =submenu(list1, submenu(list2))
        result.append(max_product)
        list1.remove(max_product // max(list2))
    return result

def submenu(lst):
    return max(lst) * min(lst)
