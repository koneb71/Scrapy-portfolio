# -*- coding: utf-8 -*-
from scrapy.utils.test import get_crawler
from scraping_tools.test_tools.for_scrapy import *
import pytest

from mongodb import MongodbSpider

import os


def response_from(file_name):
    return mock_response_from_sample_file(my_path(__file__) + "/samples", file_name)


def describe_mongodb_spider():
    to_test = MongodbSpider.from_crawler(get_crawler())

    def describe_data_extraction():
        resp = response_from("MongoDB.html")
        results = to_test.parse(resp)

        def should_return_multiple_item():
            # parse results should hold only one item (sometimes parsers have to return a mix!)
            assert count_requests_in_parse_result(results) == 0
            assert count_items_in_parse_result(results) == 486

        def should_work_with_example():
            items = results
            print items

            sample1 = {'certified': u'Not Certified',
                       'company': u'Zadara Storage',
                       'description': u"Zadara\u2122 Storage offers an elastic primary block and file storage service for Public Cloud providers. The Zadara Virtual Private Storage Array\u2122 service enables subscribers to run MongoDB and other databases and demanding applications in the Public Cloud easily, effectively and consistently. Zadara's VPSA\u2122 service, already deployed at Amazon Web Services (AWS) and Dimension Data, combines the privacy, control and consistent performance of on-premise Enterprise storage systems with cloud economics, flexibility and ease of use.",
                       'level': [u'seed'],
                       'region': [u'North America'],
                       'src': ['http://fake_url.com'],
                       'technology': u'Cloud',
                       'type': u'Technology',
                       'website': [u'http://www.zadarastorage.com/']}

            sample2 = {'certified': u'Not Certified',
                       'company': u'WorldOverIP',
                       'description': u'WorldOverIP is an Italian IT consulting company with clients in banking, insurance and finance. Areas of expertise include project management, analysis and programming, database administration, networking and more.  ',
                       'industry': [u'Banking'],
                       'language': [u'Italian'],
                       'level': [u'seed'],
                       'region': [u'Europe'],
                       'src': ['http://fake_url.com'],
                       'technology': u'Services Partners',
                       'type': u'SIs',
                       'website': [u'http://www.worldoverip.com']}

            assert sample1 in items
            assert sample2 in items
