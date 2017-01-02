# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from collections import deque


class QQStockOwner(object):
    def __init__(self):
        self.__table = ['报告期', '股东总数', '人均持股(股)', '总股本(万股)', '流通股本(万股)']
        self.__in_match = deque([], maxlen=5)

    def ismatch(self):
        if len(self.__table) != len(self.__in_match):
            return False
        for i in range(5):
            if self.__table[i] != self.__in_match[i]:
                return False
        return True

    def add(self, data):
        self.__in_match.append(data)
        #print(self.__in_match)

    def get(self):
        return list(self.__in_match)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super.__init__()
        self.__qqstockown = QQStockOwner()

    def handle_starttag(self, tag, attrs):
        #print('<%s>' % tag)
        pass

    def handle_endtag(self, tag):
        #print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
        #print('<start & end tag: %s/>' % tag)
        pass

    def handle_data(self, data):
        if isinstance(data, str):
            data = data.strip()
            if data is not '':
                print('data: ', data)
                self.__qqstockown.add(data)
                #print(qq_stock_owner.get())
                if self.__qqstockown.ismatch():
                    print('Matched!')

    def handle_comment(self, data):
        #print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        #print('&%s;' % name)
        pass

    def handle_charref(self, name):
        #print('&#%s;' % name)
        pass


def try_sample(n):
    if n == 1:
        parser = MyHTMLParser()
        html = r'''<html>
<head></head>
<body>
<!-- test html parser -->
<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>
'''
        parser.feed(html)

    if n == 2:
        file_name = r'600518.htm'
        with open(file_name) as f:
            html = f.read()
            parser = MyHTMLParser()
            parser.feed(html)


def main():
    try_sample(2)


if __name__ == '__main__':
    main()