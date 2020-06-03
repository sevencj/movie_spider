# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Movie80SItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影名
    name = scrapy.Field()
    # 电影简介
    desc = scrapy.Field()
    # 电影封面链接
    img = scrapy.Field()
    # 电影下载链接
    link = scrapy.Field()
    # 内容页url
    url = scrapy.Field()
