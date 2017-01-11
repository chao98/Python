import xlwings as xw


def markdup(sht):
    sht.activate()
    row, col = 2, 2
    v = sht.range(row, col).value

    while v is not None:
        j = row + 1
        vv = sht.range(j, col).value
        while vv is not None:
            if vv == v:
                sht.range(j, col+1).value = v
            j += 1
            vv = sht.range(j, col).value
        row += 1
        v = sht.range(row, col).value

    return


def findtr(sht, row, col, key):
    v = sht.range(row, col).value

    while v is not None:
        if v == key:
            return row
        row += 1
        v = sht.range(row, col).value

    return


def copydate(srcsht, tgtsht):
    srow, scol = 2, 8
    trow, tcol = 2, 3
    sv = srcsht.range(srow, scol).value
    tr = srcsht.range(srow, scol-7).value

    while tr is not None:
        prow = findtr(tgtsht, trow, tcol-1, tr)
        if prow is not None:
            tgtsht.range(prow, tcol).value = sv
        else:
            print('R{} not found {}!'.format(srow, tr))
        srow += 1
        sv = srcsht.range(srow, scol).value
        tr = srcsht.range(srow, scol-7).value

    # tgtsht.range(trow, tcol).value = sv


def main():
    srcfile = r'2016 Customer TR FST.xlsx'
    wb = xw.Book(srcfile)
    sht = wb.sheets('Raw')
    # markdup(sht)
    srcsht = wb.sheets('Date')
    copydate(srcsht, sht)


if __name__ == '__main__':
    main()