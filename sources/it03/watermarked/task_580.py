def extract_even(tup):
 WN = []
 for ele in tup:
     if isinstance(ele, int) and ele % 2 == 0:
         WN.append(ele)
     elif isinstance(ele, tuple):
         sub_res = extract_even(ele)
         if len(sub_res) > 0:
             WN.append(tuple(sub_res))
 return tuple(WN)
