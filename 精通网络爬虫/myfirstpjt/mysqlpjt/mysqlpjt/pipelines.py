# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MysqlpjtPipeline(object):

    def __init__(self):
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="mypydb", charset='utf8')
        #数据库想存汉字一定要设置为nchar，不要用书里面的char，也可以直接在连接中设置charset为utf8（不是utf-8），这样就不要
        # 改pymysql下面的connections.py了，具体改为：
        # def __init__(self, host="localhost", user=None, passwd="",
        #              db=None, port=3306, unix_socket=None,
        #              charset='utf8', sql_mode=None,
        #              read_default_file=None, conv=decoders, use_unicode=None,
        #              client_flag=0, cursorclass=Cursor, init_command=None,
        #              connect_timeout=None, ssl=None, read_default_group=None,
        #              compress=None, named_pipe=None):

    def process_item(self, item, spider):
        name = str(item["name"][0])
        key = str(item["keywd"][0])
        sql = "insert into mytb(title,keywd) VALUES(\""+str(name)+"\",\""+str(key)+"\")"
        self.conn.query(sql)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()