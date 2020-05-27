#!/usr/bin/python3
# encoding:utf-8

import pymysql

db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db='speders')
cursor=db.cursor()
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}

table ='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))

sql='insert into {table} ({keys}) values ({values}) on duplicate key update'.format(table=table,keys=keys,values=values)
update=','.join(["{keys}=%s".format(key=key) for key in data])
sql+=update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print("successful")
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()


