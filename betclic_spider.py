# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from tutorial.items import BetclicItem

class BetclicSpider(scrapy.Spider):
    name = "betclic"
    allowed_domains = ["betclic.fr"]
    start_urls = [
        "https://www.betclic.fr/football/ligue-1-e4",
    ]

    def parse(self, response):
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        for day in response.xpath('.//div[@class="entry day-entry grid-9 nm"]'):
            print day.xpath('.//time/@datetime').extract()
            for hour in day.xpath('.//div[@class="schedule clearfix"]'):
                print hour.xpath('.//div[@class="hour"]/text()').extract()
                for game in hour.xpath('.//div[@class="match-entry clearfix CompetitionEvtSpe "]'):
                    print game.xpath('.//div[@class="match-name"]/a/text()').extract()
                    print game.xpath('.//div[@class="match-odd"]/span/text()').extract()
            print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            


# response.xpath('//div/@data-track-event-name').extract()
#         print sel.xpath('.//div/@data-track-event-name').extract()
# entry day-entry grid-9 nm
# schedule clearfix
# "match-entry clearfix CompetitionEvtSpe "
# match-odds
     #  print response.__class__
      # print sel.__class__
      # for i in range(1,6):
      #      match = sel[i].xpath('//div/@data-track-event-name').extract()
      #    
  #      match = sel.xpath('//div/@data-track-event-name').extract()
   #     print match
