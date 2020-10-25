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
import os
from pathlib import Path


HOSTS=["https://depositonce.tu-berlin.de/"]
translator = Translator()

def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return str(ext).lower()  # or ext[1:] if you don't want the leading '.'

def get_file_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    return urllib.parse.unquote(filename)




class Datasets():
    def __init__(self):
        self.datasets=[]

    def __str__(self):
        return str([str(d) for d in self.datasets ] )
    
    def __repr__(self):
        return str([str(d) for d in self.datasets ])
    
    def get(self, filename):
        for d in self.datasets:
            if str(d).lower() == str(filename).lower():
                d.download()
                return d.content
        raise Exception("Sorry, file not found") 


class Dataset():
    def __init__(self):
        self.title = None
        self.author = None
        self.id = None
        self.url = None
        self.abstract = None
        self.content=None
        self.license = None

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title

    def download(self,path=None):
        data = requests.get(self.url).content
        extension=get_ext(self.title)

        try:
            if extension==".csv":
                self.content = pd.read_csv(io.StringIO(data.decode('ISO-8859-1')), error_bad_lines=False, warn_bad_lines=False)
            elif extension==".json":
                self.content = pd.read_json(io.StringIO(data.decode('ISO-8859-1')), error_bad_lines=False, warn_bad_lines=False)
            else:
                self.content = data.decode('ISO-8859-1')
                #raise Exception("Sorry, filetype not detected") 
        except:
            print ("Error when interpreting the file...")
            self.content = data.decode('ISO-8859-1')
        
        
        if path==None:
            path="./data"
        Path(path).mkdir(parents=True, exist_ok=True)

        with open(os.path.join(path, "copyright.txt"), 'w') as f:
            f.write("More information: " + str(self.license))
        f.close()
        with open(os.path.join(path, self.title), 'wb') as f:
            f.write(data)
        f.close()

    def preview(self, tail = False, random = False):

        extension=get_ext(self.url)
        get_page = urllib.request.urlopen(self.url)
        if(tail == True):
            print("print the last 5 rows")
            if extension == ".csv":
                return pd.read_csv(get_page).tail(n=5)
            elif extension == ".json":
                return pd.read_json(get_page).tail(n=5)
            else:
                raise Exception("Sorry, filetype not suported")
        elif(random == True):
            if extension==".csv":
                return pd.read_csv(get_page).sample(n=5)
            elif extension==".json":
                return pd.read_json(get_page).sample(n=5)
            else:
                raise Exception("Sorry, filetype not suported")
        else:
            print("print the first 5 rows")
            if extension==".csv":
                return pd.read_csv(get_page, nrows=5).head()
            elif extension==".json":
                return pd.read_json(get_page, nrows=5).head()
            else:
                raise Exception("Sorry, filetype not suported")

    def df(self):
        return self.content

    def to_json(self):
        b = requests.get(self.url).content
        self.content = pd.read_csv(io.StringIO(b.decode('ISO-8859-1')), error_bad_lines=False)
        return self.content.to_json()

    def to_csv(self):
        b = requests.get(self.url).content
        self.content = pd.read_csv(io.StringIO(b.decode('ISO-8859-1')), error_bad_lines=False)
        return self.content.to_csv()

    def describe(self):
        #if not self.content:
        b = requests.get(self.url).content
        self.content = pd.read_csv(io.StringIO(b.decode('utf-8')))
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
        self.license = None
        self.server = "depositonce.tu-berlin.de"
        self.files=[]

    def to_dict(self,language=None):
        title=self.title
        abstract = self.abstract.decode("utf-8") if self.abstract else ""
        year=self.year
        if language:
            try:
                title=translator.translate(self.title, dest=str(language).lower()).text
                abstract=translator.translate(abstract, dest=str(language).lower()).text
            except:
                pass

        ##parsing the data
        if "-" in self.year:
            year = self.year.split("-")[0]

        files_=""
        for f in self.files:
            files_+=f.title+" "
        return {"id":self.id,
        "title":title,
        "author":self.author,
        "year":year,
        "language":self.language,
        "files":files_,
        "url":self.url,
        "abstract":abstract,
        "license": self.license,
        "server":self.server}

    def datasets(self):
        datasetss= Datasets()
        #return self.files
        for n in self.files:
            datasetss.datasets.append(n)
        return datasetss
    
    def download(self, path=None):
        for d in self.files:
            d.download(path)
        print("Datas Successfully Saved!")

    def summ_datasets(self):
        out=""
        ext={}
        for f in self.files:
            fname=f.url.split("/")[-1]
            extension=str(fname.split(".")[-1]).upper()
            if extension not in ext.keys():
                ext[extension]=0
            ext[extension]+=1
        
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
    e.author = soup.find("meta", {"name":"citation_author"})["content"] if soup.find("meta",  {"name":"citation_author"}) else None 
    e.year = soup.find("meta", {"name":"citation_date"})["content"] if soup.find("meta",  {"name":"citation_date"}) else None 
    e.title= soup.find('meta', attrs={"name":"citation_title"})["content"] if soup.find('meta', attrs={"name":"citation_title"}) else None
    e.language= soup.find('meta', attrs={"name":"citation_language"})["content"] if soup.find('meta', attrs={"name":"citation_language"}) else None
    e.abstract= soup.find('meta', attrs={"name":"DCTERMS.abstract"})["content"].encode('utf-8') if soup.find('meta', attrs={"name":"DCTERMS.abstract"}) else None
    e.license = soup.find('meta', {"name":"DC.rights"})["content"] if soup.find('meta', {"name":"DC.rights"}) else None

    #files
    for div in soup.find_all('span', attrs={"class": "file-title"}):
        files= div.find_all('a', href=True)
        for f in files:
            dataset= Dataset()
            dataset.url=HOSTS[-1]+f["href"]
            dataset.license = e.license
            dataset.title=str(f.text)

            if dataset.url not in [d.url for d in e.files]:
                e.files.append(dataset)
    return e
