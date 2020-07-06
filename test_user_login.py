__author__ = '10639'
import unittest
import requests
from read_excel import  *
import json

class TestCreatCrowd(unittest.TestCase):#类必须是Test开头，继承Testcase才能识别为用例类
    @classmethod
    def setUp(cls):
        cls.data_list = excel_to_list("test_crowd_data.xlsx","TestCrowd")  #文件名和sheet名称
        # url = 'https://yjifen.ews.m.jaeapp.com/bend/crows/save-crowds'

    def test_crowd_normal(self):
        case_data = get_test_data(self.data_list,'test_user_login')  # casename
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,data = json.loads(data))
        self.assertEqual(res.text,expect_res)
if __name__ == '__main__':
    unittest.main(verbosity=2)



#     data = '''{"name":"test113488","tag_list":{"gender":{"value":[0]}},"visitor_proportion":0,"t":1591940427196}'''
#         headers = {"Content-Type":"application/json"}
#         res = requests.post(url=self.url,data=data,headers=headers)
#         result = res.json()
#         self.assertEqual('1',result['code'])
#         print('第一条用例成功')
#     def test_crowd_wrong(self):
#         data =''' {"name":"test22f061661","tag_list":{"gender":{"value":[0]}},"visitor_proportion":0,"t":1591940427196}'''
#         headers = {"Content-Type":"application/json"}
#         res = requests.post(url=self.url,data=data,headers=headers)
#         result2=res.json()
#         self.assertEqual('300008',result2['code'])
#         print('第二条用例成功')
# if __name__ == '__main__':
#     unittest.main(verbosity=2)


