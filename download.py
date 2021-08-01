import pymysql
import os

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


def down(link):
  try:
    com = "you-get -o H:\youget  " + link
    os.system(com)
  except Exception as e:
    print(e)

def set_one(id):
  sql = "UPDATE link SET download = 1 WHERE id = '{0}'".format(id)
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
  down(tup[1])
  set_one(tup[0])
  tup = get_one()