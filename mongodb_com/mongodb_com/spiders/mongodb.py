# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
import re
import json
import sys

from mongodb_com.items import PartnerItem

class MongodbSpider(CrawlSpider):
    name = "mongodb"
    allowed_domains = ["mongodb.com"]
    start_urls = (
        'https://www.mongodb.com/partners/list',
    )

    def parse(self, response):
        data = json.loads(''.join(response.xpath("//*[@id='initial-data']/@data-props").extract()))
        results = []
        for item in data['data']['partner']:
            try:
                result = self.parse_single_item(item, response)
                if result: results.append(result)
            except Exception, e:
                et, ei, tb = sys.exc_info()
                print et
                print ei
                print tb
        return results

    def parse_single_item(self, item, response):
        l = ItemLoader(PartnerItem(), response)

        l.add_value("src", response.url)
        l.add_value("company", item['title'])
        l.add_value("description", item['summary'])
        l.add_value("website", item['summary'])

        if item['attr']['certified']: l.add_value("certified", item['attr']['certified'])
        if item['attr']['industry']: l.add_value("industry", item['attr']['industry'])
        if item['attr']['language']: l.add_value("language", item['attr']['language'])
        if item['attr']['level']: l.add_value("level", item['attr']['level'])
        if item['attr']['region']: l.add_value("region", item['attr']['region'])
        if item['attr']['technology']: l.add_value("technology", item['attr']['technology'])
        if item['attr']['type']: l.add_value("type", item['attr']['type'])

        return l.load_item()