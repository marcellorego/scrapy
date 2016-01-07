from scrapy.spiders import Spider
from scrapy.selector import Selector
from g1.items import G1Item
from g1.aggregates import G1AggregatedItem

class G1Spider(Spider):
    name = "g1"
    allowed_domains = ["g1.globo.com"]
    start_urls = [
        "http://g1.globo.com/index.html"
    ]

    def parse(self, response):
        sel = Selector(response)
        feeds = sel.xpath('//span[contains(@class, "feed-text-wrapper")]')

        items = []
        for feed in feeds:
            item = G1Item()
            section = feed.xpath('span[contains(@class, "feed-post-header")]/a[contains(@class, "feed-post-header-chapeu")]')
            item['section'] = section.xpath('text()').extract()
            item['section_link'] = section.xpath('@href').extract()

            link = feed.xpath('a[contains(@class, "feed-post-link")]')
            item['link'] = link.xpath('@href').extract()
            item['title'] = link.xpath('p[contains(@class, "feed-post-body-title")]/text()').extract()
            item['resume'] = link.xpath('p[contains(@class, "feed-post-body-resumo")]/text()').extract()

            aggregator = feed.xpath('div[contains(@class, "aggregator")]/ul[contains(@class, "aggregated-items")]/li')
            item['aggregated'] = []

            for aggregated in aggregator:
                aggr = G1AggregatedItem()
                aggr['link'] = aggregated.xpath('a/@href').extract()
                aggr['title'] = aggregated.xpath('a/p[contains(@class, "aggregated-item-text")]/text()').extract()
                item['aggregated'].append(aggr)

            items.append(item)
        return items