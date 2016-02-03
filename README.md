# Nhac Viet Crawler

[![Demo Video](http://img.youtube.com/vi/T7GCLgPfwE/0.jpg)](https://www.youtube.com/watch?v=-T7GCLgPfwE)

## Why I created this

1. I want to listen to Viet music from my phone while driving
1. Viet music website does not release iOS app to US App Store
1. To save me time downloading songs manually 
2. Practice my python and scrapy coding

## Prerequisites
You need to have these Python libraries installed beforehand:
* [Scrapy framework](http://scrapy.org/): `pip install scrapy` or `easy install scrapy`

## Usage

### Clone the repository to your machine
```
$ git clone https://github.com/stevenvo/nhacviet_downloader
$ cd nhacviet_downloader
```
### Downloader

```
scrapy crawl nhacso -a url="http://nhacso.net/nghe-playlist/tet-2016-.XFhQUEVZag==.html"
```

The mp3 files will be downloaded into folder **downloaded-mp3-files** in the current directory.

__Parameters:__
* `url`: the web URL of the music album on NhacSo.Net

## Future Enhancements

* able to download music from **mp3.zing.vn**
* able to download music from **nhaccuatui.com**

__Disclaimer: this is an open-source project for educational purposes, please use it at your own risk, I'm not responsible for any copyrights nor legal actions.__