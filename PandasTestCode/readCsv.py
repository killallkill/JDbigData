# -*- coding=utf-8 -*-
import datetime, time
import pandas as pd
import re


class GetCSV():

    def readCSV(self):
        resultData = pd.read_csv(filepath_or_buffer="F:\jdata\JData\JData_Product.csv", encoding="utf-8")
        for index, row in resultData.iterrows():
            print "-----------row %i -----------" % index
            for col_name in resultData.columns:
                print "col name %s  col value %d" % (col_name, row[col_name])
            print "-----------end row-----------"

    def getUser(self):
        uData = pd.read_csv(filepath_or_buffer="F:\jdata\JData\JData_User.csv",encoding="gbk")
        for index, row in uData.iterrows():
            print "--------row %d--------" % index
            dt = row["user_reg_tm"]
            t = time.strptime(dt, "%Y-%m-%d")
            y, m, d = t[:3]
            dt1 = datetime.date(y, m, d).strftime("%Y%m%d")
            print dt1
            for col in uData.columns:
                '''
                if col.__eq__("age"):
                    numPatten = re.compile("\d{0,2}-\d{0,2} | \d{0,2}")
                    reResult = re.findall(numPatten, row[col].encode("utf-8"))
                    print reResult
                '''



            print "------end row %d------" % index

if __name__ == "__main__":
    csvObj = GetCSV()
    csvObj.getUser()

