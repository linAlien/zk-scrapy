# -*- coding: utf-8 -*-
import datetime
import json

import scrapy

from my_zakerSpider.items import HotNewsItem, AmusementNewsItem, CarNewsItem, SportsNewsItem, ScienceNewsItem, \
    InlandNewsItem
from my_zakerSpider.tool import Timestamp

cookies = dict(
    HMTIME=1547018965.887,
    UM_distinctid='167884f1313115-0c6b51428fbc2a-b79193d-100200-167884f13148d',
    Hm_lvt_cc7727963122f971608bd86205279c54=1547017442,
    CNZZDATA1255379515='1324205989-1544175654-http%253A%252F%252Fwww.myzaker.com%252F%7C1547190908',
    auto='true'
)


class ExampleSpider(scrapy.Spider):

    name = 'example'
    allowed_domains = ['myzaker.com','iphone.myzaker.com']
    # 热点新闻api接口
    start_urls = ['http://www.myzaker.com/channel/10']

    @staticmethod
    def NewsData(item,data):

        '''
        :param item: 对应新闻表的Item
        :param data: 新闻数据
        :return: 返回新闻数据列表
        '''
        articles = data['article']
        article_data_list = []
        if articles != []:
            for article in articles:
                News = item()
                News['href'] = str(article['href'])
                News['typeMark'] = str(article['typeMark'])
                News['mark'] = str(article['marks'])
                News['title'] = str(article['title'])
                News['img'] = str(article['img'])
                News['crawltime'] = datetime.datetime.now().strftime("%Y-%m-%d %X")
                article_data_list.append(News)
        return article_data_list


    def parse(self, response):
        # '娱乐新闻': self.AmusementParse,
        # '汽车新闻': self.CarParse,
        # '体育新闻': self.SportsParse,
        # '科技新闻': self.SciencePaese,
        # '国内新闻': self.Inlandparse
        parse_dict = {
            '热点新闻': self.HotParse ,
            '娱乐新闻': self.AmusementParse,
            '汽车新闻': self.CarParse,
            '体育新闻': self.SportsParse,
            '科技新闻': self.SciencePaese,
            '国内新闻': self.Inlandparse
        }

        news_urls_dict = {}
        news_urls = response.xpath("//div[contains(@class,'nav')]/a/@href").extract()
        news_titles = response.xpath("//div[contains(@class,'nav')]/a/@title").extract()
        for title in news_titles:
            news_urls_dict[title] = 'http:'+news_urls[news_titles.index(title)]

        for title,newsparse in parse_dict.items():
            yield response.follow(news_urls_dict[title],newsparse,cookies=cookies)


    def HotParse(self,response):
        '''
        热点新闻解析
        :param response:
        :return:
        '''
        try:
            next_url ='http:'+ response.xpath("//input[@id='nexturl']/@value").extract_first()
        except TypeError:
            next_url=''

        if next_url=='':

            result = json.loads(response.body)
            data = result['data']

            next_url = data.get('next_url', '')
            if next_url != '':
                next_url = 'http:' + next_url
                newsdatas = self.NewsData(HotNewsItem, data)
                for newsdata in newsdatas:
                    yield newsdata
                cookies['HMTIME'], cookies['Hm_lvt_cc7727963122f971608bd86205279c54'] = Timestamp()
        yield response.follow(next_url, self.HotParse, cookies=cookies)



    def AmusementParse(self,response):
        '''解析娱乐新闻'''
        try:
            next_url = 'http:' + response.xpath("//input[@id='nexturl']/@value").extract_first()
        except TypeError:
            next_url = ''

        if next_url == '':

            result = json.loads(response.body)
            data = result['data']

            next_url = data.get('next_url', '')
            if next_url != '':
                next_url = 'http:' + next_url
                newsdatas = self.NewsData(AmusementNewsItem, data)
                for newsdata in newsdatas:
                    yield newsdata
                cookies['HMTIME'], cookies['Hm_lvt_cc7727963122f971608bd86205279c54'] = Timestamp()

        yield response.follow(next_url, self.AmusementParse, cookies=cookies)


    def CarParse(self,response):
        '''解析汽车新闻'''
        try:
            next_url = 'http:' + response.xpath("//input[@id='nexturl']/@value").extract_first()
        except TypeError:
            next_url = ''

        if next_url == '':

            result = json.loads(response.body)
            data = result['data']

            next_url = data.get('next_url', '')
            if next_url != '':
                next_url = 'http:' + next_url
                newsdatas = self.NewsData(CarNewsItem, data)
                for newsdata in newsdatas:
                    yield newsdata
                cookies['HMTIME'], cookies['Hm_lvt_cc7727963122f971608bd86205279c54'] = Timestamp()
        print(next_url)
        yield response.follow(next_url, self.CarParse, cookies=cookies)

    def SportsParse(self,response):
        '''解析体育新闻'''
        try:
            next_url = 'http:' + response.xpath("//input[@id='nexturl']/@value").extract_first()
        except TypeError:
            next_url = ''

        if next_url == '':

            result = json.loads(response.body)
            data = result['data']

            next_url = data.get('next_url', '')
            if next_url != '':
                next_url = 'http:' + next_url
                newsdatas = self.NewsData(SportsNewsItem, data)
                for newsdata in newsdatas:
                    yield newsdata
                cookies['HMTIME'], cookies['Hm_lvt_cc7727963122f971608bd86205279c54'] = Timestamp()
        print(next_url)
        yield response.follow(next_url, self.SportsParse, cookies=cookies)


    def SciencePaese(self,response):
        '''解析科技新闻'''
        try:
            next_url = 'http:' + response.xpath("//input[@id='nexturl']/@value").extract_first()
        except TypeError:
            next_url = ''

        if next_url == '':

            result = json.loads(response.body)
            data = result['data']

            next_url = data.get('next_url', '')

            if next_url != '':
                next_url = 'http:' + next_url
                newsdatas = self.NewsData(ScienceNewsItem, data)
                for newsdata in newsdatas:
                    yield newsdata

                cookies['HMTIME'], cookies['Hm_lvt_cc7727963122f971608bd86205279c54'] = Timestamp()
        yield response.follow(next_url, self.SciencePaese, cookies=cookies)


    def Inlandparse(self,response):
        '''解析国内新闻'''
        try:
            next_url = 'http:' + response.xpath("//input[@id='nexturl']/@value").extract_first()
        except TypeError:
            next_url = ''

        if next_url == '':

            result = json.loads(response.body)
            data = result['data']

            next_url = data.get('next_url', '')

            if next_url != '':
                next_url = 'http:' + next_url
                newsdatas = self.NewsData(InlandNewsItem, data)
                for newsdata in newsdatas:
                    yield newsdata

                cookies['HMTIME'], cookies['Hm_lvt_cc7727963122f971608bd86205279c54'] = Timestamp()
        yield response.follow(next_url, self.Inlandparse, cookies=cookies)




