import xlwings as xw
import sys
import os
from datetime import datetime


class myErr(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def gettime():
    datefmt = '%Y-%m-%d'
    timefmt = '%H:%M:%S'
    now = datetime.now()
    date = now.strftime(datefmt)
    time = now.strftime(timefmt)
    return date, time


def firstline(sht, col=1, value=None, offset=0):
    row = 1 + offset
    # print('firstline, value=', value)
    v = sht.range(row, col).options(empty=None).value
    while v != value:
        # print('firstline, v=', v)
        row += 1
        v = sht.range(row, col).options(empty=None).value
    return row


def firstcol(sht, row=1, value=None, offset=0):
    col = 1 + offset
    v = sht.range(row, col).value
    while v != value:
        col += 1
        v = sht.range(row, col).value
    return col


def log(logsht, msg):
    # logsht.activate()
    date, time = gettime()
    col = 1
    if logsht:
        row = firstline(logsht)
        logsht.range(row, col).value = date
        logsht.range(row, col+1).value = time
        logsht.range(row, col+2).value = msg
    else:
        print('{0}, {1}, {2}'.format(date, time, msg))


def getwbs(target):
    if target and os.path.isfile(target):
        tgtwb = xw.Book(target)
        tgtconfsht = tgtwb.sheets('config')

        params = {'tgtwb': tgtwb, 'srcwb': ''}

        row, col = 1, 1
        v = tgtconfsht.range(row, col).value
        while v:
            params[v] = tgtconfsht.range(row, col + 1).value
            row += 1
            v = tgtconfsht.range(row, col).value
    else:
        raise myErr('Target file does not exist!')

    source = params['Input file:']
    if source and os.path.isfile(source):
        srcwb = xw.Book(source)
        params['srcwb'] = srcwb
        k = 'Source sht:'
        if k in params:
            params[k] = srcwb.sheets(params[k])
    else:
        raise myErr('Source file does not exist!')

    for k, v in params.items():
        if 'Target' in k and 'sht' in k:
            params[k] = tgtwb.sheets(v)

    return params


def copyrow(SRCSHT, TGTSHT, row):
    offset = 0
    if SRCSHT.name == 'MOTV':
        offset = 1
    endcol = firstcol(SRCSHT, row=row, offset=offset)
    for i in range(1+offset, endcol):
        TGTSHT.range(row, i-1).value = SRCSHT.range(row, i).value


def copysht(SRCSHT, TGTSHT, LOGSHT):
    if SRCSHT and TGTSHT and LOGSHT:
        TGTSHT.activate()
        trow = firstline(TGTSHT)
        if trow > 2:
            latestCSR = TGTSHT.range(trow-1, 1).value
            # print(latestCSR)
            sstartrow = firstline(SRCSHT, value=latestCSR, col=2)
        else:
            sstartrow = 1
        sendrow = firstline(SRCSHT, col=2)
        # print(sstartrow, sendrow)

        for i in range(sstartrow+1, sendrow):
            copyrow(SRCSHT, TGTSHT, i)

        log(LOGSHT, 'Successfully copied {} CSRs.'.format(sendrow-sstartrow-1))
    else:
        raise myErr('in copydata, passing in not defined sht: ' + SRCSHT + TGTSHT + LOGSHT)


def main(targetfile):
    if len(sys.argv) <= 1:
        print('No input, use default file: ', targetfile)
    elif len(sys.argv) == 2:
        targetfile = sys.argv[1]
    else:
        print('Wrong cmd line!')
        print('cmd line: motvdata.py input.[xls|xlsm|xlsx]')
        exit()

    try:
        params = getwbs(targetfile)
        # print(params)
        SRCSHT = params['Source sht:']
        TGTSHT = params['Target sht:']
        TRDSHT = params['Target Trend sht:']
        STASHT = params['Target Sta sht:']
        LOGSHT = params['Target Log sht:']
        YEAR = params['Year:']
        TGTWB = params['tgtwb']

        log(LOGSHT, 'found both source and target files.')
        copysht(SRCSHT, TGTSHT, LOGSHT)
        TGTWB.save()

    except myErr as err:
        log('', err.args)


if __name__ == '__main__':
    targetfile = 'CP201701.xlsm'
    main(targetfile)
