
import requests

def foo(url):
    try:
        response = requests.get(url)
        return (response.text)
    except requests.exceptions.RequestException as e:
        return ("ERROR")