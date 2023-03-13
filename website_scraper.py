import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # find and print all of the links on the page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

scrape_website('https://example.com')
