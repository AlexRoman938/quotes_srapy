import scrapy

#Título = '//h1/a/text()'
#Citas = '//span[@class = "text" and  @itemprop = "text"]/text()'
#Citas top = '//div[contains(@class, "tags-box")]//span[@class = "tag-item"]/a/text()'
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
                'fields': ['title', 'tags_top', 'quotes'], #Estos campos tienen que estar igual que las variables
                'overwrite': True
            }
        }

        ,

        'MEMUSAGE_LIMIT_MB' : 2048 #Para decirle al spyder cuanta memoria ram utilizar
    }

    def parse_only_quotes(self, response, **kwargs): #guardar las citas

        if kwargs:

            quotes = kwargs['quotes']

        quotes.extend(response.xpath('//span[@class = "text" and  @itemprop = "text"]/text()').getall())

        next_page_button_link = response.xpath('//ul[@class = "pager"]//li[@class = "next"]/a/@href').get()

        if next_page_button_link:

            yield response.follow(next_page_button_link, callback = self.parse_only_quotes, cb_kwargs = {'quotes': quotes})
        
        else:

            yield{

                'quotes' : quotes
            }

    def parse(self, response): #Analizar un archivo para extraer información valiosa

        title = response.xpath('//h1/a/text()').get()
        
        quotes = response.xpath('//span[@class = "text" and  @itemprop = "text"]/text()').getall()
        
        tags_top = response.xpath('//div[@class="col-md-4 tags-box"]//span[@class="tag-item"]/a/text()').getall()
        
        top = getattr(self, 'top', None) #Argumento para sacar el top 5 o lo que queramos de tags_top
        
        if top:

            top = int(top)
            tags_top = tags_top[:top] #Nos traer hasta el indice que queremos
            
        yield{
            'title' : title,
            'tags_top' : tags_top

        }

 
        next_page_button_link = response.xpath('//ul[@class = "pager"]//li[@class = "next"]/a/@href').get()

        if next_page_button_link:

            yield response.follow(next_page_button_link, callback = self.parse_only_quotes, cb_kwargs = {'quotes': quotes})
        
      