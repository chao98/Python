import xlwings as xw
from pandas import DataFrame


def _get_sheet(name):
    # to_wb = xw.Book.caller()
    to_wb = xw.Book('Customer Perception - 201702.xlsm')
    config_sheet = to_wb.sheets['config']

    start_row, start_col = 0, 0     # $A$1
    end_row, end_col = 8, 2         # $B$7, note, the value should be +1 larger
    # df = DataFrame(config_sheet.range('A1:B7').value, columns=['name', 'value'])
    df = DataFrame(config_sheet[start_row:end_row, start_col:end_col].value,
                   columns=['name', 'result'])
    df.set_index(keys=df.name, inplace=True)

    # print(df)

    # start_row, start_col = 15-1, 1-1
    # end_row, end_col = 22-1, 2-1
    # config_sheet[start_row:end_row, start_col:end_col].value = df
    # config_sheet[start_row:end_row, start_col:end_col].value = df.values

    # pos = 'A16'
    # config_sheet.range(pos).value = df[df.name == name].result.values
    # return df[df.name == name].result.values
    if name == 'Source':
        from_wb = xw.Book(*df[df.name == 'Input'].result.values)
        sheet = from_wb.sheets(*df[df.name == name].result.values)
    else:
        sheet = to_wb.sheets(*df[df.name == name].result.values)
    return sheet


def _get_sheet_size(sheet, row_offset=0, col_offset=0):
    start_row, start_col = 0 + row_offset, 0 + col_offset
    # row_pace, col_pace = 512, 256
    # end_row, end_col = start_row + row_pace, start_col + col_pace
    origin_position = chr(ord('A') + start_col) + str(start_row+1)
    print(origin_position)

    end_col = sheet.range(origin_position).end('right').column
    end_row = sheet.range(origin_position).end('down').row
    return start_row, start_col, end_row, end_col


def import_csr_data():
    from_sheet = _get_sheet('Source')
    config_sheet = _get_sheet('Config')
    pos = 'A16'
    config_sheet.activate()
    config_sheet.range(pos).value = _get_sheet_size(from_sheet, 0, 1)


def main():
    import_csr_data()


if __name__ == '__main__':
    main()