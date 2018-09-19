import requests

url = "http://www.baidusssssss.com" #url that doesnt exist


def get_data(url):
    try:
        data = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print("Error, url:", url)
        print("Error Details: ", e)
        data = None
    return data

if __name__ == '__main__':
    get_data(url)