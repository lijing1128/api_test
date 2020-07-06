__author__ = '10639'
import unittest
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./")

f = open("report.html",'wb')

HTMLTestRunner(stream=f,title="创建人群",description="测试描述",tester="静静").run(suite)

f.close()
