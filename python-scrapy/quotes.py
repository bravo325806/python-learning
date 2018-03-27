# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log('I visited :'+ response.url)
        yield {
            'author_name':response.css('small.author::text')[0].extract(),
            'texts':response.css('span.text::text')[0].extract(),
            # 'tags':response.css('a.tag:text')[0].extract(),
        }
