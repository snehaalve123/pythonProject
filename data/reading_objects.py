import xlrd

path = r'C:\Users\sneha\PycharmProjects\SeleniumProject\data\locators.xls'

def reading_locators():
    workbook_obj = xlrd.open_workbook(path)
    worksheet_obj = workbook_obj.sheet_by_name('Sheet1')

    rows = worksheet_obj.get_rows()
    print(rows)
    header = next(rows)

    return { row[0].value: (row[1].value, row[2].value) for row in rows}

print(reading_locators())