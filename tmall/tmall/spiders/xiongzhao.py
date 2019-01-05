# -*- coding: utf-8 -*-
import scrapy, json, re
from tmall.items import TmallItem


class XiongzhaoSpider(scrapy.Spider):
    name = 'xiongzhao'
    allowed_domains = ['tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton']

    def parse(self, response):
        url_list = response.xpath('//a[@class="productImg"]/@href').extract()
        for url in url_list:
            itemid = url.split('&skuId')[0].replace('//detail.tmall.com/item.htm?id=', '')
            pages_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId='+str(itemid)+'&spuId=284996589&sellerId=1813097055&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvevvovLWvUvCkvvvvvjiPR259sjYURFqZQjljPmPZzjlWRF5UQjnHPssWAj3PRphvChCvvvvtvpvhphvvvUhCvvswMmaeRrMwznAwclujvpvhphhvv8wCvvBvpvpZ2QhvCvvvMMGCvpvVphhvvvvvmphvLhnQVpmFd369nCkDYEkOaZEQcneYr2E9Zj%2BO3w0AhjE2J9kx6fItb9gDNr3l5dUf8BlVD764d361bpPClfy64HDlpKLWetis7eQCKWVEvpvVpyUUCEKOuphvmhCvCEllaYjfKphv8hCvvvvvvhCvphvZVpvvpkxvpCBXvvC2p6CvHHyvvh89phvZ7pvvpiQtvpvhphvvv2yCvvBvpvvvdphvmZCmpBkYvhCbZ86CvvDvpFipo9Cv7LACvpvWzCAYf5sSznswjg14dphvmZCmmlvwvhC%2BsIhCvCLwP8iK1nMwznQm5lSzIaAhzVC49p%3D%3D&needFold=0&_ksTS=1545834775243_1179&callback=jsonp1180'
            yield scrapy.Request(pages_url, callback=self.second, meta={'itemid': itemid, 'download_timeout': 10})

    def second(self, response):
        itemid = response.meta['itemid']
        text = response.text.replace('jsonp1180(', '').replace(')', '')
        text = json.loads(text, encoding='utf-8')
        pagination = int(text['rateDetail']['paginator']['lastPage'])
        for currentPage in range(1, int(pagination) + 1):
            detail_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId='+str(itemid)+'&spuId=284996589&sellerId=1813097055&order=3&currentPage='+str(currentPage)+'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvevvovLWvUvCkvvvvvjiPR259sjYURFqZQjljPmPZzjlWRF5UQjnHPssWAj3PRphvChCvvvvtvpvhphvvvUhCvvswMmaeRrMwznAwclujvpvhphhvv8wCvvBvpvpZ2QhvCvvvMMGCvpvVphhvvvvvmphvLhnQVpmFd369nCkDYEkOaZEQcneYr2E9Zj%2BO3w0AhjE2J9kx6fItb9gDNr3l5dUf8BlVD764d361bpPClfy64HDlpKLWetis7eQCKWVEvpvVpyUUCEKOuphvmhCvCEllaYjfKphv8hCvvvvvvhCvphvZVpvvpkxvpCBXvvC2p6CvHHyvvh89phvZ7pvvpiQtvpvhphvvv2yCvvBvpvvvdphvmZCmpBkYvhCbZ86CvvDvpFipo9Cv7LACvpvWzCAYf5sSznswjg14dphvmZCmmlvwvhC%2BsIhCvCLwP8iK1nMwznQm5lSzIaAhzVC49p%3D%3D&needFold=0&_ksTS=1545834775243_1179&callback=jsonp1180'
            yield scrapy.Request(detail_url, callback=self.third, meta={'download_timeout': 10})

    def third(self, response):
        text = response.text.replace('jsonp1180(', '').replace(')', '')
        text = json.loads(text, encoding='utf-8')
        rateList = text['rateDetail']['rateList']
        for rate in rateList:
            color = re.split('[;:]', rate['auctionSku'])[1]
            size = re.split('[;:]', rate['auctionSku'])[3]
            date = rate['rateDate']
            comment = rate['rateContent']
            source = '天猫'
            item = TmallItem()
            item['color'] = color
            item['size'] = size
            item['date'] = date
            item['comment'] = comment
            item['source'] = source
            yield item


