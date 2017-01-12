import xlwings as xw
import sys
import os
import csrreport
from datetime import datetime
from collections import namedtuple
# from enum import Enum


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


def builddatamatrix(rawsht):
    rawdata = []
    CSRtemplate = namedtuple('CSRdata', ['Num', 'Type', 'Severity', 'Customer', 'Region', 'NodeType', 'Node',
                                     'Hot', 'Queue', 'Handler', 'TR', 'Status', 'CreateD', 'CreateT',
                                     'LS2GSD', 'LS2GST', 'GS2LSD', 'Cause', 'CSRV', 'DurD', 'DurWaitTD',
                                     'IA', 'RSTV', 'RSTPD', 'RSTTgtD',	'TotalH', 'LSHrs', 'GSHrs',
                                     'RSTPonTgtV'])
    endrow = firstline(rawsht)
    endcol = firstcol(rawsht, 1)
    for i in range(2, endrow):
        csrdata = []
        # endcol = firstcol(rawsht, i)
        for j in range(1, endcol):
            csrdata.append(rawsht.range(i, j).value)
        # print(csrdata)
        rawdata.append(CSRtemplate(*csrdata))

    return rawdata


def buildtrendreq(sht):
    reqpos = namedtuple('req', ['In', 'Out', 'Open', 'BDC', 'BMC', 'Low', 'Medium',
                             'High', 'Hot', 'Emergency', 'Consultation', 'Internal',
                             'Problem', 'Project', 'Total'])
    monthpos = namedtuple('month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                                 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    row, col = 2, 2
    endrow = firstline(sht, value='Total') + 1
    endcol = firstcol(sht, value='Dec') + 1
    r = list(range(row, endrow))
    c = list(range(col, endcol))
    return reqpos(*r), monthpos(*c)


def trendanalyse(sht, rawdata, reqpos, monthpos):
    sht.activate()
    YEAR = datetime.now().year
    # YEAR = 2016
    for rowdata in rawdata:
        if rowdata.CreateD.year == YEAR:
            month = rowdata.CreateD.month - 1
            csrreport.trend_check_items['Total'][month] += 1

            if rowdata.Queue != r'Not assigned':
                csrreport.trend_check_items['In'][month] += 1

                severity = rowdata.Severity
                csrreport.trend_check_items[severity][month] += 1

                csrtype = rowdata.Type
                if csrtype in ['Consultation', 'Internal', 'Problem', 'Project']:
                    csrreport.trend_check_items[csrtype][month] += 1

                nodetype = rowdata.NodeType
                if 'DELIVERY' in nodetype:
                    csrreport.trend_check_items['BDC'][month] += 1
                else:
                    csrreport.trend_check_items['BMC'][month] += 1

                if rowdata.GS2LSD != None:
                    csrreport.trend_check_items['Out'][month] += 1
                else:
                    csrreport.trend_check_items['Open'][month] += 1

    for k, v in csrreport.trend_check_items.items():
        # print('\t', k, ' = ', v)
        row = csrreport.trend_required_analysis_row[k]
        for col in range(2, 14):
            sht.range(row, col).value = v[col-2]


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
        print(datetime.now(), ': Get file/sheet handler!')
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
        print(datetime.now(), ': Copy sht done!')

        rawdata = builddatamatrix(TGTSHT)
        print(datetime.now(), ': Extract rawdata done!')

        reqpos, monthpos = buildtrendreq(TRDSHT)
        print(datetime.now(), ': Get trend sheet format!')

        trendanalyse(TRDSHT, rawdata, reqpos, monthpos)
        print(datetime.now(), ': Fill in trend sheet done!')
        TGTWB.save()

    except myErr as err:
        log('', err.args)


if __name__ == '__main__':
    targetfile = 'CP201701.xlsm'
    main(targetfile)
