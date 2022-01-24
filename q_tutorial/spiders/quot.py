from email.quoprimime import quote
import scrapy

#Título = '//h1/a/text()'
#Citas = '//span[@class = "text" and  @itemprop = "text"]/text()'
#Citas top = '//div[contains(@class, "tags-box")]//span[@class = "tag-item"]/a/text()'
#Next page button = '//ul[@class = "pager"]//li[@class = "next"]/a/@href'
#Autor = '//small[@class = "author" and @itemprop = "author"]/text()'

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
                'fields': ['title', 'tags_top', 'quo_and_auth'], #Estos campos tienen que estar igual que las variables
                'overwrite': True
            }
        }

        ,

        'MEMUSAGE_LIMIT_MB' : 2048, #Para decirle al spyder cuanta memoria ram utilizar
        'MEMUSAGE_NOTIFY_MAIL':  ['aroman.link11@gmail.com'], #Para mandar alerta si es que sobrepasa el limite de memoria
        'ROBOTSTXT_OBEY' : True, #True para que obedeza el robots , False si es que no
        'USER_AGENT': 'SnowD', #Con esto nuestro bot que hace la petición se llamará así

    }

    def parse_only_quotes_with_author(self, response, **kwargs): #guardar las citas

        if kwargs:

            quotes = kwargs['quotes']
            author = kwargs['author']

        quotes.extend(response.xpath('//span[@class = "text" and  @itemprop = "text"]/text()').getall())
        author.extend(response.xpath('//small[@class = "author" and @itemprop = "author"]/text()').getall())

        quo_and_auth = {}
        
        for i in range(0,len(quotes)):

            quo_and_auth[quotes[i]] = author[i]
        


        next_page_button_link = response.xpath('//ul[@class = "pager"]//li[@class = "next"]/a/@href').get()

        if next_page_button_link:

            yield response.follow(next_page_button_link, callback = self.parse_only_quotes_with_author, cb_kwargs = {'quotes': quotes, 'author': author})
        
        else:

            yield{

                'quo_and_auth' :  quo_and_auth,
            }

    def parse(self, response): #Analizar un archivo para extraer información valiosa

        title = response.xpath('//h1/a/text()').get()
        
        quotes = response.xpath('//span[@class = "text" and  @itemprop = "text"]/text()').getall()
        
        author = response.xpath('//small[@class = "author" and @itemprop = "author"]/text()').getall()
        
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

            yield response.follow(next_page_button_link, callback = self.parse_only_quotes_with_author, cb_kwargs = {'quotes': quotes, 'author': author})
        
      