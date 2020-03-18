#coding:utf-8
import xlrd
import xlwt
#封装操作excel的方法
class Excel_option():
    def read_excel(filename,index):
        testDataPath = filename
        xls = xlrd.open_workbook(testDataPath)
        sheet = xls.sheet_by_index(index)
        data_dic = {}
        for i in range(sheet.ncols):
            data = []
            for j in range(sheet.nrows):
                if j == 0:
                    continue
                else:
                    data.append(sheet.row_values(j)[i])
            data_dic[i] = data
            print(data_dic)
        return data_dic

