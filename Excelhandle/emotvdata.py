import sys
import pprint
import ecsrreportconfig as cr
from datetime import datetime
from collections import OrderedDict


def trend_analyse(sht, rawdata):
    sht.activate()
    YEAR = datetime.now().year
    # YEAR = 2016
    for rowdata in rawdata:
        if rowdata.CreateD.year == YEAR:
            month = rowdata.CreateD.month - 1
            cr.trend_item['Total'][month] += 1

            if rowdata.Queue != r'Not assigned':
                cr.trend_item['In'][month] += 1

                severity = rowdata.Severity
                cr.trend_item[severity][month] += 1

                csrtype = rowdata.Type
                if csrtype in ['Consultation', 'Internal', 'Problem', 'Project']:
                    cr.trend_item[csrtype][month] += 1

                nodetype = rowdata.NodeType
                if 'DELIVERY' in nodetype:
                    cr.trend_item['BDC'][month] += 1
                else:
                    cr.trend_item['BMC'][month] += 1

                if not rowdata.GS2LSD:
                    cr.trend_item['Open'][month] += 1
                else:
                    cr.trend_item['Out'][month] += 1

    datamatrix = [v for v in cr.trend_item.values()]
    cr.write_sheet(sht, datamatrix, row=2, col=2)


def stat_analyse(sht, rawdata):
    sht.activate()
    sht.clear()
    YEAR = datetime.now().year
    # YEAR = 2016
    for rowdata in rawdata:
        if rowdata.CreateD.year == YEAR:
            if not cr.csr_stat[rowdata.Node][rowdata.Customer]:
                cr.csr_stat[rowdata.Node][rowdata.Customer] = OrderedDict().fromkeys(cr.stat_report_template, 0)
                cr.csr_stat[rowdata.Node][rowdata.Customer]['CSR'] = 1
            else:
                cr.csr_stat[rowdata.Node][rowdata.Customer]['CSR'] += 1

            if rowdata.Queue != r'Not assigned':
                cr.csr_stat[rowdata.Node][rowdata.Customer]['Tier2'] += 1

                if rowdata.Type == 'Problem':
                    cr.csr_stat[rowdata.Node][rowdata.Customer]['PROB'] += 1
                if rowdata.TR != '#':
                    cr.csr_stat[rowdata.Node][rowdata.Customer]['FAULT'] += 1
                if rowdata.Severity == 'Emergency':
                    cr.csr_stat[rowdata.Node][rowdata.Customer]['EMER'] += 1

    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(cr.csr_stat)
    stat_table = list()
    stat_table.append(['', '', *cr.stat_report_template])
    for i in cr.csr_stat:
        for j in cr.csr_stat[i]:
            node = list()
            node.extend([i, j])
            node.extend(cr.csr_stat[i][j].values())
            stat_table.append(node)
    # pp.pprint(sorted(stat_table))
    cr.write_sheet(sht, sorted(stat_table), row=1, col=1)


def main(from_file, to_file):
    l = len(sys.argv)
    if l == 1:
        pass
    elif l == 3:
        from_file = sys.argv[1]
        to_file = sys.argv[2]
    else:
        print('Wrong cmd line!')
        print('cmd line: python emotvdata.py fromfile.[xls|xlsm|xlsx] tofile.[xls|xlsm|xlsx]')
        exit()

    try:
        cr.log(None, r"Start to find/get workbooks and sheets handlers.")
        FROMWORKBOOK = cr.CSRWorkbook(from_file).workbook()
        FROMSHEET = FROMWORKBOOK.sheets(cr.config['fromsheet'])

        TOWORKBOOK = cr.CSRWorkbook(to_file).workbook()
        RAWSHEET = TOWORKBOOK.sheets(cr.config['Raw'])
        TRENDSHEET = TOWORKBOOK.sheets(cr.config['Trend'])
        STATSHEET = TOWORKBOOK.sheets(cr.config['Statistics'])
        LOGSHEET = TOWORKBOOK.sheets(cr.config['Log'])
        cr.log(LOGSHEET, r'Successfully get WB/Sheets handlers.')

        cr.log(None, r'Start to copy raw data.')
        num_copied_row = cr.copy_sheet(FROMSHEET, RAWSHEET)
        cr.log(LOGSHEET, r'Successfully copied {} lines raw data.'.format(num_copied_row))

        cr.log(None, r'Start to input rawdata to memory.')
        raw_data = cr.build_data(RAWSHEET)
        # print(raw_data[1])
        # print(raw_data[-1])
        cr.log(LOGSHEET, r'Input rawdata to memory done.')

        cr.log(None, r'Start to fill in trend sheet.')
        trend_analyse(TRENDSHEET, raw_data)
        cr.log(LOGSHEET, r'Filled in trend sheet.')

        cr.log(None, r'Start to fill in stat sheet.')
        stat_analyse(STATSHEET, raw_data)
        cr.log(LOGSHEET, r'Filled in stat sheet.')

    except cr.CSRErr as err:
        cr.log(LOGSHEET, err.args)


if __name__ == '__main__':
    from_file = 'MOTV-2017WK03.xlsx'
    to_file = 'Customer Perception - 201701.xlsm'
    main(from_file, to_file)

