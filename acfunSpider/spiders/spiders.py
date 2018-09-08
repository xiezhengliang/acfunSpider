# encoding=utf-8
import re
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from acfunSpider.items import UserItem, VideoItem
import json
import re
import datetime


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
        for video in data_json['data']:
            user_url = video['userUrl']
            yield Request(url=user_url, callback=self.user_parse)
        for page in range(2, page_count):
            next_page_url = 'http://www.acfun.cn/list/getlist?channelId=89&sort=0&pageSize=20&pageNo=' + str(page)
            yield Request(url=next_page_url, callback=self.total_num_parse)

    def user_parse(self, response):
        item = UserItem()
        url = response.url
        id = re.sub("\D", "", url)
        html = response.text
        main = Selector(text=html).xpath("//div[@class='main']").extract()
        script = str(re.findall("<script>[^<]*</script>", str(main)))
        username = re.findall('"username":.*?,', str(script))  # 用户名
        signature = re.findall('"signature":.*?,', str(script))  # 签名
        followingCount = re.findall('"followingCount":.*?,', str(script))  # 关注数
        userId = re.findall('"userId":.*?,', str(script))  # 用户id
        followedCount = re.findall('"followedCount":.*?,', str(script))  # 粉丝数
        contributeCount = re.findall('"contributeCount":.*?,', str(script))  # 投稿数
        totalPage = re.findall('"totalPage":.*?,', str(script))[0]
        item['user_id'] = int(id)
        item['nick_name'] = str(username[0]).replace('"username":"', "").replace('",', "")
        item['signature'] = str(signature[0]).replace('"signature":"', "").replace('",', "")
        item['video_number'] = int(
            str(contributeCount[0]).replace('"contributeCount":', "").replace(',', "").replace(".", "").replace("万",
                                                                                                                ""))
        item['fans_number'] = int(
            str(followedCount[0]).replace('"followedCount":', "").replace(',', "").replace(".", "").replace("万", ""))
        item['follows_number'] = int(
            str(followingCount[0]).replace('"followingCount":', "").replace(',', "").replace(".", "").replace("万", ""))
        item['url'] = url
        total_page = int(str(totalPage).replace('"totalPage":', "").replace(',', ""))
        # clearfix = Selector(text=html).xpath("//div[@class='clearfix']").extract()
        # nicke_name = Selector(text=str(clearfix)).xpath("//div[@class='name fl text-overflow']/text()").extract()
        # video_number = Selector(text=str(clearfix)).xpath("//span[@class='fl sub']/text()").extract()
        # follow_number = Selector(text=str(clearfix)).xpath("//span[@class='fl follow']/text()").extract()
        # fans_number = Selector(text=str(clearfix)).xpath("//span[@class='fl fans']/text()").extract()
        # signature = Selector(text=str(html)).xpath("//div[@class='infoM']/text()").extract()
        # hint = Selector(text=str(html)).xpath("//div[@id='list-pager-video']").extract()
        # page_count = re.sub("\D", "", str(hint))
        # yield Request(url=url, meta={"totalPage": totalPage, "user_id": id}, callback=self.user_page_parse)
        for pageno in range(1, total_page):
            next_page_url = "http://www.acfun.cn/space/next?uid=" + str(
                id) + "&type=video&orderBy=2&pageNo=" + str(pageno)
            yield Request(url=next_page_url, meta={"user_id": id}, callback=self.video_parse)
        yield item

    def video_parse(self, response):
        item = VideoItem()
        user_id = response.meta['user_id']
        text = json.loads(response.text)
        html = text['data'].get("html", "")
        video_list = Selector(text=str(html)).xpath("//a/figure").extract()
        for v in video_list:
            data_date = Selector(text=v).xpath("//@data-date").extract()[0]
            data_url = Selector(text=v).xpath("//@data-url").extract()[0]
            data_title = Selector(text=v).xpath("//@data-title").extract()[0]
            watch_number = Selector(text=v).xpath("//p[@class='crumbs']//span[@class='nums']/text()").extract()[0]
            barrage_number = Selector(text=v).xpath("//p[@class='crumbs']//span[@class='nums']/text()").extract()[1]
            item['user_id'] = int(user_id)
            item['title'] = data_title
            item['watch_number'] = int(watch_number.replace(".", "").replace("万", ""))
            item['barrage_number'] = int(barrage_number.replace(".", "").replace("万", ""))
            item['time'] = datetime.datetime.strptime(data_date, "%Y/%m/%d")
            item['data_url'] = data_url
            yield item
