import scrapy


class pgaSpider(scrapy.Spider):
    name = "PGA"
    start_urls = [
        'https://www.pgatour.com/players.html'
    ]

    def parse(self, response):
        all_players = response.css('span.name')

        for players in all_players:
            yield {
                'Name' : players.css("a").xpath("text()").extract(),
                'Link' : "https://www.pgatour.com/players" + players.css("a").xpath("@href").extract()[0]
            }
