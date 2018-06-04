import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from nautica.items import NauticaItem

class NauticaSpider(CrawlSpider):
	name = 'nautica'
	item_count = 0
	allowed_domain = ['www.example.com']

	start_urls = [
				'https://www.example.com/5.html?language=es',
				
	]

	rules = {
			Rule(LinkExtractor(allow = (), restrict_xpaths = ('//span/a[contains(@title, " Siguiente ")]'))),
			Rule(LinkExtractor(allow = (), restrict_xpaths = ('//span[@class="ProductName"]')),
								callback = 'parse_item', follow = False)
		}

	def parse_item(self,response):
		bo_item = NauticaItem()
		# product_info
		
		bo_item['nombre'] = response.xpath('normalize-space(//*[@id="products_name"]/text())').extract()
		bo_item['url'] = response.xpath('//div[contains(@id, "breadcrumbs")]/a[4]/@href').extract()
		bo_item['imagen'] = response.xpath('//div[contains(@id, "products_imagenes")]/a/@href').extract()
		bo_item['modelo'] = response.xpath('//*[@id="products_model"]/text()').extract()
		bo_item['categoria'] = response.xpath('//span[@class="smallText"]/a/text()').extract()
		bo_item['precio'] = response.xpath('//span[@class = "productInfoSpecialNewPrice"]/text()').extract()
		bo_item['descripcion'] = response.xpath('//div[contains(@id, "products_description")]/p/text()').extract()
		bo_item['opiniones'] = response.xpath('//div[contains(@id, "cuadro_voto_numero")]/text()').extract()
		
		
		self.item_count += 1
		if self.item_count > 2238:
			raise CloseSpider('item_exceded')

		yield bo_item