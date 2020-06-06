import scrapy
from scrapy.http import FormRequest

import pandas as pd


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://depositonce.tu-berlin.de/'
    ]

    def __init__(self, query):
        self.query = query

    def parse(self, response):
        return FormRequest.from_response(response,
                                         formdata={'query': self.query},
                                         callback=self.search_result
                                         )

    def search_result(self, response):
        tel = response.body
        print(tel)
