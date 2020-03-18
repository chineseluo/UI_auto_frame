#coding:utf-8
import unittest
import os
from Reports import HTMLTestRunner
#测试的入口
def allcases():
    #case_path = os.path.join(os.getcwd())
    rule = "*case.py"
    pa = "F:\\UI_auto_project\\TestCases"
    discover = unittest.defaultTestLoader.discover(start_dir=pa,pattern=rule,top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    report_dir = "F:\\UI_auto_project\\Reports\\test_report.html"
    fp = open(report_dir,"wb")
    runCaseReport = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="输出测试用例执行结果")
    runCaseReport.run(allcases())
