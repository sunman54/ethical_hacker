import requests


def make_request(url):
    try:
        return requests.get('http://' + url)

    except requests.exceptions.ConnectionError:
        pass


target_url = 'google.com'

with open('./data/subdomains-wodlist.txt', 'r') as file:
    for line in file:
        word = line.strip()

        test_url = word + '.' + target_url
        response = make_request(test_url)

        if response:
            print(f'[+] Subdomain discovered : {test_url}')