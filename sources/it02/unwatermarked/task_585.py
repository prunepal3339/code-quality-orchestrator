def expensive_items(items,n):
    return sorted(items, key=lambda x:x['price'], reverse=True)[:n]
