# -*- coding: utf-8 -*-
import scrapy
import sys,os,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名称
    name = 'douban_spider'
    #允许的域名
    allowed_domains = ['movie.douban.com']
    #url入口，扔到调度器
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # from scrapy.http.response.html import HtmlResponse
        # print(response,type(response))
        # print(response.text)
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = item.xpath(".//div[@class='item']//em//text()").extract_first()
            douban_item['movie_name'] = item.xpath(".//div[@class='hd']/a/span[1]/text()").extract_first()
            content = item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = " ".join(i_content.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['comments'] = item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describe'] = item.xpath(".//div[@class='bd']/p[1]/text()").extract_first()
            yield douban_item

        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)

