import scrapy
from ..items import CnblogspiderItem
from scrapy import Selector

class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    offset = 2
    baseURL = "https://www.cnblogs.com/qiyeboy/default.html?page="
    # baseUrl = "https://www.cnblogs.com/qiyeboy/default.html?page="
    start_urls = [
            # "http://www.cnblogs.com/qiyeboy/default.html?page=",
            # https://www.cnblogs.com/qiyeboy/default.html?page=2",
            baseURL + str(offset)
    ]
    def parse(self, response):
        print("start to crawl data!!")
        papers = response.xpath(".//*[@class='day']")
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            # yield "the all content is ", [url, title, time, content]
            print(url, time, title, content)
            item = CnblogspiderItem(url=url, title=title, time=time, content=content)
            yield item
        # 根据xpath动态获取url，进行多个页面爬取
        next_page = Selector(response).xpath('//div[@id="homepage1_HomePageDays_homepage_bottom_pager"]/div[@class="pager"][1]/a[8]/@href').extract()[0]
        # 第一种爬取方式：静态爬取
        # if self.offset < 7:
        #    self.offset += 1
        #    next_page = self.baseURL + str(self.offset)
        if next_page:
            print("start to get next_page", next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
