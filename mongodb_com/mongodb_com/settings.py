# -*- coding: utf-8 -*-

# Scrapy settings for mongodb_com project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mongodb_com'

SPIDER_MODULES = ['mongodb_com.spiders']
NEWSPIDER_MODULE = 'mongodb_com.spiders'

COOKIES_ENABLED = False
DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS = 20
CONCURRENT_REQUESTS_PER_DOMAIN = 1

DOWNLOAD_TIMEOUT = 30

# activate to go as fast as possible
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_DEBUG = True
#AUTOTHROTTLE_MAX_DELAY = 10.0

# activate proxy rotation if needed
DOWNLOADER_MIDDLEWARES = {
    #'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    #'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 95,
    #'scraping_tools.scrapy.middlewares.proxy_net.ProxyNetMiddleware': 100,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
    'scraping_tools.scrapy.middlewares.rotate_user_agent.RotateUserAgentMiddleware' :400
}


# USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
# USER_AGENT = "Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
# USER_AGENT = "Mozilla/5.0 (compatible; bingbot/2.0 +http://www.bing.com/bingbot.htm)"

# force output as csv
FEED_FORMAT = 'csv'
#FEED_EXPORT_FIELDS = ["category", "count", "listingUrl", "title", "streetAddress", "postalCode", "locality", "countryName", "companyUrl", "phoneNumber", "faxNumber", "latitude", "longitude", "email"]

# PROXY_LIST_URL = "http://proxy-list.org/english/yourproxylists/speed-16/limit-3000/type-elite/ssl-no/9de8e524f7c51669bc3cfdf2fee5f9d4.txt"
#  "http://proxy-list.org/english/yourproxylists/limit-300/country-usa-and-canada/type-anonymous-and-elite/9de8e524f7c51669bc3cfdf2fee5f9d4.txt"
PROXY_LIST_URL = "http://proxy-list.org/english/yourproxylists/limit-3000/speed-16/type-anonymous-and-elite/9de8e524f7c51669bc3cfdf2fee5f9d4.txt"
PROXY_LIST_RELOAD_SECONDS = 1800


#DOWNLOAD_HANDLERS = {
#    'http':  'scraping_tools.scrapy.download_handlers.js_downloader.JsDownloader',
#    'https': 'scraping_tools.scrapy.download_handlers.js_downloader.JsDownloader',
#}

#WEBDRIVERS_LIST = ["http://127.0.0.1:8910"]

# run phantomjs locally: phantomjs --webdriver='127.0.0.1:8910'


#
# DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 600}
# CRAWLERA_ENABLED = True
# CRAWLERA_USER = 'd280347b258f4dfcbecc2570143034fb'
# CRAWLERA_PASS = ''
#
# #DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# #   'X-Crawlera-UA': 'desktop',
# #}
#
# CONCURRENT_REQUESTS = 256
# CONCURRENT_REQUESTS_PER_DOMAIN = 64
# DOWNLOAD_TIMEOUT = 600
#
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_DEBUG = True
# #AUTOTHROTTLE_MAX_DELAY = 60.0

# # Retry many times since proxies often fail
# RETRY_TIMES = 1000
# # Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 502, 503, 504, 429, 400, 403, 404, 408, 429, 470, 999]
# REDIRECT_PRIORITY_ADJUST = 200