# encoding=utf-8
import re
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from acfunSpider.items import UserItem
import json
import re

class Spider(CrawlSpider):
    name = "acfunSpider"
    host = "http://www.acfun.cn/"


    def start_requests(self):
        star_url = "http://www.acfun.cn/list/getlist?channelId=89&sort=0&pageSize=20&pageNo=1"
        yield Request(url=star_url, callback=self.total_num_parse)  # 去爬关注人

    def total_num_parse(self, response):
        html = json.loads(response.text)
        data_json = html['data']
        page_count = data_json['params'].get("pageCount", 0)
        # page_count = 10
        for video in data_json['data']:
            user_url = video['userUrl']
            yield Request(url=user_url, callback=self.user_parse)
        for page in range(2, page_count):
            next_page_url = 'http://www.acfun.cn/list/getlist?channelId=89&sort=0&pageSize=20&pageNo='+str(page)
            yield Request(url=next_page_url, callback=self.total_num_parse)
    def user_parse(self, response):
        item = UserItem()
        url = response.url
        id = re.sub("\D", "", url)
        html = response.text
        main = Selector(text=html).xpath("//div[@class='main']").extract()
        script = str(re.findall("<script>[^<]*</script>", str(main)))
        username = re.findall('"username":.*?,', str(script))  #用户名
        signature = re.findall('"signature":.*?,', str(script))  #签名
        followingCount = re.findall('"followingCount":.*?,', str(script))  #关注数
        userId = re.findall('"userId":.*?,', str(script))  #用户id
        followedCount = re.findall('"followedCount":.*?,', str(script))  #粉丝数
        contributeCount = re.findall('"contributeCount":.*?,', str(script))  #投稿数
        totalPage = re.findall('"totalPage":.*?,', str(script))[0]
        item['user_id'] = int(id)
        item['nick_name'] = str(username[0]).replace('"username":"', "").replace('",', "")
        item['signature'] = str(signature[0]).replace('"signature":"', "").replace('",', "")
        item['video_number'] = int(str(contributeCount[0]).replace('"contributeCount":', "").replace(',', ""))
        item['fans_number'] = int(str(followedCount[0]).replace('"followedCount":', "").replace(',', ""))
        item['follows_number'] = int(str(followingCount[0]).replace('"followingCount":', "").replace(',', ""))
        item['url'] = url
        # item['page_count'] = str(totalPage).replace('"totalPage":', "").replace(',', "")


        # clearfix = Selector(text=html).xpath("//div[@class='clearfix']").extract()
        # nicke_name = Selector(text=str(clearfix)).xpath("//div[@class='name fl text-overflow']/text()").extract()
        # video_number = Selector(text=str(clearfix)).xpath("//span[@class='fl sub']/text()").extract()
        # follow_number = Selector(text=str(clearfix)).xpath("//span[@class='fl follow']/text()").extract()
        # fans_number = Selector(text=str(clearfix)).xpath("//span[@class='fl fans']/text()").extract()
        # signature = Selector(text=str(html)).xpath("//div[@class='infoM']/text()").extract()
        # hint = Selector(text=str(html)).xpath("//div[@id='list-pager-video']").extract()
        # page_count = re.sub("\D", "", str(hint))
        yield item


