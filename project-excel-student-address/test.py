
import xlwt
import xlrd
from xlutils.copy import copy

def updateExcel( row, col, value,url,  sheet = 0 ):
    # load excel file
    rb = xlrd.open_workbook(
        filename=url)

    # open workbook
    wb = copy(rb)

    # modify the desired cell
    w_sheet = wb.get_sheet(sheet)
    w_sheet.write(row, col, value)

    # save the file
    wb.save(url)

# updateExcel(0, 3, "Hello World")

