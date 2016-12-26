import xlwings as xw

def copyProgress(origSht, tgtSht):
    i = 2
    progressIndex = 7
    while origSht.range(i,1).value is not None:
        try:
            #print(vzwSht.range(i, progressIndex).value)

            j = i
            while tgtSht.range(j,1).value != origSht.range(i,1).value:
                j += 1

            #tgtSht.range(j, progressIndex+1).value = origSht.range(i, progressIndex).value
            tgtSht.range(j, progressIndex+2).value = origSht.range(i, progressIndex+1).value

            i += 1
        except:
            print('Exception occurred, i = {}, j = {}'.format(i, j))
            break

def copyNodeInfo(origSht, tgtSht):
    tgtContentPos = 6
    origContentPos = 6

    tgtIndex = 2
    origIndex = 2
    while tgtSht.range(tgtIndex, 1).value is not None:
        while origSht.range(origIndex, 1).value is not None \
            and origSht.range(origIndex, 1).value != tgtSht.range(tgtIndex, 1).value:
            origIndex += 1

        tgtSht.range(tgtIndex, tgtContentPos).value = origSht.range(origIndex, origContentPos).value
        tgtIndex += 1

def copyCustomerInfo(origSht, tgtSht):
    origContentPos = 4
    tgtContentPos = 5

    customerDict = {
        'AT&T Mobility WE' : 'AT&T',
        'Germany INTERNAL' : 'Youlab',
        'Telecom Italia' : 'Tel Ita',
        'Telefonica ES' : 'Telefo',
        'Telstra Mobility (AU)' : 'Telstra',
        'TIM/Test Plant BR' : 'TIM',
        'T-Mobile Lab' : 'TMO',
        'TURKCELL TR' : 'TURKCELL',
        'Verizon Wireless HQ' : 'vzw',
        'Verizon Wireless Midwest' : 'vzw'
    }

    tgtIndex = 2
    origIndex = 2

    while tgtSht.range(tgtIndex, 1).value is not None:
        while origSht.range(origIndex, 1).value is not None \
              and origSht.range(origIndex, 1).value != tgtSht.range(tgtIndex, 1).value:
            origIndex += 1

        customerName = origSht.range(origIndex, origContentPos).value
        tgtSht.range(tgtIndex, tgtContentPos).value = customerDict[customerName]
        tgtIndex += 1

def copyTR(origSht, tgtSht):
    origContentPos = 12
    tgtContentPos = 13

    tgtIndex =2
    origIndex = 2

    while tgtSht.range(tgtIndex, 1).value is not None:
        while origSht.range(origIndex, 2).value is not None \
              and origSht.range(origIndex, 2).value != tgtSht.range(tgtIndex, 1).value:
            origIndex += 1

        csr = origSht.range(origIndex, 1).value
        tr = origSht.range(origIndex, origContentPos).value
        if tr != '#':
            tgtSht.range(tgtIndex, tgtContentPos).value = tr
            print('pos = {}, csr = {}, tr = {}'.format(tgtIndex, csr, tr))

        tgtIndex += 1

def main():
    #vzwWb = xw.Book('VzW.xlsx')
    motvWb = xw.Book('MOTV.xlsm')

    #vzwSht = vzwWb.sheets('CSR Performance')
    motvSht = motvWb.sheets('CSR Performance')

    #copyProgress(vzwSht, motvSht)

    #cpWb = xw.Book('CP.xlsm')
    #cpSht = cpWb.sheets('CSRs')

    #copyNodeInfo(cpSht, motvSht)
    #copyCustomerInfo(cpSht, motvSht)

    wkReportWb = xw.Book('2016W50.xlsx')
    wkReportSht = wkReportWb.sheets('Customer Perception')

    copyTR(wkReportSht, motvSht)

if __name__ == '__main__':
    main()

