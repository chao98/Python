import xlwings as xw

def shtActive(sht):
    sht.activate()
    print('WBook name is: {}'.format(sht.book.name))
    print('Sheet name is: {}'.format(sht.name))

    rng = sht.cells
    #print('Sheet column is: {}'.format(rng.column))
    #print('Sheet size, row = {}, col = {}'.format(rng.last_cell.row, rng.last_cell.column))

    lastrowaddr = sht.range('A1').end('down').get_address()
    print('Sheet last row address is: {}'.format(lastrowaddr))
    rowNum = lastrowaddr[-1]

    lastcoladdress = sht.range('A1').end('right').get_address()
    print('Sheet last col address is: {}'.format(lastcoladdress))
    colNum = lastcoladdress[1]

    rngSizeDef = 'A1'+':'+colNum+rowNum
    print('Range scope is: {}'.format(rngSizeDef))
    rng = sht.range(rngSizeDef)

    print('Sheet size is: {}'.format(rng.size))

def wbActive(wb):
    """
    Try to activate a Wb.

    :param wb:
    :return:
    """
    wb.activate(steal_focus=True)

def main():
    #app = xw.apps.active
    #print('Active app is: {}'.format(app))

    cpWb = xw.Book('CP.xlsm')
    cpSht = cpWb.sheets['Release']

    vzwWb = xw.Book('VzW.xlsx')
    wbActive(cpWb)
    shtActive(cpSht)

    #cpSht.range('A1').value = '1'
    #print('Active sheet is: {}'.format(sht))

    #rng = sht.range('A1:J5')
    #rng = sht.range('A1:D5')
    #for i in range(5):
    #    print('rng[:, 0] = {}'.format(i, rng[i, 0].value))
    #print('rng[1:3, 3:5] = {}'.format(rng[1:3, 3:5].value))
    #for elem in rng:
    #    print(elem.value)

    #rng = sht.range('A7')
    #rng.value = [['Foo 1', 'Foo 2', 'Foo 3'], [10, 20, 30]]
    #print('rng[6:8, 0:3] = {}'.format(sht.range((7,1), (8,3)).value))

    #sht.range(7,1).value = None
    #sht.range(7,1).value = [['Fool 1', 'Fool 2', 'Fool 3'], [100, 200, 300]]

    #for elem in rng:
    #    print(elem.value)

    #wb.close()
    #app.kill()

if __name__ == '__main__':
    main()

