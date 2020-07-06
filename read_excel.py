__author__ = '10639'
# 封装读取excel

import xlrd

def excel_to_list(data_file, sheet):
    data_list = []  #新建个空列表，来封装所有的额数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  #获取工作薄
    header = sh.row_values(0)  #获取标题行数据
    for i in range(1,sh.nrows):  #跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  #将标题和每行数据组装成字典
        data_list.append(d)
        return data_list  #列表嵌套字典格式，每个元素是一个字典

def get_test_data(data_list, case_name):
        for case_data in data_list:
            if case_name == case_data['case_name']:
                return case_data
if __name__ == '__main__':
    data_list = excel_to_list("test_crowd_data.xlsx","TestCrowd")   #读取excel所有数据
    case_data =get_test_data(data_list,'test_user_login') #查找用例中的名称
    print(case_data)
