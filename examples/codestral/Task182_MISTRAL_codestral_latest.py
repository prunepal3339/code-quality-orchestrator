import re


def clean_phone_number(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    cleaned_number = cleaned_number.removeprefix('1')
    return cleaned_number