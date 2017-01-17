import xlwings as xw
from datetime import datetime
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict


config = {'fromsheet': 'MOTV',
          'Raw': 'raw17',
          'Trend': 'trend17',
          'Statistics': 'sta17',
          'Log': 'Log'}


class CSRWorkbook(object):
    def __init__(self, filename):
        self.__workbook = xw.Book(filename)
        if not self.__workbook:
            raise CSRErr('Can not find file: {}'.format(filename))

    def workbook(self):
        return self.__workbook

    def sheet(self, sheetname):
        sheet = self.__workbook.sheets(sheetname)
        if not sheet:
            raise CSRErr('Can not find {} sheet in {}'.format(sheetname, self.__workbook))
        return sheet

    def save(self):
        self.__workbook.save()


trend_row = {'In':          2,
             'Out':         3,
             'Open':        4,
             'BDC':         5,
             'BMC':         6,
             'Low':         7,
             'Medium':      8,
             'High':        9,
             'Hot':         10,
             'Emergency':   11,
             'Consultation': 12,
             'Internal':    13,
             'Problem':     14,
             'Project':     15,
             'Total':       16}

trend_line = {'In': None,
              'Out': None,
              'Open': None,
              'BDC': None,
              'BMC': None,
              'Low': None,
              'Medium': None,
              'High': None,
              'Hot': None,
              'Emergency': None,
              'Consultation': None,
              'Internal': None,
              'Problem': None,
              'Project': None,
              'Total': None}

trend_item = OrderedDict()
for k, v in sorted(trend_row.items(), key=lambda x: x[1]):
    empty = [0 for i in range(12)]
    trend_item[k] = empty

CSRData = namedtuple('CSRData', ['Num', 'Type', 'Severity', 'Customer', 'Region', 'NodeType', 'Node',
                                 'Hot', 'Queue', 'Handler', 'TR', 'Status', 'CreateD', 'CreateT',
                                 'LS2GSD', 'LS2GST', 'GS2LSD', 'Cause', 'CSRV', 'DurD', 'DurWaitTD',
                                 'IA', 'RSTV', 'RSTPD', 'RSTTgtD',	'TotalH', 'LSHrs', 'GSHrs',
                                 'RSTPonTgtV'])


class CSRErr(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def get_time():
    datefmt = '%Y-%m-%d'
    timefmt = '%H:%M:%S'
    now = datetime.now()
    date = now.strftime(datefmt)
    time = now.strftime(timefmt)
    return date, time


def get_first_empty_row(sht, col=1, value=None, offset=0):
    row = 1 + offset
    v = sht.range(row, col).options(empty=None).value
    while v != '' and v != value:
        row += 1
        v = sht.range(row, col).options(empty=None).value
    return row


def get_first_empty_col(sht, row=1, value=None, offset=0):
    col = 2 if sht.name == 'MOTV' else 1
    v = sht.range(row, col).options(empty=None).value
    while v != '' and v != value:
        col += 1
        v = sht.range(row, col).options(empty=None).value
    return col


def log(logsheet, msg, prefix=''):
    date, time = get_time()
    col = 1
    if logsheet:
        row = get_first_empty_row(logsheet)
        logsheet.range(row, col).value = date
        logsheet.range(row, col+1).value = time
        logsheet.range(row, col+2).value = msg
    print('{0} {1}, {2}, {3}'.format(prefix, date, time, msg), flush=True)
    return


def copy_row(fromsheet, tosheet, row, startcol=1, endcol=0):
    if endcol == 0:
        endcol = get_first_empty_col(fromsheet, row=row, offset=startcol)
    # for i in range(startcol, endcol):
    #     tosheet.range(row, i-1).value = fromsheet.range(row, i).value
    if fromsheet.name == 'MOTV':
        startcol = 2
        tosheet[row-1:row, startcol-2:endcol-2].value = fromsheet[row-1:row, startcol-1:endcol-1].value
    else:
        tosheet[row-1:row, startcol-1:endcol-1].value = fromsheet[row-1:row, startcol-1:endcol-1].value


def copy_sheet(fromsheet, tosheet):
    tosheet.activate()
    # tosheet_empty_row = get_first_empty_row(tosheet)
    # col = 2 if fromsheet.name == 'MOTV' else 1
    # if tosheet_empty_row > 2:
    #     latestCSR = tosheet.range(tosheet_empty_row-1, 1).value
    #     fromsheet_startrow = get_first_empty_row(fromsheet, value=latestCSR, col=col)
    # else:
    #     fromsheet_startrow = 1
    # fromsheet_endrow = get_first_empty_row(fromsheet, col=col)
    #
    # for i in range(fromsheet_startrow+1, fromsheet_endrow):
    #     copy_row(fromsheet, tosheet, i)
    #     if (i - fromsheet_startrow - 1) % 20 == 0:
    #         log(None, 'Copied to line-{}.'.format(i), prefix='\t')

    tosheet_startrow = get_first_empty_row(tosheet)
    fromsheet_startcol = 2 if fromsheet.name == 'MOTV' else 1
    if tosheet_startrow > 2:
        latestCSR = tosheet.range(tosheet_startrow-1, 1).value
        # print('tosheet, startrow = {}, CSR = {}'.format(tosheet_startrow, latestCSR))
        fromsheet_startrow = get_first_empty_row(fromsheet, value=latestCSR, col=fromsheet_startcol) + 1
    else:
        fromsheet_startrow = 2
    fromsheet_endrow = get_first_empty_row(fromsheet, col=fromsheet_startcol) - 1
    fromsheet_endcol = get_first_empty_col(fromsheet) - 1
    # print('fromsheet, start row = {}, end row = {}'.format(fromsheet_startrow, fromsheet_endrow))
    # print('tosheet, start row = {}'.format(tosheet_startrow))
    num_copied_row = fromsheet_endrow - fromsheet_startrow + 1
    tosheet_endrow = tosheet_startrow + num_copied_row
    tosheet[tosheet_startrow-1:tosheet_endrow, 0:].value = fromsheet[fromsheet_startrow-1:fromsheet_endrow, fromsheet_startcol-1:fromsheet_endcol].value
    return num_copied_row


def build_data(sheet):
    # rawdata = []
    endrow = get_first_empty_row(sheet)
    endcol = get_first_empty_col(sheet)
    # for i in range(2, endrow):
    #     csrdata = []
    #     for j in range(1, endcol):
    #         csrdata.append(sheet.range(i, j).value)
    #     rawdata.append(CSRData(*csrdata))
    #     if (i - 2) % 50 == 0:
    #         log(None, 'Import {0:4} lines raw data into memory.'.format(i-2), prefix='\t')
    tmpdata = sheet[1:endrow-1, 0:endcol-1].value

    return [CSRData(*rowdata) for rowdata in tmpdata]


def write_row(sht, rowdata, row=2, col=1):
    start_row, end_row = row-1, row
    start_col, end_col = col-1, col+len(rowdata)-1
    sht[start_row:end_row, start_col:end_col].value = rowdata


def write_sheet(sht, datamatrix, row=2, col=1):
    row_num = len(datamatrix)
    if row_num > 0:
        col_num = len(datamatrix[0])
    else:
        col_num = 0
    start_row, end_row = row-1, row+row_num-1
    start_col, end_col = col-1, col+col_num-1
    sht[start_row:end_row, start_col:end_col].value = datamatrix


# define a multi-level dict, with default value
csr_stat_dict = lambda: defaultdict(csr_stat_dict)
csr_stat = csr_stat_dict()
stat_report_template = ['CSR', 'Tier2', 'PROB', 'FAULT', 'EMER']


