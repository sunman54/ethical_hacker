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

href_links = extract_links_from(target_url)

for link in href_links:
    link = urljoin(target_url, link)

    if target_url in link: #for avoiding other websites
        print(link)
