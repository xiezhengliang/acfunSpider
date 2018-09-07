# -*- coding: utf-8 -*-

# Scrapy settings for acfunSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'acfunSpider'

SPIDER_MODULES = ['acfunSpider.spiders']
NEWSPIDER_MODULE = 'acfunSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'acfunSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept:application/json': 'text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '''ac__avi	101038905959040ecefc6251028600c651df4784846erpcx975c39394b654df17172f619c26dce5danalytics GA1.2.806335638.1502857140clientlanguagezh_CNCNZZDATA1266840871	1371770072-1517360400-null|1522312273did	web_aDiySzia1RgD75U73VCR6gmqLLoyHm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1	1536140301Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1	1534150388,1534151588,1534151893,1536137228Hm_lvt_bc75b9260fe72ee13356c664daa5568c	1515555102,1515566843,1515632968,1515637024sec_tc	AQAAAEP31RmF1wkAHnmBd2CpVtiSIqWosensorsdata2015jssdkcross	{"distinct_id":"15d4eb638881f6-00030998c1f2478-17397740-1fa400-15d4eb63889502"}session_id	web_EDAUr73canJGuuid	c9e4860dc70d516b5d7e617e5fbb479b''',
    'Host': 'www.acfun.cn',
    # 'Referer': 'http://www.acfun.cn/v/list89/index.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'acfunSpider.middlewares.AcfunspiderSpiderMiddleware': 543,
#    'acfunSpider.middlewares.userAgentDownloadMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'acfunSpider.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'acfunSpider.pipelines.AcfunspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = "localhost"
MYSQL_DBNAME = "acfun"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"