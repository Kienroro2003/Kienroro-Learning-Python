import pandas as pd
import xlsxwriter
import test

url = "/Users/kienroro2003/Downloads/Filemau-C1-HocSinhDiaPhuong-ver2-data (4)KHOI 3 copy 2.xls"

currentRow = -1
listColumnUpdate = {"S": "Tổ/Thôn/Xóm (Theo địa chỉ thường trú)",
                    "T": "Tỉnh/Thành phố\n(Theo quê quán)",
                    "U": "Quận/Huyện\n(Theo quê quán)",
                    "V": "Xã/Phường\n(Theo quê quán)",
                    "W": "Tổ/Thôn/Xóm (Theo quê quán)",
                    "X": "Tỉnh/Thành phố\n(Theo nơi sinh)",
                    "Y": "Quận/Huyện\n(Theo nơi sinh)",
                    "Z": "Nơi sinh chi tiết",
                    "AA": "Chỗ ở hiện nay",
                    "AB": "Số điện thoại liên hệ",
                    "BK": "Họ tên cha",
                    "BL": "Nghề nghiệp cha",
                    "BM": "Năm sinh cha",
                    "BN": "Số điện thoại cha",
                    "BO": "Họ tên mẹ",
                    "BP": "Nghề nghiệp mẹ",
                    "BQ": "Năm sinh mẹ",
                    "BR": "Số điện thoại mẹ"}

print(listColumnUpdate.keys())


def ValidateName(name):
    return name.lower()


dataframe = pd.read_excel(url)

nameSearch = input("Enter name search: ")
for index in range(len(dataframe["Họ tên"].values)):

    if ValidateName(dataframe["Họ tên"].values[index]) == ValidateName(nameSearch):
        currentRow = index

if currentRow != -1:
    for value in listColumnUpdate.values():
        valueCol = input(f"Enter {value}: ")
        col = dataframe.columns.get_loc(value)
        row = currentRow + 1
        print(col, row)
        test.updateExcel(row, col, valueCol, url)
        # print(value+": " + str(dataframe[value].values[currentRow]))
