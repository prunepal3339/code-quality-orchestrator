import requests

def retrieve_file(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print('File downloaded successfully.')
        else:
            print(f'Failed to download file. Status code: {response.status_code}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    url = input('Enter the URL of the file you want to retrieve: ')
    filename = input('Specify the filename to save the file under: ')
    retrieve_file(url=url, filename=filename)
