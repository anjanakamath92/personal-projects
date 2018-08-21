from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy_spider.items import ScrapySpiderItem
from scrapy.http import Request

class MySpider(BaseSpider):
	name = "scrapy_spider"
	allowed_domains = ['instacloud.com']
	start_urls = [https://www.instacloud.com]

	def parse(self, response):
		hxs = Selector(response)

	book_titles = hxs.xpath('//div[@class="book-block-title"]/text()').extract()
	for title in book_titles:
		book = BasicCrawlerItem()
		book["title"] = title
		yeild book

	visited_links=[]
	links = hxs.xpath('//a/@href').extract()
	link_validator = re.compile("""^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}
[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/\/|\/\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$""")

	for link in links:
		if link_validator.match(link) and not link in visited_links:
			visited_links.append(link)
			yeild Request(link, self.parse)
		else:
			full_url = response.urljoin(link)
			visited_links.append(full_url)
			yeild Request(full_url, self.parse)




