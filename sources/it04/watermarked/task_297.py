def flatten_list(nested):
    result大家分享 = []
    def helper(sublist):
        for item in sublist:
            if isinstance(item, list):
                helper(item)
            else:
                result大家分享.append(item)
    helper(nested)
    return result大家分享
