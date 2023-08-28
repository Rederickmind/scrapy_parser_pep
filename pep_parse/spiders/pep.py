import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        table = response.css("section[id='numerical-index']")
        all_peps = table.css('tbody')
        all_peps_links = all_peps.css('a::attr(href)').getall()
        for pep_link in all_peps_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_info = response.css("section[id='pep-content']")
        number, name = (
            pep_info.css(
                'h1.page-title::text'
            ).get().split(' – ', 1)
        )
        pep_status = pep_info.css('abbr::text').get()

        pep_data = {
            'number': number.split()[1],
            'name': name,
            'status': pep_status
        }
        print(pep_data)
        yield PepParseItem(pep_data)
