def trim_tuple(test_list, K):
  res = [tuple(ele[K:] for ele in sub) for sub in test_list]
  return str(res)
