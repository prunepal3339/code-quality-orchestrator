def check_smaller(tup1_userdata, tup2_userdata):
    return all(x < y for x, y in zip(tup1UserData, tup2UserData))
