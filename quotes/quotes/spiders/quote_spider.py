import scrapy
from ..items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quotespider'
    start_urls = ['http://www.goodreads.com/quotes/tag/fashion']

    def parse(self, response):
        for quote_block in response.xpath('//div[@class="quoteDetails "]'):
            item = QuoteItem()
            
            item['text'] = quote_block.xpath('div[@class="quoteText"]/text()')[0].extract()
            item['author'] = quote_block.xpath('div[@class="quoteText"]/a/text()')[0].extract()
            item['tags'] = quote_block.xpath('div[@class="quoteFooter"]/div[1]/a/text()').extract()
            item['likes'] = quote_block.xpath('div[@class="quoteFooter"]/div[2]/a/text()')[0].extract()

            yield item