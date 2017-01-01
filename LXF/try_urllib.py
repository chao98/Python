from urllib import request
import json


def urlget(n, url):
    if n == 1:
        with request.urlopen(url) as f:
            data = f.read()
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            #print('Data:', data.decode('utf-8'))

        js = json.loads(data.decode('utf-8'))
        print('JSON: ', end='')
        pp_json(js)

    if n == 2:
        with request.urlopen(url) as f:
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            s = f.read().decode('GB2312')
            print('\n\nData:\n', s)

            file_name = r'600518.htm'
            with open(file_name, 'w') as ff:
                ff.write(s)
    if n == 3:
        with request.urlopen(url) as f:
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            s = f.read()

            file_name = r'StockAList.htm'
            with open(file_name, 'wb') as ff:
                ff.write(s)


def pp_json(js, sort=True, indents=4):
    if type(js) is str:
        print(json.dumps(json.loads(js), ensure_ascii=False, sort_keys=sort, indent=indents))
    else:
        print(json.dumps(js, ensure_ascii=False, sort_keys=sort, indent=indents))
    return None


def main():
    url1 = r'https://api.douban.com/v2/book/2129650'
    #urlget(1, url1)
    url2 = r'http://stock.finance.qq.com/corp1/stk_holder_count.php?zqdm=600518'
    urlget(3, url2)
    url3 = r'http://quote.eastmoney.com/stocklist.html'
    #urlget(3, url3)


if __name__ == '__main__':
    main()