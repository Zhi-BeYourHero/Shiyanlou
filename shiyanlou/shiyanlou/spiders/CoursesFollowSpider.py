# -*- coding: utf-8 -*-
import scrapy


class CoursesfollowspiderSpider(scrapy.Spider):
    name = 'CoursesFollowSpider'
    start_urls = ['http://shiyanlou.com/courses/63/']
    
    def start_request(self):
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href').extract():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'name':response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author':response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        
        }
        
