# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, Compose, TakeFirst
from scraping_tools.scrapy.processors.output import *
from scraping_tools.scrapy import items
import re


def getWebUrl(input):
    return re.findall('<a href="?\'?([^"\'>]*)', input)

def cleaned_description(input):
    url = ''.join(getWebUrl(''.join(input)))
    text1 = '\r\n\r\nVisit <a href="' + url + '" target="_BLANK">their website</a> to learn more.'
    text2 = '\r\n\r\nVisit <a href="' + url + '" target="_BLANK">their website</a> for more information.'
    return (''.join(input)).replace(text1, "").replace(text2, "")

class PartnerItem(items.BasicItem, items.ProductInformation):
    website = scrapy.Field(
        output_processor=Compose(strip_strings, remove_emptys, remove_duplicates, Join(''), getWebUrl),
    )
    description = scrapy.Field(
        output_processor=Compose(strip_strings, remove_emptys, remove_duplicates, Join(''), cleaned_description),
    )
    certified = scrapy.Field(
        output_processor=Compose(strip_strings, remove_emptys, remove_duplicates, Join('')),
    )
    industry = scrapy.Field()
    language = scrapy.Field()
    level = scrapy.Field()
    region = scrapy.Field()
    technology = scrapy.Field(
        output_processor=Compose(strip_strings, remove_emptys, remove_duplicates, Join('')),
    )

