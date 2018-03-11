import scrapy
from time import sleep


class RegiojetSpider(scrapy.Spider):
    custom_settings = {
        # 'REDIRECT_ENABLED': False,
        # 'USER_AGENT': 'DDW',
        # 'DOWNLOAD_DELAY': 0.00005,
        'ROBOTSTXT_OBEY': True,
        'COOKIES_DEBUG': True,
        # 'HANDLE_HTTPSTATUS_LIST': [302]
    }
    handle_httpstatus_list = [302]

    counter = 0
    name = "regiojet"
    start_urls = [
        'https://jizdenky.regiojet.cz/',

        'https://jizdenky.regiojet.cz/Booking/'
        'from/372825000/to/17655001/'
        'tarif/REGULAR/departure/20180404/'
        'retdep/20180404/'
        'return/false',

        # 'https://jizdenky.regiojet.cz/Booking/'
        # 'from/372825000/to/17655001/'
        # 'tarif/REGULAR/departure/20180404'
        # '/retdep/20180404/'
        # 'return/false?0-9.IBehaviorListener.0-mainPanel-routesPanel-content'
        # '-refreshRoutesButton&_=1520698958485'
    ]

    # def start_requests(self):
    #     for u in self.start_urls:
    #         yield scrapy.Request(u, meta={'dont_redirect': True}, callback=self.parse_httpbin,
    #                              errback=self.errback_httpbin,
    #                              dont_filter=True)
    #
    # def parse_httpbin(self, response):
    #     print('cookie from login', response.headers)
    #
    # def errback_httpbin(self, failure):
    #     print('error', repr(failure))

    def parse(self, response):
        # self.log('cookie from login', response.headers.getlist('Set-Cookie'))
        print('cookie from login', response.headers.getlist('Set-Cookie'))

        filename = 'results_%s.html' % RegiojetSpider.counter
        RegiojetSpider.counter += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        # sleep(4)

        # for quote in response.css('div#ticket_lists'):
        #     yield {
        #         'day': quote.css('#id49 > div > h2.overflow_h1::text').extract_first(),
        #         # 'author': quote.css('small.author::text').extract_first(),
        #         # 'tags': quote.css('div.tags a.tag::text').extract(),
        #     }
