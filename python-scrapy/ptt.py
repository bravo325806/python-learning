
# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider

class PttSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.ptt.cc/']
    start_urls = ['https://www.ptt.cc/bbs/movie/index.html']
    def parse(self, response):
        count_page = count_fun()
        # with open('./count.txt','r') as f:
        #     count_page = int(f.read())
        for q in response.css('div.r-ent'):
            item = {
                'push':q.css('div.nrec > span.hl').extract_first(),
                'title':q.css('div.title > a::text').extract_first(),
                'href':q.css('div.title > a::attr(href)').extract_first(),
                'date':q.css('div.meta > div.date ::text').extract_first(),
                'author':q.css('div.meta > div.author ::text').extract_first(),
            }
            yield(item)
        # find return page btn
        next_page_url = response.css('div.action-bar > div.btn-group > a.btn::attr(href)')[3].extract()
        # run till no next page
        if (next_page_url) and (count_page < 10):
            count_page = count_page + 1 
            # with open('./count.txt','w+') as f:
            #     count_page = str(count_page)
            #     f.write(count_page)
            new = response.urljoin(next_page_url)  
        else:   
            raise  CloseSpider('close it')
        yield scrapy.Request(new, callback = self.parse, dont_filter = True)
    
                


    