from scrapy import cmdline
import re
if __name__ == '__main__':
    cmdline.execute("scrapy crawl acfunSpider".split())

    # str1 ="""var UPUser = {"contributeCount":1100,"userImg":"http://cdn.aixifan.com/dotnet/artemis/u/cms/www/201605/18162922h0u51t5r.jpg","gender":-1,"signature":"罐头视频盛产最脑洞的生活方式类短视频！","followedCount":3402,"verified":0,"isDisabled":false,"userId":4392576,"followingCount":3,"verifiedText":"","username":"罐头视频","spaceImage":""}\\nvar pageList = {"video":{"pageNo":1,"pageSize":20,"totalCount":1083,"totalPage":55,"prePage":1,"nextPage":2},"article":{"pageNo":1,"pageSize":10,"totalCount":17,"totalPage":2,"prePage":1,"nextPage":2},"flow":{"pageNo":1,"pageSize":10,"totalCount":3,"totalPage":1,"prePage":1,"nextPage":1},"flowed":{"pageNo":1,"pageSize":10,"totalCount":3402,"totalPage":341,"prePage":1,"nextPage":2}}\\nvar pageCount = {"video":1083,"article":17,"collection":0,"flow":3,"flowed":3402}"""
    # nicke_name = re.findall('"username":.*?,', str(str1))
    # signature = re.findall('"signature":.*?,', str(str1))
    # follow_number = re.findall('"followedCount":.*?,', str(str1))
    # userId = re.findall('"userId":.*?,', str(str1))

#     # nicke_name = re.search("<script>[^<]*</script>", str1)
#     # h = re.search("<script>.*?</script>", str1)
#     # h = re.findall(r"<script>.+.</script>",  str1)
#     print(nicke_name)
