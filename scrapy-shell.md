
You can go to [this page](http://quotes.toscrape.com/)

Start command: 
```sh
$ scrapy shell http://quotes.toscrape.com
```

We can find in this page:
```
tag : <small>
class: <author>
```

get all element:
```
$ response.css('small.author')
```
extract it :
```
$ response.css('small.author').extract()
```
only want content text :
```
$ response.css('small.author::text').extract()
```

We can find in this page:
```
tag : <span>
class: <text>
```
Only get text list by tag and class 
```
$ response.css('span.text::text').extract()
```
---

Run a Scrapy file :
```
$ crapy genspider quotes http://quotes.toscrape.com/
```
then you will see `quotes.py` in your directory.



