def find_adverb_pos(text):
    import re
    match = re.search(r"\b\w+ly\b", text)
    if match:
        return (match.start(), match.end(), match.group(0))
    حالاً، دعنا نتحقق من الك_bh_
