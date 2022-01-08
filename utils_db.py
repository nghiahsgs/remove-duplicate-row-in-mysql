from peewee import *
import requests
import json
import datetime


host='89.40.0.146'
db_name = 'user_fb'
db_user='nghiahsgs4'
db_pass='261997'

db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)

class User_info(Model):
    uid = CharField()
    # name = CharField()
    # birthday = DateField()
    # avatar = CharField()
    class Meta:
        database=db

if __name__=="__main__":
    # User_info.create_table()
    pass