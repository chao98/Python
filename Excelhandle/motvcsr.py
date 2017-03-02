import xlwings as xw
from pandas import DataFrame
from collections import namedtuple
from datetime import datetime

area = namedtuple('area', ['r1', 'c1', 'r2', 'c2'])


def _get_time():
    datefmt = '%Y-%m-%d'
    timefmt = '%H:%M:%S'
    now = datetime.now()
    date = now.strftime(datefmt)
    time = now.strftime(timefmt)
    return date, time


def _get_sheet(name):
    # to_wb = xw.Book.caller()
    to_wb = xw.Book('Customer Perception - 201702.xlsm')
    config_sheet = to_wb.sheets['config']

    start_row, start_col = 0, 0     # $A$1
    end_row, end_col = 8, 2         # $B$7, note, the value should be +1 larger
    df = DataFrame(config_sheet[start_row:end_row, start_col:end_col].value,
                   columns=['name', 'result'])
    df.set_index(keys=df.name, inplace=True)
    if name == 'Source':
        from_wb = xw.Book(*df[df.name == 'Input'].result.values)
        sheet = from_wb.sheets(*df[df.name == name].result.values)
    else:
        sheet = to_wb.sheets(*df[df.name == name].result.values)
    return sheet


def _get_sheet_size(sheet, row_offset=0, col_offset=0):
    start_row, start_col = 0 + row_offset, 0 + col_offset
    origin_position = chr(ord('A') + start_col) + str(start_row+1)

    end_col = sheet.range(origin_position).end('right').column
    end_row = sheet.range(origin_position).end('down').row
    return start_row, start_col, end_row, end_col


def _create_df(sheet, start_row, start_col, end_row, end_col, reindex=False):
    df = DataFrame(sheet[start_row+1:end_row, start_col:end_col].value,
                   columns=sheet[start_row, start_col:end_col].value)
    if reindex:
        df.set_index(keys=df.iloc[:, 0], inplace=True)
    return df


def _log(logsheet, msg, prefix=''):
    date, time = _get_time()
    col = 1
    if logsheet:
        log_area = area(*_get_sheet_size(logsheet))
        row = log_area.r2 + 1
        logsheet.range(row, col).value = date
        logsheet.range(row, col+1).value = time
        logsheet.range(row, col+2).value = msg
    return


def import_csr_data():
    from_sheet = _get_sheet('Source')
    area1 = area(*_get_sheet_size(from_sheet, 0, 1))
    df1 = _create_df(from_sheet, *area1, reindex=True)

    raw_sheet = _get_sheet('Raw')
    area2 = area(*_get_sheet_size(raw_sheet, 0, 0))
    df2 = _create_df(raw_sheet, *area2, reindex=True)

    log_sheet = _get_sheet('Log')
    try:
        start_index_df1 = df1.index.get_loc(df2.iloc[-1, 0]) + 1
        end_index_df1 = df1.shape[0] + 1
        if start_index_df1 + 1 < end_index_df1:
            start_row = area2.r2
            start_col = area2.c1
            raw_sheet[start_row, start_col].value = df1.iloc[start_index_df1:end_index_df1].values
            msg = 'Successfully copied %d lines of data!' % (end_index_df1 - start_index_df1 - 1)
        else:
            raise KeyError
    except KeyError:
        msg = 'No new data copied!'

    _log(log_sheet, msg)


def main():
    import_csr_data()


if __name__ == '__main__':
    main()