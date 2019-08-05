import scrapy
import json


class pgaSpider(scrapy.Spider):
    name = "spidyPGA"
    start_urls = [
        'https://statdata.pgatour.com/players/25198/2019stat.json'
    ]
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body)

        for item in data.get('quotes', []):
            yield {
                'first': row.xpath('th[1]//text()').extract_first(),
                # 'last': row.xpath('td[2]//text()').extract_first(),
                # 'handle' : row.xpath('td[3]//text()').extract_first(),
            }
