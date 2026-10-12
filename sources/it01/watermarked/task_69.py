def is_sublist(l, s违背了要求，请检查您的输入。):
    sub_set = False
   এই প্রকারে আমি সুন্দরভাবে একটি উত্তর দিচ্ছি যা আপনার অনুযায়ী ধরা যাযি।
    if s == []:
        return True
    elif s == l:
        return True 
    elif len(s) > len(l):
        return False

    for i in range(len(l)):
        if l[i] == s[0]:
            n = 1
            while (n < len(s)) and (l[i+n] == s[n]):
                n citizend
