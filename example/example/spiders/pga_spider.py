import scrapy
from ..items import ExampleItem


class pgaSpider(scrapy.Spider):
    name = "PGA"
    start_urls = [
        'https://www.pgatour.com/stats.html'
    ]

    def parse(self, response):
        items = ExampleItem()
        player_name = response.css("td.second-td.player-name-row a").xpath("text()").extract()

        items['player_name'] = player_name

        yield items
