import xlwings as xw
from datetime import datetime
from collections import namedtuple

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


trend_item = {'In': None,
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

for k in trend_item:
    empty = [0 for i in range(12)]
    trend_item[k] = empty

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
    while v != value:
        row += 1
        v = sht.range(row, col).options(empty=None).value
    return row


def get_first_empty_col(sht, row=1, value=None, offset=0):
    col = 2 if sht.name == 'MOTV' else 1
    v = sht.range(row, col).options(empty=None).value
    while v != value:
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
    tosheet_empty_row = get_first_empty_row(tosheet)
    col = 2 if fromsheet.name == 'MOTV' else 1
    if tosheet_empty_row > 2:
        latestCSR = tosheet.range(tosheet_empty_row-1, 1).value
        fromsheet_startrow = get_first_empty_row(fromsheet, value=latestCSR, col=col)
    else:
        fromsheet_startrow = 1
    fromsheet_endrow = get_first_empty_row(fromsheet, col=col)

    for i in range(fromsheet_startrow+1, fromsheet_endrow):
        copy_row(fromsheet, tosheet, i)
        if (i - fromsheet_startrow - 1) % 20 == 0:
            log(None, 'Copied to line-{}.'.format(i), prefix='\t')


def build_data(sheet, YEAR=None):
    rawdata = []
    endrow = get_first_empty_row(sheet)
    endcol = get_first_empty_col(sheet)
    for i in range(2, endrow):
        csrdata = []
        for j in range(1, endcol):
            csrdata.append(sheet.range(i, j).value)
        rawdata.append(CSRData(*csrdata))
        if (i - 2) % 50 == 0:
            log(None, 'Import {0:4} lines raw data into memory.'.format(i-2), prefix='\t')

    return rawdata
