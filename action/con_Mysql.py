#encoding:utf-8

import pymysql
import logging
logging.basicConfig(level=logging.DEBUG , filename='log.txt',filemode='a+',format=('%(asctime)s - %(name)s - %(filename)s -%(levelname)s -  %(message)s'))

from VarConfig import *

class con_Mysql():
    def __init__(self,sql='',tuple = ()):
        self.connect = pymysql.connect(host = host,user =user,password = password,db = database,port = 3306,charset='utf8mb4',cursorclass = pymysql.cursors.DictCursor)
        self.sql = sql
        self.tuple = tuple


    def select_sql(self):#执行查询语句，返回查询结果
        try:
            with self.connect.cursor() as self.cursor:
                self.cursor.execute(self.sql)
                logging.info('execute sql : '+str(self.sql))
                result = self.cursor.fetchall()
                logging.info('sql_result:'+str(result))
                return result
        except Exception as e:
            logging.info('select_sql-----error is ' + str(e))

    def change_data(self):#执行新增、删除、更新操作
        try:
            with self.connect.cursor() as self.cursor:
                if len(self.tuple) == 0:
                    self.cursor.execute(self.sql)
                else:
                    self.cursor.execute(self.sql,self.tuple)
                logging.info('execute sql: '+str(self.sql))
                self.connect.commit()
        except Exception as e:
            logging.info('change_data-----error is '+ str(e))

    def end_con(self):#关闭连接
        self.connect.close()







# sql = "SELECT household_ext_id from hydra_digital_village.t_family_information_ext where household_id in (SELECT household_id from hydra_digital_village.t_family_information where household_number = '120101000008')"
# a = con_Mysql(sql=sql)
# p = a.select_sql()
# a.end_con()
# print(p)
# print(type(p))

