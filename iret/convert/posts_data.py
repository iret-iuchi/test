# coding: utf-8

import pymysql.cursors
from delete_tags import MyHtmlStripper


conn = pymysql.connect(host='localhost',
                    user='iuchi',
                    db='cloudbreakdb',
                    password='iuchi',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = "SELECT post_content FROM wp_posts ORDER BY ID DESC LIMIT 10 "
        cursor.execute(sql)
        result = cursor.fetchall()
        print(MyHtmlStripper(str(result)).value)

finally:
    conn.close()




