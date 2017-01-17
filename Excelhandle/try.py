import pprint
from collections import defaultdict
from collections import OrderedDict


NODETYPE = ['BDC14A', 'BMC14A', 'BDC15A', 'BMC15A', 'BMC15B', 'BDC16B', 'BMC16B']
CUSTOMER = ['VzW', 'Telstra', 'TIM', 'ATT', 'TMO']

# class ElemData(object):
#     def __init__(self, data):

pp = pprint.PrettyPrinter(indent=2)

def innerdict():
    ddict = defaultdict(dict)
    ddict['1'] = 1
    ddict['2']['2'] = 2

    # dddict = defaultdict(defaultdict(dict))
    # dddict['3']['2']['3'] = 3
    pp.pprint(ddict)

    x = lambda: defaultdict(x)
    template = ['CSR', 'Tier2', 'PROB', 'FAULT', 'EMER']

    mx = x()

    for i in NODETYPE:
        for j in CUSTOMER:
            mx[i][j] = OrderedDict().fromkeys(template, 0)
    # d = dict().fromkeys(template, [])
    # print(d)
    if not mx['BDC14A']['Vzz']:
        mx['BDC14A']['Vzz'] = 10
    pp.pprint(mx)


def try_reduce():
    pass


def main():
    # innerdict()
    try_reduce()

if __name__ == '__main__':
    main()