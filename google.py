import sys
import webbrowser
import requests
from bs4 import BeautifulSoup
def read_input():
    if len(sys.argv)>1:
        keywords = ' '.join(sys.argv[1:])
        return keywords

def google_search(keywords):
    link = "https://www.google.com/search?q="+keywords
    return make_request(link)

def make_request(link):
    r = requests.get(link)
    return r

def parse(res):
    soup = BeautifulSoup(res.text,'lxml')
    return soup

def open_page(links):
    for link in links:
        webbrowser.open("https://www.google.com/"+link['href'])

keywords          = read_input()
response          = google_search(keywords) 
soup              = parse(response)
high_ranked_links = soup.select('.r a')[0:3]
open_page(high_ranked_links)


