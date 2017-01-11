import json


def get_stklst(fn, p):
    stk = []
    with open(fn, 'r') as f:
        for line in f:
            dummy = line.split('\t')
            if len(dummy) >= 3:
                sid, name, increase, price, *left = dummy
                if sid is not None and sid.isdigit():
                    # print(sid, price)
                    if isinstance(price, str):
                        price = price.strip()
                    if price == '--':
                        price = 0
                    price = float(price)
                    if 0 < price <= p:
                        stk.append(sid)
    return stk


def get_owners(file):
    with open(file, 'r') as f:
        owners = json.load(f)
    return owners


def check_update_15(share_list):
    for value in share_list:
        if '-15'in value[0] and '2016-' in value[0]:
            return True
    return False


def extract_update_15(stk, owners):
    update_every_15 = []
    for sid in stk:
        # print(sid)
        if sid in owners:
            share_change_info = owners[sid]
            if check_update_15(share_change_info):
                update_every_15.append(sid)
    return update_every_15


def save_stk(ofile, update_15):
    with open(ofile, 'w') as f:
        json.dump(update_15, f, indent=2)


def main():
    stklistfile = 'stk_list.txt'
    stkownerfile = 'jqowners.txt'
    outfile = 'u15.txt'

    stk = get_stklst(stklistfile, 300)
    owners = get_owners(stkownerfile)
    update_15 = extract_update_15(stk, owners)
    print(len(update_15), update_15)
    save_stk(outfile, update_15)

if __name__ == '__main__':
    main()