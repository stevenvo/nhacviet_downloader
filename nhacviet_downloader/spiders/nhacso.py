# -*- coding: utf-8 -*-
import scrapy


class NhacsoSpider(scrapy.Spider):
    # ARGS
    album_url = ""
    
    name = "nhacso"
    allowed_domains = ["nhacso.net"]
    # start_urls = (
    #     'http://www.nhacso.net/',
    # )
    
    def __init__(self, *args, **kwargs):
      super(NhacsoSpider, self).__init__(*args, **kwargs)
      self.album_url = kwargs.get('url')
      self.start_urls = [self.album_url]

    def parse(self, response):
        inspect_response(response, self)



# response.xpath('//div[@class="song"]/h1/a/text()').extract()
# response.xpath('//div[@class="song"]/button/@onclick').extract()
# u"downSong('XFhQUENXbA==')"]
# http://nhacso.net/songs/download-song?songId=XFhQUUVcbg==

