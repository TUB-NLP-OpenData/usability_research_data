"""A sample module."""

from bs4 import BeautifulSoup
import urllib
import urllib.request
import pandas as pd
import io
import requests
from tqdm import tqdm
import urllib.request
from itertools import islice
from pandas_profiling import ProfileReport



HOSTS=["https://depositonce.tu-berlin.de/"]


class Element():
    def __init__(self):
        self.title = None
        self.author = None
        self.id = None
        self.url = None
        self.abstract = None
        self.files=[]

    def to_dict(self):
        return {"id":self.id,"title":self.title,"authors":self.title,"files":[f.split("/")[-1] for f in self.files],"url":self.url}

    def __str__(self):
        return str(self.title) + " - "+ str(len(self.files)) + " files"


def get_element_from_handle(handle_id):
    handle_id="/handle/"+handle_id.replace("/handle/","")
    url=HOSTS[-1] + handle_id
    #print (url)
    e=Element()
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml')
    e.id= handle_id.replace("/handle/","")
    e.url = url
    e.title= soup.find('meta', attrs={"name":"DC.title"})["content"] if soup.find('meta', attrs={"name":"DC.title"}) else None
    e.abstract= soup.find('meta', attrs={"name":"DCTERMS.abstract"})["content"].encode('utf-8') if soup.find('meta', attrs={"name":"DCTERMS.abstract"}) else None
    if (soup.find('div', attrs={"class":"file-row"})):
        for div in soup.find_all('div', attrs={"class": "file-row"}):
            files= div.find_all('a', href=True)
            for f in files:
                # print(f)
                # print(HOSTS[-1])
                # print(f["href"])
                e.files.append(HOSTS[-1]+f["href"])
    return e


def get_elements_by_keywork(keyword, max_e=10):

    query_string= HOSTS[-1] +"simple-search?location=%2F&rpp=10&sort_by=score&order=desc&etal=5&query=" + keyword
    elements = []
    while query_string:
        if len(elements)> max_e-1:
            break
        soup = BeautifulSoup(urllib.request.urlopen(query_string).read(), 'lxml')
        table = soup.find('table', attrs={"class":"table"}).find_all('tr')

        for x in table:
            if len(x.find_all('a',href=True)) > 0:
                elements.append(get_element_from_handle(x.find_all('a', href=True)[0]["href"]))
        if soup.find('ul', attrs={"class": "pagination"}).find_all('li')[-1].find("a"):
            query_string = HOSTS[-1] + soup.find('ul', attrs={"class": "pagination"}).find_all('li')[-1].find("a")["href"]
        else:
            query_string = ""
    return elements


def search(keyword, max_e=10):
    results=[x.to_dict() for x in get_elements_by_keywork(keyword, max_e=10)]
    return pd.DataFrame(results)


def get_datasets(id_,ind_=[-1]):
    out=[]
    files=[f for f in get_element_from_handle(id_).files]

    for f in tqdm(files):
        #print (f)
        try:
            s=requests.get(f).content
            pdf=pd.read_csv(io.StringIO(s.decode('utf-8')))
            out.append(pdf)
        except:
            pass
    return out


def get_preview(id_):
    #get_page = urllib.request.urlopen('https://depositonce.tu-berlin.de/bitstream/' + id_ + '/2/Xb.csv')
    #return pd.read_csv(get_page, nrows=5)
    out = []
    files = [f for f in get_element_from_handle(id_).files]
    for f in tqdm(files):
        try:
            get_page = urllib.request.urlopen(f)
            var = pd.read_csv(get_page, nrows=5)
            out.append(var)
        except:
            pass

    return out




def describe(id_):
    get_page = urllib.request.urlopen('https://depositonce.tu-berlin.de/bitstream/' + id_ + '/2/Xb.csv')
    df = pd.read_csv(get_page)
    profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
    return profile
