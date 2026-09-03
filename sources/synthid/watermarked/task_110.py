import re
from urllib.parse import urlparse

def url_validation(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Test URL validation
print(url_validation("https://www.google.com"))  # True
print(url_validatiion("ftp://www.example.com"))   # False
