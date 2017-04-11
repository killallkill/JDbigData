# -*- coding=utf-8 -*-

import pandas as pd
import numpy as np
import re
import MySQLdb
import time, datetime

class UserTableClear():

    # 初始化读取数据
    def __init__(self, path):
        try:
            self.filepath = path
            self.userData = pd.read_csv(filepath_or_buffer=self.filepath, encoding="gbk")
        except IOError:
            print "Cant read file %s" % path

    '''
    用于清洗注册日期
    '''
    def AgeClear(self):
        print "-----------user clear start----------"
        for uIndex, uRow in self.userData.iterrows():

            # 删除注册时间未知或为空或注册时间大于2016-04-15的用户
            dateData = uRow["user_reg_tm"]
            if dateData is None or dateData > u'2016-04-15':
                self.userData.drop(uIndex, inplace=True)


        print "---------user clear complete--------"
        return self.userData


    '''
    将清洗后的用户数据表放入数据库中
    '''
    def loadToDB(self, DBName, TableName):
        self.dbName = DBName
        self.tName = TableName
        connection = MySQLdb.connect(host='localhost', user='root', passwd='1234', db=self.dbName, charset='utf8')
        cursor = connection.cursor()
        sqlHead = "insert into " + self.tName + " values ("
        sqlTail = ")"
        print "------------load data to db start-----------"
        for index, uDataRow in self.userData.iterrows():
            uid = uDataRow["user_id"]
            # 截取年龄，删除字段中的年龄中文字符
            ageStr = uDataRow["age"]
            if type(ageStr) is float:
                self.userData.drop(index, inplace=True)
                continue
            xx = u'([\u4e00-\u9fa5]+)'
            patten = re.compile(xx)
            s = uDataRow["age"]
            result = re.split(patten, s)
            uage = result[0]
            usex = uDataRow["sex"]
            ulevel = uDataRow["user_lv_cd"]
            y, m, d = time.strptime(uDataRow["user_reg_tm"], "%Y-%m-%d")[:3]
            uRegDate = datetime.date(y, m, d)
            insertSql = sqlHead + '\'' + str(uid) +'\',\'' + uage + '\',\'' + str(usex) + '\',\'' + str(ulevel) + '\',\'' + str(uRegDate) +'\''+sqlTail
            cursor.execute(insertSql)
            cursor.nextset()

        cursor.close()
        connection.commit()
        connection.close()
        print "-----------load data to db complete----------"


if __name__ == '__main__':
    UserClear = UserTableClear("F:\jdata\JData\JData_User.csv")
    UserClear.AgeClear()
    UserClear.loadToDB('jdata', 'user')
