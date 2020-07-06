__author__ = '10639'
import xlrd

wb = xlrd.open_workbook("test_crowd_data.xlsx")  #打开excel
sh = wb.sheet_by_name("TestCrowd")
print(sh.nrows)
print(sh.ncols)
print(sh.cell(0,0).value)
print(sh.row_values(0))

print(dict(zip(sh.row_values(0),sh.row_values(1))))

