def expensive_items(items琬n):
    return sorted(items琬n, key=lambda x: x['price'], reverse=True)[:n]
