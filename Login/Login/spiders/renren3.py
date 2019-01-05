# -*- coding: utf-8 -*-
import scrapy


class Renren3Spider(scrapy.Spider):

    custom_settings = {
        'COOKIES_ENABLED': True
    }
    cookies = {
        'anonymid': 'jpicghe03gkycv',
        '_r01_': '1',
        'ln_uact': '15731664508',
        'ln_hurl': 'http://head.xiaonei.com/photos/0/0/men_main.gif',
        'jebe_key': '7497737a-95e3-414c-ad6d-04b5adce6baf%7C5d834e261e1cd6cb2b72b047f7d73840%7C1544448044050%7C1%7C1544448042378',
        'depovince': 'BJ',
        'ick_login': 'de37432d-0392-476b-afe1-2d276645a4c4',
        'first_login_flag': '1',
        'loginfrom': 'syshome',
        'ch_id': '10016',
        'JSESSIONID': 'abcxytP-gdzD-acIJxbFw',
        'wp_fold': '0',
        'Hm_lvt_966bff0a868cd407a416b4e3993b9dc8': '1545143655',
        'Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8': '1545143655',
        '_ga': 'GA1.2.319562852.1545143656',
        '_gid': 'GA1.2.1797535655.1545143656',
        '_ga': 'GA1.3.319562852.1545143656',
        '_gid': 'GA1.3.1797535655.1545143656',
        'jebecookies': 'f0f99dea-8c4b-4223-b691-bf1f5bba984a|||||',
        '_de': 'BA24B5DD754B276DB9D2F66C60E5CA77',
        'p': '31f28b57bb3d8c4a361ca590fb03b0f01',
        't': '2b0cd7e60090858cfb00677d733d18f01',
        'societyguester': '2b0cd7e60090858cfb00677d733d18f01',
        'id': '830760061',
        'xnsid': '3e3ca4ae',
        'jebe_key': '7497737a - 95e3 - 414c - ad6d - 04b5adce6baf % 7C5d834e261e1cd6cb2b72b047f7d73840 % 7C1544448044050 % 7C1 % 7C1545144067928'
    }

    name = 'renren3'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/']

    def start_requests(self):
        yield scrapy.FormRequest('http://www.renren.com/', cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        yield scrapy.Request('http://www.renren.com/410057922/profile', callback=self.lcz)

    def lcz(self, response):
        with open('lcz2.html', 'wb') as f:
            f.write(response.body)
