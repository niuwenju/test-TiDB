# _*_ coding: utf-8 _*_
import MySQLdb
import time


#查询数据
def test():
    conn = MySQLdb.connect(host='10.0.5.107', user='root', passwd='its7888$', port=4000)
    conn.autocommit(True)
    # a = cur.execute("use test_TiDB;select * from test where id = 49999;")
    timee = None
    number = 500000L
    while timee == None:
        cur = conn.cursor()
        cur.execute("use test_TiDB;select count(*) as value from test;")
        result = cur.fetchall()
        if result != ((number,),):
            timee = None
        else:
            ct = time.time()
            local_time = time.localtime(ct)
            data_head = time.strftime("%H:%M:%S", local_time)
            data_secs = (ct - int(ct)) * 1000
            timee = "%s.%03d" % (data_head, data_secs)
        cur.close()
    conn.commit()
    return timee

print(test())
