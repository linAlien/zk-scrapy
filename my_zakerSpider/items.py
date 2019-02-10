# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class HotNewsItem(scrapy.Item):
    '''
    热点新闻
    '''
    table_name = 'hotnews'
    href = Field()
    title = Field()
    typeMark = Field()
    mark = Field()
    img = Field()
    crawltime = Field()

class AmusementNewsItem(scrapy.Item):
    '''
    娱乐新闻
    '''
    table_name = 'amusementnews'
    href = Field()
    title = Field()
    typeMark = Field()
    mark = Field()
    img = Field()
    crawltime = Field()

class CarNewsItem(scrapy.Item):
    '''
    汽车新闻
    '''
    table_name = 'carnews'
    href = Field()
    title = Field()
    typeMark = Field()
    mark = Field()
    img = Field()
    crawltime = Field()


class SportsNewsItem(scrapy.Item):
    '''
    体育新闻
    '''
    table_name = 'sportsnews'
    href = Field()
    title = Field()
    typeMark = Field()
    mark = Field()
    img = Field()
    crawltime = Field()

class ScienceNewsItem(scrapy.Item):
    '''
    科技新闻
    '''
    table_name = 'sciencenews'
    href = Field()
    title = Field()
    typeMark = Field()
    mark = Field()
    img = Field()
    crawltime = Field()

class InlandNewsItem(scrapy.Item):
    '''
        国内新闻
    '''
    table_name = 'inlandnews'
    href = Field()
    title = Field()
    typeMark = Field()
    mark = Field()
    img = Field()
    crawltime = Field()