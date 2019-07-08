# -*- coding: utf-8 -*-
import json
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CnblogsspiderPipeline(object):
    def __init__(self):
        self.file = open("paper.json", "w")
    def process_item(self, item, spider):
        if item["title"]:
            line = json.dumps(dict(item), ensure_ascii=False) + ", \n"
            self.file.write(line)
        else:
            raise DropItem("Missing title in %s "% item)
        return item
    
    def close_spider(self, spider):
        self.file.close()


