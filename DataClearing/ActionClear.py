# -*- coding=utf-8 -*-
import MySQLdb
import pandas as pd

class ActionClear():
    def __init__(self, filePath):
        self.filepath = filePath
        try:
            self.actionData = pd.read_csv(filepath_or_buffer=self.filepath, encoding="utf-8")
        except IOError:
            print "File %r can't read." % self.filepath


    def ActionFileClear(self, dbname, tableName):
        dbConnection = MySQLdb.connect(host="localhost", user="root", passwd="1234", db=dbname,charset="utf8")
        cursor = dbConnection.cursor()
        sqlBeg = "insert into " + tableName + " values ("
        sqlEnd = "\' );"
        for aIndex, aRow in self.actionData.iterrows():
            print aIndex
            aModelId = aRow["model_id"]
            aType = aRow["type"]
            if aModelId is None and aType.__eq__(6):
                self.actionData.drop(aIndex)
                continue

            if aModelId is None:
                aModelId = "0"
            aUser = aRow["user_id"]
            sSkuId = aRow["sku_id"]
            adt = aRow["time"]
            aCate = aRow["cate"]
            aBrand = aRow["brand"]
            sql = sqlBeg + "\'"+ str(aUser) + "\',\'" + str(sSkuId) + "\',\'" + adt + "\',\'" + str(aModelId) + "\',\'" + str(aType) + "\',\'" + str(aCate) + "\',\'" + str(aBrand) + sqlEnd
            cursor.execute(sql)
            cursor.nextset()

        cursor.close()
        dbConnection.commit()
        dbConnection.close()

if __name__ == '__main__':
    ac = ActionClear("F:\jdata\JData\JData_Action_201604.csv")
    ac.ActionFileClear(dbname="jdata", tableName="action4")

    ac2 = ActionClear("F:\jdata\JData\JData_Action_201603.csv")
    ac2.ActionFileClear(dbname="jdata", tableName="action3")