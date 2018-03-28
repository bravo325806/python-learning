# -*- coding: utf-8 -*-
import scrapy
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response, page):
        # self.log('I visited :'+ response.url)
        for q in response.css('div.quote'):
            item = {
                'author_name':q.css('small.author::text').extract_first(),
                'texts':q.css('span.text::text').extract_first(),
                'tags':q.css('a.tag::text').extract(),
            }
            yield(item)
        # find next page btn
        next_page_url = response.css('li.next > a ::attr(href)').extract_first()
        # run till no next page
        if next_page_url: 
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url ,callback = self.parse)
