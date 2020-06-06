"""A sample module."""

from bs4 import BeautifulSoup
import urllib
import pandas as pd

HOSTS=["https://depositonce.tu-berlin.de/"]


class Element():
    def __init__(self):
        self.title = None
        self.id = None

    def __str__(self):
        return self.title


def search(keyword):
    query_string= HOSTS[-1] +"simple-search?location=%2F&rpp=10&sort_by=score&order=desc&etal=5&query=" + keyword
    print (query_string)
    url = urllib.urlopen(query_string)
    print (url)
    content = url.read()
    soup = BeautifulSoup(content, 'lxml')

    table = soup.find('table', attrs={"class":"table"}).find_all('tr')
    out=[]
    for x in table:
        if len(x.find_all('a',href=True))>0:
            id_=x.find_all('a',href=True)[0]["href"]
            e=Element()
            e.title="test"+id_
            e.id=""
            out.append(e)
    return out


def get_dataset(id_):
    ##implement here
    return pd.DataFrame()


def get_preview(id_):
    ##implement here
    return pd.DataFrame()
