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

            print('\n\nData:\n', f.read().decode('GB2312'))


def pp_json(js, sort=True, indents=4):
    if type(js) is str:
        print(json.dumps(json.loads(js), ensure_ascii=False, sort_keys=sort, indent=indents))
    else:
        print(json.dumps(js, ensure_ascii=False, sort_keys=sort, indent=indents))
    return None


def main():
    url1 = r'https://api.douban.com/v2/book/2129650'
    url2 = r'http://stock.finance.qq.com/corp1/stk_holder_count.php?zqdm=600518'
    #urlget(1, url1)
    urlget(2, url2)

if __name__ == '__main__':
    main()