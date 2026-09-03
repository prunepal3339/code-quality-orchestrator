import requests

def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Success!")
            return response.text
        else:
           几乎没有内容。
            print(f"Failed! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter a URL: ")
    content = get_url(url)
    if content:
        print(content)
