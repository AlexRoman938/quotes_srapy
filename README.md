<h1> A BASIC WEB SCRAPING TO QUOTES TO SCRAPE WEBSITE </h1>

<h2> What's web scraping? </h2>

Web Scraping is a technique where you recollect data from websites.

<h2> What tool will we use? </h2>

There are many tools to do web scraping. The most known are Selenium, Beautiful Soup and Scrapy.
We will use Scrapy in this case.

<h2> Why will we use Scrapy? </h2>

It's a web scraping framework. And Scrapy is written in python. 

You can use xpath here... XPATH is a programming language to select nodos from XML document. 

<strong>For more information about Scrapy here -> </strong> https://en.wikipedia.org/wiki/Scrapy

<strong> For more information about XPATH here -> </strong> https://en.wikipedia.org/wiki/XPath

<h2> What website will we scrape? </h2>

http://quotes.toscrape.com/page/1/

<h2> INTRODUCTION </h2>

In quotes to scrape website there are many quotes with its respective authors. Therefore, we decided to extract all quotes and more from this website.

What do we want?

-Title ( It isn't very necesary )
-Top ten tags
-Quotes
-Author

<h2> DEVELOPING </h3>

<h3> TO GET XPATH FROM TOP TEN TAGS, QUOTES AND AUTHOR </h3>

First, we need to into inspect element, and visualize the HTML structure of top ten tags, quotes and author.

Top Ten Tags:

![image](https://user-images.githubusercontent.com/85772184/154829116-2aee5deb-dcad-4e3d-bf34-ae279629938e.png)


Quotes:

![image](https://user-images.githubusercontent.com/85772184/153972189-66975178-7540-4793-993c-a8bdfad32a5c.png)


Author:

![image](https://user-images.githubusercontent.com/85772184/154829128-09c4edca-b2e8-4805-9c44-98e3838e991a.png)


Next, we'll create the xpath of them.

Top Ten Tags:

![image](https://user-images.githubusercontent.com/85772184/154829057-91a51985-24e3-4e13-9c13-09bc5be02658.png)


Quotes:

![image](https://user-images.githubusercontent.com/85772184/153972796-9da7bcdd-b437-4cd6-b0e4-c4b798ee245b.png)

Author:

![image](https://user-images.githubusercontent.com/85772184/154829047-9c1f5d1c-f11d-43d6-b599-f519b0bd1b55.png)



