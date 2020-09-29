# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FjyaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    pub_time = scrapy.Field()
    title_full = scrapy.Field()
    title = scrapy.Field()
    ya_id = scrapy.Field()
    delegation = scrapy.Field()
    type = scrapy.Field()
    drafter = scrapy.Field()
    sponsors = scrapy.Field()
    content_main = scrapy.Field()

    department_1 = scrapy.Field()
    process_type_1 = scrapy.Field()
    reply_time_1 = scrapy.Field()
    reply_type_1 = scrapy.Field()
    content_reply_1 = scrapy.Field()
    feedback_1 = scrapy.Field()
    feedback_detail_1 = scrapy.Field()
    feedback_time_1 = scrapy.Field()

    department_2 = scrapy.Field()
    process_type_2 = scrapy.Field()
    reply_time_2 = scrapy.Field()
    reply_type_2 = scrapy.Field()
    content_reply_2 = scrapy.Field()
    feedback_2 = scrapy.Field()
    feedback_detail_2 = scrapy.Field()
    feedback_time_2 = scrapy.Field()