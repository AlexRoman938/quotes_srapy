import scrapy

#Título = '//h1/a/text()'
#Citas = '//span[@class = "text" and  @itemprop = "text"]/text()'
#Citas top = '//span[@class = "tag-item"]/a[@class = "tag"]/text()'
#Next page button = '//ul[@class = "pager"]//li[@class = "next"]/a/@href'

class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    start_urls = [
             'http://quotes.toscrape.com/page/1/'
    ]

    custom_settings = {
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'fields': ['title', 'quotes', 'top_ten_tags'],
                'overwrite': True
            }
        }
    }


    def parse(self, response): #Analizar un archivo para extraer información valiosa

        title = response.xpath('//h1/a/text()').get()
        
        quotes = response.xpath('//span[@class = "text" and  @itemprop = "text"]/text()').getall()
        
        tags_top = response.xpath('//span[@class = "tag-item"]/a[@class = "tag"]/text()').getall()
        
        yield{
            'title' : title,
            'quotes' : quotes,
            'tags_top' : tags_top

        }

 
        next_page_button_link = response.xpath('//ul[@class = "pager"]//li[@class = "next"]/a/@href').get()

        if next_page_button_link:

            yield response.follow(next_page_button_link, callback = self.parse)
        
        