# -*- coding: utf-8 -*-

# Scrapy settings for tmall project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tmall'

SPIDER_MODULES = ['tmall.spiders']
NEWSPIDER_MODULE = 'tmall.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tmall (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path': '/list_detail_rate.htm?itemId=40001265455&spuId=284996589&sellerId=1813097055&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvevvovLWvUvCkvvvvvjiPR259sjYURFqZQjljPmPZzjlWRF5UQjnHPssWAj3PRphvChCvvvvtvpvhphvvvUhCvvswMmaeRrMwznAwclujvpvhphhvv8wCvvBvpvpZ2QhvCvvvMMGCvpvVphhvvvvvmphvLhnQVpmFd369nCkDYEkOaZEQcneYr2E9Zj%2BO3w0AhjE2J9kx6fItb9gDNr3l5dUf8BlVD764d361bpPClfy64HDlpKLWetis7eQCKWVEvpvVpyUUCEKOuphvmhCvCEllaYjfKphv8hCvvvvvvhCvphvZVpvvpkxvpCBXvvC2p6CvHHyvvh89phvZ7pvvpiQtvpvhphvvv2yCvvBvpvvvdphvmZCmpBkYvhCbZ86CvvDvpFipo9Cv7LACvpvWzCAYf5sSznswjg14dphvmZCmmlvwvhC%2BsIhCvCLwP8iK1nMwznQm5lSzIaAhzVC49p%3D%3D&needFold=0&_ksTS=1545834775243_1179&callback=jsonp1180',
            'scheme': 'https',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'cna=u1CVFDRijzACAXaQhSfQPUiJ; hng=CN%7Czh-CN%7CCNY%7C156; uss=""; enc=1YoMc8kB9wAcPiOf3zhiwKucss%2F4tGlQJh3v%2Fhs%2Bz0ouTZk5Hg7mJOVOPIR0DanK0j3yaY2HrjqLPKXYHW27IQ%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; lid=%E9%98%B2%E7%81%BE%E6%88%90%E6%97%AD%E5%85%89; _m_h5_tk=6bf33edf0795b49b3b3299bf46a133a8_1545836378305; _m_h5_tk_enc=b22e9366514aa74ba7663eb40167de61; t=ae99d6ca84f0ab52f176b7d21dfc44d1; uc3=vt3=F8dByRMHi5alaMTWmJc%3D&id2=UonfPoKUuPY8XQ%3D%3D&nk2=1AdMIPGj2coPfA%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu9632%5Cu707E%5Cu6210%5Cu65ED%5Cu5149; lgc=%5Cu9632%5Cu707E%5Cu6210%5Cu65ED%5Cu5149; _tb_token_=e533b77993e33; cookie2=18d5b22574e132ae1ad4b668190a1954; x5sec=7b22726174656d616e616765723b32223a22333566396631393833393363306434633866643363633934333965396238363443504f686a754546454b696a724c662f7562373143413d3d227d; isg=BLW1b6meBVcygWHYGYpbb9cdxDGvmmgvOwOoDzfa3ywXDtYA_4EpFJrIXJKdSIH8; l=aBCjQkJ-yzx-zUbKQMa4NNp1w707g8fPsW_O1MwHDTEhNPuR7RXy1brbI_zwMJNQZqZjPm02CcSZ.',
            'referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.5c732beaNZdGZK&id=40001265455&areaId=440300&user_id=1813097055&cat_id=2&is_b=1&rn=ee981af686a4fc030c2ac13f083f3f31',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tmall.middlewares.TmallSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tmall.middlewares.TmallUserAgentProxyMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tmall.pipelines.TmallPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
RETRY_ENABLED = True
RETRY_TIMES = 5
