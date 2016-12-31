from __future__ import print_function
from HTMLParser import HTMLParser
from collections import OrderedDict
import sys
import os
import time
import json

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._met_date = False
        self._dict = OrderedDict()
        self._temp = ''

    def handle_starttag(self, tag, attrs):
        #print('Encountered a start tag: ', tag)
        pass

    def handle_endtag(self, tag):
        #print('Encoountered an end tag: ', tag)
        pass

    def handle_data(self, data):
        #print('Encountered some data: ', data)
        #print('Valid Date: ', is_valid_date(data))
        if is_valid_date(data) is True:
            #print(data, ', ', end='')
            self._temp = data
            self._met_date = True
        if is_valid_digits(data) is not '':
            if self._met_date == True:
                #print(is_valid_digits(data), ' | ', end='')
                self._dict[self._temp] = is_valid_digits(data)
                self._met_date = False

    def get_dict(self):
        return self._dict

def is_valid_date(s):
    try:
        time.strptime(s, '%Y-%m-%d')
        return True
    except:
        return False

def is_valid_digits(s):
    if s is not None or s is not '':
        result = s.split('.')
        if len(result) != 0:
            num = ''.join(result[0].split(','))

    if num is not None or num is not '':
        if num.isdigit() is True:
            return num
        else:
            return ''
    else:
        return ''


def simpletry(feed):
    #myDict = OrderedDict()
    parser = MyHTMLParser()
    parser.feed(feed)
    myDict = parser.get_dict()
    return myDict

def listfile(dir):
    result = []
    if dir is not '':
        filenames = os.listdir(dir)

        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext == '.html' or ext == '.htm':
                result.append(dir + '/' + filename)

    return sorted(result)

def get_stock_id(name):
    if name is not '':
        pos = name.index('.')
        return name[pos-6:pos]
    else:
        return ''

def main():
    '''
    if len(sys.argv) != 2:
        print('Wrong cmdline!')
        print('Usage: tryHtml.py [xxx.htm|dir]')
        exit(1)
    '''

    #instr = sys.argv[1]
    instr = 'examdir'
    data_dict = OrderedDict()

    if os.path.isfile(instr):
        with open(instr) as f:
            #feed = f.read()
            simpletry(f.read())
    elif os.path.isdir(instr):
        filenames = listfile(instr)
        for filename in filenames:
            with open(filename) as f:
                #print('\n', get_stock_id(filename), ':', sep='')
                #feed = f.read()
                data_dict[get_stock_id(filename)] = simpletry(f.read())
    else:
        print('Err: not valid input')
        exit(1)

    with open('examdir/stockinfo.json', 'w') as f:
        print(data_dict)
        json.dump(data_dict, f)

if __name__ == '__main__':
    main()
