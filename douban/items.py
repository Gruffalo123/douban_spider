# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()#序号
    movie_name = scrapy.Field()#电影名称
    introduce = scrapy.Field()#介绍
    star = scrapy.Field()#星级
    comments = scrapy.Field()#评论数
    describe = scrapy.Field()#描述