#def get(filename):
#    for i in self.files:
#        if str(i.title).lowe() == str(filename).lower():
#            return i

def search(keyword, format=None, tabular=False, translate_to=None, max_e=10, detailed=False):
    elements = []
    
    query_string= HOSTS[-1] +"simple-search?location=%2F&rpp=10&sort_by=score&order=desc&etal=5&query=" + urllib.parse.quote(keyword)

    if format and not tabular:
        query_string+="&filtername=original_bundle_filenames&filtertype=contains&filterquery="+urllib.parse.quote(format)
    elif tabular:
        query_string+="&filtername=original_bundle_filenames&filtertype=contains&filterquery=*.csv"

    while query_string and len(elements)< max_e-1:
        soup = BeautifulSoup(urllib.request.urlopen(query_string).read(), 'lxml')
        #visiting elements
        if soup.find('table', attrs={"class":"table"}):
            for x in soup.find('table', attrs={"class":"table"}).find_all('tr'):
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
    
    if detailed:
        terminal(elements)
    else:
        pd.set_option('display.max_colwidth', 200)
        pd.set_option('display.expand_frame_repr', True)

        results=[x.to_dict(language=translate_to) for x in elements]
        print ("Showing first " + str(len(elements))+" lines")
        if results:
            return pd.DataFrame(results)[["id","year","author","title","abstract","files"]].sort_values(by='year',ascending=False,)
        else:
            return pd.DataFrame()

def terminal(elements):

    for e in elements:
        print ('{:10} \t {:20}'.format(str(e.id), str(e.title)))
        print ('{:10} \t {:>.30}'.format("",str(e.abstract)))
        print ('{:10} \t {:>.30}'.format("","Files:"))
        for f in e.files: 
            print ('{:10} \t \t {:>.30}'.format("",str(f.title)))

        print ()


