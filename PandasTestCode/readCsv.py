# -*- coding=utf-8 -*-

import pandas as pd

class GetCSV():

    def readCSV(self):
        resultData = pd.read_csv(filepath_or_buffer="F:\jdata\JData\JData_Product.csv", encoding="utf-8")
        for index, row in resultData.iterrows():
            print "-----------row %i -----------" % index
            for col_name in resultData.columns:
                print "col name %s  col value %d" % (col_name, row[col_name])
            print "-----------end row-----------"



if __name__ == "__main__":
    csvObj = GetCSV()
    csvObj.readCSV()

