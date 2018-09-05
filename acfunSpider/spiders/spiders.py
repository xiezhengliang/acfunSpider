# encoding=utf-8
import re
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from acfunSpider.items import UserItem


class Spider(CrawlSpider):
    name = "acfunSpider"
    host = "http://www.acfun.cn/"


    def start_requests(self):
        star_url = "http://www.acfun.cn/v/list89/index.htm"
        yield Request(url=star_url, callback=self.total_num_parse)  # 去爬关注人

    def total_num_parse(self, response):
        item = UserItem()
        html = response.text
        yield item
        url_next = Selector(text="").xpath(u"//div[@class='WB_cardpage S_line1']/div[@class='W_pages']/a[last()]/@href").extract()
        if url_next:
            yield Request(url=self.host + url_next[0], callback=self.parse3)

