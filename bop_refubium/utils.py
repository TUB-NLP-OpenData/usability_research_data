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
from urllib.parse import urlparse
from os.path import splitext
from googletrans import Translator


HOSTS=["https://refubium.fu-berlin.de/"]
translator = Translator()

def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return str(ext).lower()  # or ext[1:] if you don't want the leading '.'

class Dataset():
    def __init__(self):
        self.title = None
        self.author = None
        self.id = None
        self.url = None
        self.abstract = None
        self.content=None

    def download(self,path):
        s=requests.get(self.url).content
        self.content=pd.read_csv(io.StringIO(s.decode('utf-8')))
        print ("Datas Successfully Saved!")

    def preview(self):
        extension=get_ext(self.url)
        get_page = urllib.request.urlopen(self.url)
        if extension==".csv":
            return pd.read_csv(get_page, nrows=5).head()
        elif extension==".json":
            return pd.read_json(get_page, nrows=5).head()
        else:
            raise Exception("Sorry, filetype not suported") 

    def df(self):
        return self.content
    
    def describe(self):
        if not self.content:
            self.download("/home/lord_tristan/Desktop")
        return ProfileReport(self.content, title='Pandas Profiling Report', explorative=True)


class Element():
    def __init__(self):
        self.title = None
        self.author = None
        self.id = None
        self.url = None
        self.year = None
        self.language = None
        self.abstract = None
        self.server = "refubium.fu-berlin.de"
        self.files=[]

    def to_dict(self,language=None):
        title=self.title
        year=self.year
        if language:
            try:
                title=translator.translate(self.title, dest=str(language).lower()).text
            except:
                pass

        ##parsing the data
        if "-" in self.year:
            year = self.year.split("-")[0]

        
        return {"id":self.id,
        "title":title,
        "author":self.author,
        "year":year,
        "language":self.language,
        "files":self.summ_datasets(),
        "url":self.url,
        "server":self.server}

    def datasets(self):
        return self.files

    def summ_datasets(self):
        out=""
        ext={}
        for f in self.files:
            fname=f.url.split("/")[-1]
            extension=str(fname.split("?")[-2])
            extensionType = str(extension.split(".")[-1]).upper()
            if extensionType not in ext.keys():
                ext[extensionType]=0
            ext[extensionType]+=1
        
        for k,v in ext.items():
            out+= str(v)+ " " +str(k)+"s, "
        return out
            
    def __str__(self):
        return str(self.title) + " - "+ str(len(self.files)) + " files"


def repository(handle_id):
    handle_id="/handle/"+handle_id.replace("/handle/","")
    url=HOSTS[-1] + handle_id
    e=Element()
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml')
    
    #atributes
    e.id= handle_id.replace("/handle/","")
    e.url = url
    e.author = soup.find("meta", {"name":"DC.creator"})["content"] if soup.find("meta",  {"name":"DC.creator"}) else None
    e.year = soup.find("meta", {"name":"DCTERMS.issued"})["content"] if soup.find("meta",  {"name":"DCTERMS.issued"}) else None
    e.title= soup.find('meta', attrs={"name":"DC.title"})["content"] if soup.find('meta', attrs={"name":"DC.title"}) else None
    e.language= soup.find('meta', attrs={"name":"DC.language"})["content"] if soup.find('meta', attrs={"name":"DC.language"}) else None
    e.abstract= soup.find('meta', attrs={"name":"DCTERMS.abstract"})["content"].encode('utf-8') if soup.find('meta', attrs={"name":"DCTERMS.abstract"}) else None
    
    #files
    for div in soup.find_all('div', attrs={"class": "btn-group"}):
        files= div.find_all(class_="btn-default", href=True)
        for f in files:
            dataset= Dataset()
            dataset.url=HOSTS[-1]+f["href"]
            if dataset.url not in [d.url for d in e.files]:
                e.files.append(dataset)
    return e

def search(keyword, format=None, translate_to=None, max_e=5):
    elements = []
    query_string= HOSTS[-1] +"discover?scope=%2F&&rpp=5&sort_by=score&order=desc&query=" + urllib.parse.quote(keyword)
    if format:
        query_string+="&filtertype_1=original_bundle_descriptions&filter_relational_operator_1=contains&filter_1"+urllib.parse.quote(format)
    while query_string and len(elements) < max_e-1:
        soup = BeautifulSoup(urllib.request.urlopen(query_string).read(), 'lxml')
        #visiting elements
        if soup.find('div', attrs={"class":"list-group"}):
            for x in soup.find('div', attrs={"class":"list-group"}).find_all(class_="list-group-item"):
                e_url=x.find('a',href=True)
                if e_url:
                    elements.append(repository(e_url["href"]))
        
            ##pagination
            if soup.find('ul', attrs={"class": "pagination"}).find_all('li')[-1].find("a"):
                query_string = HOSTS[-1] + soup.find('ul', attrs={"class": "pagination"}).find_all('li')[-1].find("a")["href"]
            else:
                query_string = ""
        else:
                query_string = ""
    
    results=[x.to_dict(language=translate_to) for x in elements]
    if results:

        return pd.DataFrame(results)[["id","server","language","title","author","year","files"]].sort_values(by='year',ascending=False,)
    else:
        return pd.DataFrame()


