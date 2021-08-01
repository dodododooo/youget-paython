# -*- encoding=utf8 -*-
__author__ = "gong"

from airtest.core.api import *
import pymysql
import re
auto_setup(__file__)

conn = pymysql.connect(host='127.0.0.1', port=3306, db='youget', user='root', password='123')

# wake()
# sleep(3)
keyevent("HOME")
touch(Template(r"tpl1627741942370.png", record_pos=(-0.361, -0.662), resolution=(720, 1280)))

sleep(1)

keyevent("BACK")

sleep(1)

touch(Template(r"tpl1627741989595.png", record_pos=(0.117, 0.192), resolution=(720, 1280)))
sleep(3)
# keyevent("BACK")
# sleep(2)
# touch(Template(r"tpl1627748390290.png", record_pos=(-0.008, 0.361), resolution=(720, 1280)))
n = 0
while n < 500:
    n = n + 1
    guanbi = exists(Template(r"guanbi.png"))
    if guanbi:
        print("guanbi.png")
        touch(guanbi)
    
#     if exists(Template(r"hongbao.png")):
#         print("hongbao.png")
#         keyevent("BACK")

    if exists(Template(r"zhibojieshu.png")):
        print("zhibojieshu.png")
        swipe((360, 1000), (360, 400), duration=0.1)
        continue

    if exists(Template(r"zhibo.png")):
        print("zhibo.png")
        swipe((360, 1000), (360, 400), duration=0.1)
        continue

    if exists(Template(r"zhibobaoxiang.png")):
        print("zhibaobaoxiang.png")
        swipe((360, 1000), (360, 400), duration=0.1)
        continue

    if exists(Template(r"tishi.png")):
        print("tishi.png")
        swipe((360, 1000), (360, 400), duration=0.1)
        continue
    
    touch((690,900))
    sleep(1)
    swipe((700,1200),(400,1200))

    sleep(1)
    touch((600,1120))
    sleep(3)



    linkStr = shell("am broadcast -a clipper.get")
    print(linkStr)
    link = re.search(r'https.*?\s', linkStr).group()

    addSql = 'INSERT INTO link(link) VALUES("{0}")'.format(link)
    try:
        with conn.cursor() as cursor:
            cursor.execute(addSql)
        conn.commit()
    except Exception as e:
        conn.rollback()
    sleep(3)
    swipe((360, 1000), (360, 400), duration=0.1)

    
# if exists(Template(r"zhibopk.png")):
#     print("zhibopk.png")
#     swipe((360, 1000), (360, 400), duration=0.1)

# touch(Template(r"tpl1627744991100.png", record_pos=(-0.004, 0.031), resolution=(720, 1280)))
# touch(Template(r"tpl1627745018323.png", record_pos=(-0.181, 0.386), resolution=(720, 1280)))


    
