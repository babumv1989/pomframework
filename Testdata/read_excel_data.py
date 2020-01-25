import xlrd


def get_data():
    wb = xlrd.open_workbook(r"C:\Users\Personal\PycharmProjects\POM\Testdata\payee_details_sample.xlsx")
    sheet = wb.sheet_by_name("payeedetails")

    datalist = []
    for i in range(1, sheet.nrows):
        data = []
        for j in range(0, sheet.ncols):
            data.append(sheet.cell_value(i, j))
        datalist.append(data)
    return datalist
