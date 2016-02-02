# -*- coding: utf-8 -*-
import scrapy


class NhacsoSpider(scrapy.Spider):
    name = "nhacso"
    allowed_domains = ["nhacso.net"]
    start_urls = (
        'http://www.nhacso.net/',
    )

    def parse(self, response):
        pass


# response.xpath('//div[@class="song"]/h1/a/text()').extract()
# response.xpath('//div[@class="song"]/button/@onclick').extract()
# u"downSong('XFhQUENXbA==')"]
# http://nhacso.net/songs/download-song?songId=XFhQUUVcbg==

