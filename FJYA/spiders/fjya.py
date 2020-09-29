# -*- coding: utf-8 -*

# From Yue
import scrapy
from urllib.parse import urljoin
from FJYA.items import FjyaItem


class FJYASpider(scrapy.Spider):
    name = 'fjya'
    allowed_domains = ['http://www.fjrd.gov.cn']
    start_urls = ['http://www.fjrd.gov.cn/ct/1166-155490']

    # Extracting the information we want from each YA.
    def parse(self, response):
        item = FjyaItem()
        item['link'] = response.url
        item['pub_time'] = response.xpath('//div[@class="detail_title"]/p/text()').extract()
        item['title_full'] = response.xpath('//div[@class="detail_title"]/h3/text()').extract()
        item['title'] = response.xpath('//div[@class="detail_con"]/table[1]/tr[2]/td/text()').extract()
        item['ya_id'] = response.xpath('//div[@class="detail_con"]/table[1]/tr[3]/td[2]/text()').extract()
        item['delegation'] = response.xpath('//div[@class="detail_con"]/table[1]/tr[4]/td[1]/text()').extract()
        item['type'] = response.xpath('//div[@class="detail_con"]/table[1]/tr[4]/td[2]/text()').extract()
        item['drafter'] = response.xpath('//div[@class="detail_con"]/table[1]/tr[5]/td/text()').extract()
        item['sponsors'] = response.xpath('//div[@class="detail_con"]/table[1]/tr[6]/td/text()').extract()
        item['content_main'] = response.xpath('//div[@class="detail_con"]/table[1]/tr[7]/td//text()').extract()
        temp_type_1 = response.xpath('//div[@class="detail_con"]/table[2]/tr[3]/td[2]/text()').extract()

        if temp_type_1 == '独办    ' or temp_type_1 == '主办    ':
            item['department_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[3]/td[1]/text()').extract()
            item['process_type_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[3]/td[2]/text()').extract()
            item['reply_time_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[4]/td[1]/text()').extract()
            item['reply_type_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[4]/td[2]/text()').extract()
            item['content_reply_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[5]/td[1]//text()').extract()
            item['feedback_1'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[3]/td[2]/text()').extract()
            item['feedback_detail_1'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[3]/td[3]/text()').extract()
            item['feedback_time_1'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[3]/td[4]/text()').extract()

        else:
            item['department_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[3]/td[1]/text()').extract()
            item['process_type_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[3]/td[2]/text()').extract()
            item['reply_time_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[4]/td[1]/text()').extract()
            item['reply_type_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[4]/td[2]/text()').extract()
            item['content_reply_1'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[5]/td[1]//text()').extract()
            item['feedback_1'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[3]/td[2]/text()').extract()
            item['feedback_detail_1'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[3]/td[3]/text()').extract()
            item['feedback_time_1'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[3]/td[4]/text()').extract()

            item['department_2'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[6]/td[1]/text()').extract()
            item['process_type_2'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[6]/td[2]/text()').extract()
            item['reply_time_2'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[7]/td[1]/text()').extract()
            item['reply_type_2'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[7]/td[2]/text()').extract()
            item['content_reply_2'] = response.xpath('//div[@class="detail_con"]/table[2]/tr[8]/td[1]//text()').extract()
            item['feedback_2'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[4]/td[2]/text()').extract()
            item['feedback_detail_2'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[4]/td[3]/text()').extract()
            item['feedback_time_2'] = response.xpath('//div[@class="detail_con"]/table[3]/tr[4]/td[4]/text()').extract()

        yield item

        for i in range(155490, 155500, 1):
            next_link = '/ct/1166-' + str(i)
            next_url = 'http://www.fjrd.gov.cn' + next_link
            print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)