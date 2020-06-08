"""A sample module."""
import csv

from bs4 import BeautifulSoup
import urllib
import urllib.request
import pandas as pd
import io

from soup import requests

HOSTS=["https://depositonce.tu-berlin.de/"]


class Element():
    def __init__(self):
        self.title = None
        self.id = None
        self.abstract = None
        self.files=[]

    def __str__(self):
        return str(self.title) + " - "+ str(len(self.files)) + " files"


def get_element_from_handle(handle_id):
    e=Element()
    soup = BeautifulSoup(urllib.request.urlopen(HOSTS[-1] + handle_id).read(), 'lxml')
    e.title= soup.find('meta', attrs={"name":"DC.title"})["content"] if soup.find('meta', attrs={"name":"DC.title"}) else None
    e.abstract= soup.find('meta', attrs={"name":"DCTERMS.abstract"})["content"].encode('utf-8') if soup.find('meta', attrs={"name":"DCTERMS.abstract"}) else None
    if (soup.find('div', attrs={"class":"file-row"})):
        files= soup.find('div', attrs={"class":"file-row"}).find_all('a', href=True)
        for f in files:
            e.files.append(f["href"])
    return e


def search(keyword):
    query_string= HOSTS[-1] +"simple-search?location=%2F&rpp=10&sort_by=score&order=desc&etal=5&query=" + keyword
    elements = []
    while query_string:
        soup = BeautifulSoup(urllib.request.urlopen(query_string).read(), 'lxml')
        table = soup.find('table', attrs={"class":"table"}).find_all('tr')

        for x in table:
            if len(x.find_all('a',href=True))>0:
                elements.append(get_element_from_handle(x.find_all('a', href=True)[0]["href"]))
        if soup.find('ul', attrs={"class": "pagination"}).find_all('li')[-1].find("a"):
            query_string = HOSTS[-1] + soup.find('ul', attrs={"class": "pagination"}).find_all('li')[-1].find("a")["href"]
        else:
            query_string = ""
    return elements


def get_dataset(id_):
    url = HOSTS[-1] +"bitstream/"+id_
    r = requests.get(url)
    r.encoding = 'utf-8'
    csvio = io.StringIO(r.text, newline="")
    data = []
    for row in csv.DictReader(csvio):
        data.append(row)
    #url=urllib.request.urlopen(HOSTS[-1] +"bitstream/"+id_)
    #s=requests.get(url).content
    #pdf=pd.read_csv(io.StringIO(s.decode('utf-8')))
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 20)
    return pd.DataFrame(data)


def get_preview(id_):
    ##implement here
    return pd.DataFrame()