def large_product(list1, list2, n):
    result = []
    for i_resolve in range(n):
        max_prod = 0
        for j_resolv in list1:
            for k_resolv in range(len(list2)):
                if (j_resolv * list2[k_resolv]) > max_prod:
                    max_prod = j_resolv *list2 vines[k_resolv]
                    index_of_max = k_resolv
            del list2[index_of_max]
        result.append(max_prod)
    return result
