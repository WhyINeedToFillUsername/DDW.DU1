import scrapy


class ZiveSpider(scrapy.Spider):
    custom_settings = {
        # 'REDIRECT_ENABLED': False,
        'USER_AGENT': 'DDW_robot',
        'DOWNLOAD_DELAY': 0.1,
        'ROBOTSTXT_OBEY': True,
        # 'COOKIES_DEBUG': True,
        # 'HANDLE_HTTPSTATUS_LIST': [302]
    }

    name = "zive"
    start_urls = [
        'https://www.zive.cz/'
    ]

    MAX_PAGES = 100
    page = 1

    # parse the main page - get the first list of articles to crawl
    def parse(self, response):
        # get list of articles
        for row in response.css('div.ar-row'):
            article_url = row.css('h2 > a::attr(href)').extract_first()
            if article_url is not None and "https://" not in article_url:
                article_url = response.urljoin(article_url)
                # go to the link
                yield scrapy.Request(article_url, callback=self.parse_article)

        # get next page, limit number of pages
        if ZiveSpider.page < ZiveSpider.MAX_PAGES:
            next_page = response.urljoin("/?pgnum={}".format(ZiveSpider.page))
            ZiveSpider.page += 1
            yield scrapy.Request(next_page, callback=self.parse)

    # parse an article - get the content and follow related articles
    def parse_article(self, response):
        full_article = ""
        for par in response.css('div.ar-content.ar-inquiry-holder > p::text').extract():
            full_article += par

        yield {
            'url': response.url,
            'title': response.css('h1[itemprop=name]::text').extract_first(),
            'author': response.css('a[itemprop=author]::text').extract_first(),
            'date': response.css('span.ar-date::text').extract_first(),
            'content': full_article,
            'tags': response.css('div.ar-detail p.ar-tags a::text').extract(),
        }

        # get related articles - not working because of dynamic javascript adding
        # for next_page in response.css('div.spklw-post > a::attr(href)').extract():
        #     yield scrapy.Request(next_page, callback=self.parse_article)
