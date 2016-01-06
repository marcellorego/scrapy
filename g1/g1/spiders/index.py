from scrapy.spiders import Spider
from scrapy.selector import Selector
from g1.items import G1Item

class G1Spider(Spider):
    name = "g1"
    allowed_domains = ["g1.globo.com"]
    start_urls = [
        "http://g1.globo.com/index.html"
    ]

    # <div class="feed-post">
    #   <div class="feed-post-body">
    #	  <a class="feed-post-figure-link gui-image-hover gui-color-primary-link">
    #	  <span class="feed-text-wrapper">
    #       <span class="feed-post-header">
    #		  <a class="feed-post-header-chapeu gui-text-section-title" href="http://g1.globo.com/sao-paulo/index.html"
    #		    <span>Sao Paulo
    #		<a href="http://g1.globo.com/sao-paulo/noticia/2016/01/camera-registra-inicio-do-fogo-que-destruiu-museu-da-lingua-portuguesa.html" class="feed-post-link gui-image-hover gui-color-primary-link">
    #		  <p class="feed-post-body-title gui-text-title gui-color-primary">Camera registra inicio do fogo que destruiu Museu da Lingua Portuguesa
    #		  <p class="feed-post-body-resumo">Suspeita e que curto-circuito ou estouro de lampada tenham iniciado chamas.
    #		  <span class="feed-post-time">
    #			<span class="feed-post-time-label">ha 1 hora
    #

    def parse(self, response):
        sel = Selector(response)
        feeds = sel.xpath('//div[@class="feed-post-body"]')
        items = []
        for feed in feeds:
        	item = G1Item()
        	item['section'] = feed.xpath('span/span/a/span/text()').extract()
        	item['section_link'] = feed.xpath('span/span/a/@href').extract()
        	item['link'] = feed.xpath('span/a/@href').extract()
        	item['title'] = feed.xpath('span/a/p[1]/text()').extract()
        	item['resume'] = feed.xpath('span/a/p[2]/text()').extract()
        	items.append(item)

        return items