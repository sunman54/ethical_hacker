import requests


def make_request(url):
    try:
        return requests.get('http://' + url)

    except requests.exceptions.ConnectionError:
        pass


target_url = 'google.com'

with open('./data/files-and-dirs-wordlist.txt', 'r') as file:
    for line in file:
        word = line.strip()

        test_url = target_url + '/' + word
        response = make_request(test_url)

        if response:
            print(f'[+] URL discovered : {test_url}')