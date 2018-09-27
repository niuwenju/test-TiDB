# _*_ coding: utf-8 _*_
import MySQLdb
import threading
import time


# 创建一个表用于测试增量同步数据
# conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
# conn.autocommit(True)
# cur = conn.cursor()
# cur.execute("use test_TiDB;create table test(id VARCHAR(40) NOT NULL,time VARCHAR(256) NOT NULL,PRIMARY KEY ( id ))ENGINE=InnoDB DEFAULT CHARSET=utf8;")
# cur.close()

#单线程添加表
# conn = MySQLdb.connect(host='10.0.5.107', user='root', passwd='its7888$', port=4000)
# conn.autocommit(True)
# number = 10000
# for i in range(number):
#     cur = conn.cursor()
#     ct = time.time()
#     local_time = time.localtime(ct)
#     data_head = time.strftime("%H_%M_%S", local_time)
#     data_secs = (ct - int(ct)) * 1000
#     time_stamp = "%s_%03d" % (data_head, data_secs)
#     cur.execute('use testtable1;create table ' + 'time_' + str(i) + '_' + str(
#         time_stamp) + '(tutorial_id INT NOT NULL AUTO_INCREMENT,PRIMARY KEY ( tutorial_id ));')
#     cur.close()

#多线程添加表
# def do(id,num):
#     conn = MySQLdb.connect(host='10.0.5.107', user='root', passwd='its7888$', port=4000)
#     conn.autocommit(True)
#     a = range(num)
#     for i in a[id*len(a)/10:(id+1)*len(a)/10]:
#         cur = conn.cursor()
#         ct = time.time()
#         local_time = time.localtime(ct)
#         data_head = time.strftime("%H_%M_%S", local_time)
#         data_secs = (ct - int(ct)) * 1000
#         time_stamp = "%s_%03d" % (data_head, data_secs)
#         cur.execute('use testtable1;create table ' + 'time_' + str(i) + '_' + str(
#             time_stamp) + '(tutorial_id INT NOT NULL AUTO_INCREMENT,PRIMARY KEY ( tutorial_id ));')
#         cur.close()
#
# thread = 10
# number = 10000
# for i in range(thread):
#     t = threading.Thread(target=do,args=(i,number))
#     t.start()

#单线程添加数据（一次1条）
# conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
# conn.autocommit(True)
# number = 50000
# for i in range(number):
#     cur = conn.cursor()
#     ct = time.time()
#     local_time = time.localtime(ct)
#     data_head = time.strftime("%H:%M:%S", local_time)
#     data_secs = (ct - int(ct)) * 1000
#     time_stamp = "%s.%03d" % (data_head, data_secs)
#     sql = 'use test_TiDB;INSERT INTO test(id,time) VALUES (' + str(i) + ',' + "\'" + time_stamp + "\'" + ');'
#     try:
#         # 执行sql语句
#         cur.execute(sql)
#         cur.close()
#         # 提交到数据库执行
#         conn.commit()
#     except:
#         # Rollback in case there is any error
#         conn.rollback()

#单线程添加数据（一次10条）
# conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
# conn.autocommit(True)
# number = 50000
# for i in range(number):
#     cur = conn.cursor()
#     ct = time.time()
#     local_time = time.localtime(ct)
#     data_head = time.strftime("%H:%M:%S", local_time)
#     data_secs = (ct - int(ct)) * 1000
#     time_stamp = "%s.%03d" % (data_head, data_secs)
#     sql = 'use test_TiDB;INSERT INTO test(id,time) VALUES (' + str(i*10) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+1) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+2) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+3) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+4) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+5) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+6) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+7) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+8) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+9) + ',' + "\'" + time_stamp + "\'" + ');'
#     # print(sql)
#     try:
#         # 执行sql语句
#         cur.execute(sql)
#         cur.close()
#         # 提交到数据库执行
#         conn.commit()
#     except:
#         # Rollback in case there is any error
#         conn.rollback()

#多线程添加数据(一次1条）
# def do(id,num):
#     conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
#     conn.autocommit(True)
#     a = range(num)
#     for i in a[id*len(a)/10:(id+1)*len(a)/10]:
#         cur = conn.cursor()
#         ct = time.time()
#         local_time = time.localtime(ct)
#         data_head = time.strftime("%H:%M:%S", local_time)
#         data_secs = (ct - int(ct)) * 1000
#         time_stamp = "%s.%03d" % (data_head, data_secs)
#         sql = 'use test_TiDB;INSERT INTO test(id,time) VALUES (' + str(i) + ',' + "\'" + time_stamp + "\'" + ');'
#         try:
#             # 执行sql语句
#             cur.execute(sql)
#             cur.close()
#             # 提交到数据库执行
#             conn.commit()
#         except:
#             # Rollback in case there is any error
#             conn.rollback()
#
# thread = 10
# number = 10000
# for i in range(10):
#     t = threading.Thread(target=do,args=(i,number))
#     t.start()

#多线程添加数据(一次10条）
# def do(id,num):
#     conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
#     conn.autocommit(True)
#     a = range(num)
#     for i in a[id*len(a)/10:(id+1)*len(a)/10]:
#         cur = conn.cursor()
#         ct = time.time()
#         local_time = time.localtime(ct)
#         data_head = time.strftime("%H:%M:%S", local_time)
#         data_secs = (ct - int(ct)) * 1000
#         time_stamp = "%s.%03d" % (data_head, data_secs)
#         sql = 'use test_TiDB;INSERT INTO test(id,time) VALUES (' + str(i*10) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+1) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+2) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+3) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+4) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+5) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+6) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+7) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+8) + ',' + "\'" + time_stamp + "\'" + '),(' + str(i*10+9) + ',' + "\'" + time_stamp + "\'" + ');'
#         # print(sql)
#         try:
#             # 执行sql语句
#             cur.execute(sql)
#             cur.close()
#             # 提交到数据库执行
#             conn.commit()
#         except:
#             # Rollback in case there is any error
#             conn.rollback()
#
# thread = 10
# number = 10000
# for i in range(10):
#     t = threading.Thread(target=do,args=(i,number))
#     t.start()