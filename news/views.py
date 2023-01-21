from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# First, we get the news fromTimes of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13]  # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

toi_news = toi_news[2:]  # removing first two entires - they're not news headers


def index(req):
    return render(req, 'news/index.html', {'toi_news': toi_news})
