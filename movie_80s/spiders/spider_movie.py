# -*- coding: utf-8 -*-
import scrapy
from movie_80s.items import Movie80SItem
from copy import deepcopy
import re


class SpiderMovieSpider(scrapy.Spider):
    name = 'spider_movie'
    allowed_domains = ['www.80s.tw/movie/list']
    start_urls = ['https://www.80s.tw/movie/list']
    i = 0
    p = 1

    def parse(self, response):
        """
        处理电影列表
        获取电影名
        获取电影封面
        获取电影内容页url
        """
        item = Movie80SItem()
        li_list = response.xpath('//*[@id="block3"]/div[3]/ul[2]/li')
        for li in li_list:
            item['name'] = li.xpath('.//@title').extract_first().split()[0]               # 电影名
            item['img'] = li.xpath('.//a//@src').extract_first()                          # 电影封面
            item['url'] = 'https://www.80s.tw/' + li.xpath('.//a/@href').extract_first()  # 电影内容页
            yield scrapy.Request(item['url'], callback=self.parse_content, meta={'item': deepcopy(item)}, dont_filter=True)
        # 翻页
        # 当前页
        current_page = int(response.xpath('//div[@class="pager"]/strong/text()').extract_first())
        # 总页数
        total_page = int(re.search('下一页</a><a href="/movie/list/-----p/(\d*)">尾页', response.body.decode('utf-8')).group(1))
        # 下一页url
        next_page = f'https://www.80s.tw/movie/list/-----p/{current_page + 1}'
        # 当前页与总页数比较
        if total_page and current_page < (total_page - 4):
            yield scrapy.Request(next_page, callback=self.parse, meta={'item': deepcopy(item)}, dont_filter=True)
        elif not total_page and p < 5:
            self.p += 1
            yield scrapy.Request(next_page, callback=self.parse, meta={'item': deepcopy(item)}, dont_filter=True)

    def parse_content(self, response):
        """
        处理电影内容页
        获取电影简介
        获取下载链接
        """
        item = response.meta['item']  # 接收item
        item['desc'] = response.xpath('//div[@id="movie_content"]/text()').extract()[1]\
            .replace(' ', '').replace("\u3000", "").replace('\n', '')
        item['link'] = response.xpath('//span[@class="xunlei dlbutton1"]/a/@href').extract_first()
        self.i += 1
        print(self.i)
        yield item













