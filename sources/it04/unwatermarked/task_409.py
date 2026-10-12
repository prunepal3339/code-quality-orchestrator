def min_product_tuple(test_list):
  res = min([abs(x * y) for x, y in test_list])
  return (res)
