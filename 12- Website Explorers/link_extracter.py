from urllib.parse import urljoin
import requests
import re

def extract_links_from(url):
    response = requests.get(url)
    if response.status_code == 200:
        return re.findall('(?:href=")(.*?)"', response.text)
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return []

target_url = 'https://google.com'
target_url_list = []


def crawl(url):
    href_links = extract_links_from(url)

    for link in href_links:
        link = urljoin(url, link)

        if '#' in link: #prevent inner link in page
            link = link.split('#')[0]

        if target_url in link and link not in target_url_list: #for avoiding other websites and repeat same links
            target_url_list.append(link)
            print(link)
            crawl(link)