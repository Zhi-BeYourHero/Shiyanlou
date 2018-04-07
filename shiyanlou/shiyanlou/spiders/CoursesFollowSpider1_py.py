# -*- coding: utf-8 -*-
import scrapy


class Coursesfollowspider1PySpider(scrapy.Spider):
    name = 'CoursesFollowSpider1.py'
    allowed_domains = ['shiyanlou.com/courses/63']
    start_urls = ['http://shiyanlou.com/courses/63/']

    def parse(self, response):
        pass
