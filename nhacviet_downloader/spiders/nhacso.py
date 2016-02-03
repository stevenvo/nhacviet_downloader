# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy.shell import inspect_response
from nhacviet_downloader.items import NhacsoNetItem



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


    # print song_titles
    # print song_download_urls
    # inspect_response(response, self)

    # response.xpath('//div[@class="song"]/h1/a/text()').extract()
    # response.xpath('//div[@class="song"]/button/@onclick').extract()
    # u"downSong('XFhQUENXbA==')"]
    # http://nhacso.net/songs/download-song?songId=XFhQUUVcbg==

    def parse(self, response):
        # songs = []
        p = re.compile(ur'downSong\(\'(.*?)\'\)')
        for title, partial_url in zip(response.xpath('//div[@class="song"]/h1/a/text()').extract(), response.xpath('//div[@class="song"]/button/@onclick').extract()):
            song = NhacsoNetItem()
            song["title"] = title
            search = re.search(p, partial_url)
            song["file_url"] = "http://nhacso.net/songs/download-song?songId={}".format(search.group(1))
            song["referer_url"] = response.url
            yield song
            
        # p = re.compile(ur'downSong\(\'(.*?)\'\)')
        # urls = []
        # for partial_url in response.xpath('//div[@class="song"]/button/@onclick').extract():
        #     search = re.search(p, partial_url)
        #     url = "http://nhacso.net/songs/download-song?songId={}".format(search.group(1))
        #     urls.append(url)
        #
        # songs = NhacsoNetItem()
        # songs["file_urls"] = urls
        # return songs
    

