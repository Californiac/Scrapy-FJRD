# -*- coding: utf-8 -*

# From Yue
import scrapy
from urllib.parse import urljoin
from FJYA.items import FjyaItem


class FJYASpider(scrapy.Spider):
    name = 'fjdb'
    allowed_domains = ['http://www.fjrd.gov.cn']
    start_urls = ['http://www.fjrd.gov.cn/admin/dbcx.jsp']

    def parse(self, response):
        page_list = response.xpath('/html/body//div[@class="list_seli"]/ul//li/a/@href').extract()
        response.xpath('/html/title/text()').extract()
        response.xpath('').extract()
        response.xpath('').extract()
        response.xpath('').extract()
        response.xpath('//*[@id="personnelSearchDiv"]/div/div[2]/ul//li/a/@href').extract()
        response.xpath('/html/body/div/div/div[2]/ul/li[2]/a').extract()

        for page in page_list:
            url = urljoin('http://www.fjrd.gov.cn', page)
        yield scrapy.Request(url=url, dont_filter=True, callback=self.parse_detail)


    # Extracting the information we want from each YA.
    def parse_detail(self, response):
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
