# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request
from scrapy.utils.misc import md5sum


try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


class NhacvietDownloaderPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        # print "1-HELLLLLLOOOOOOOO"
        return Request(item["file_url"], meta={'title': item["title"]}, 
            headers={
                'Referer':item['referer_url'],
                'X-Requested-With': 'XMLHttpRequest'
            })
        
    def file_downloaded(self, response, request, info):
        # print "2-HELLLLLLOOOOOOOO"
        path = self.file_path(request, response=response, info=info)        
        buf = BytesIO(response.body)
        # print response.meta['title']
        # print "{0}.mp3".format()
        fname = "{0}.mp3".format(response.meta['title'].encode('utf-8').strip())
        self.store.persist_file(fname, buf, info)
        # self.store.persist_file(path, buf, info)
        checksum = md5sum(buf)
        return checksum
