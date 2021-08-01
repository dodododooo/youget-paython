import pymysql
import os
import time
import hashlib

conn = pymysql.connect(host='127.0.0.1', port=3306, db='youget', user='root', password='123')

def get_one():
  sql = "SELECT id,link FROM link WHERE download = 0"
  try:
    with conn.cursor() as cursor:
      cursor.execute(sql)
      select_result = cursor.fetchone()
      return select_result
  except Exception as e:
    print(e)


def down(link, id):
  try:
    s = str(id) + link
    md5 = hashlib.md5(s.encode("utf-8")).hexdigest()
    com = "you-get -f -o H:\youget -O " + md5 + " " + link
    os.system(com)
  except Exception as e:
    print(e)

def set_one(link):
  sql = "UPDATE link SET download = 1 WHERE link = '{0}'".format(link)
  try:
    with conn.cursor() as cursor:
      cursor.execute(sql)
    conn.commit()
  except Exception as e:
    print(e)
    conn.rollback()

tup = get_one()
while tup:
  print(tup)
  down(tup[1], tup[0])
  set_one(tup[1])
  time.sleep(1)
  tup = get_one()