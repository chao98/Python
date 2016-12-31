import struct


def int_pack(n, x):
    if n == 1:
        print('Traditional way: ', end='')
        b1 = (x & 0xff000000) >> 24
        b2 = (x & 0xff0000) >> 16
        b3 = (x & 0xff00) >> 8
        b4 = (x & 0xff)
        bs = bytes([b1, b2, b3, b4])
        print(bs)

    if n == 2:
        b = struct.pack('>I', x)
        print('struct.pack (4b unsigned): ', b)

    if n == 3:
        b = struct.pack('>I', x)
        c = struct.unpack('>I', b)
        print('struct.unpack (4b unsigned): ', c)


def read_bmp_info(file_name):
    with open(file_name, 'rb') as f:
        s = f.read(30)
        fmt = r'<ccIIIIIIHH'
        c = struct.unpack(fmt, s)
        print('bmp info: ', c)


def main():
    x = 10240099
    int_pack(3, x)

    file_name = 'sample.bmp'
    read_bmp_info(file_name)


if __name__ == '__main__':
    main()