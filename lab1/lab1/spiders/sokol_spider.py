from scrapy.http.response import Response
import scrapy


class SokolSpider(scrapy.Spider):
    name = 'sokol'
    allowed_domains = ['sokol.ua']
    start_urls = ['https://sokol.ua/products/noutbuki/?product_list_limit=36&price=10000-']

    def parse(self, response: Response):
        products = response.xpath("//div[contains(@class, 'product details product-item-details')]")[:20]

        for product in products:
            yield {
                'description': product.xpath(".//a[contains(@class,'name')]/text()").get(),
                'img': product.xpath(".//img[contains(@class,'owl-lazy')]/@data-src").get(),
                'price':product.xpath(".//span[contains(@class, 'price-wrapper')]/@data-price-amount").get()

            }