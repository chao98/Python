from collections import OrderedDict

def get_input():
    n = int(input())    # number of shape groups

    shape_groups = OrderedDict()
    for i in range(n):
        m = int(input())    # number of shapes in this group

        shapes = list()
        for j in range(m):
            params = input().split()
            shapes.append(tuple(params))

        shape_groups[i] = shapes

        if i != n-1:
            input()

    return shape_groups

def ret_p_coord(p):
    x, y = [int(z) for z in p]
    return x, y, x, y

def ret_c_coord(c):
    x, y, r = [int(z) for z in c]
    return x-r, y-r, x+r, y+r

def ret_l_coord(l):
    lx, ly, tx, ty = [int(z) for z in l]
    return lx, ly, tx, ty

def calc_shape_grps(shape_grps):
    for k, v in shape_grps.items():
        print(*calc_shapes(v))

def calc_shapes(shapes):
    coords = []
    for shape in shapes:
        if shape[0] == 'p':
            coords.append(ret_p_coord(shape[1:]))
        elif shape[0] == 'c':
            coords.append(ret_c_coord(shape[1:]))
        elif shape[0] == 'l':
            coords.append(ret_l_coord(shape[1:]))

    lx, ly, tx, ty = (coords[0])
    for coord in coords:
        lx = min(lx, coord[0])
        ly = min(ly, coord[1])
        tx = max(tx, coord[2])
        ty = max(ty, coord[3])

    return lx, ly, tx, ty

def main():
    shape_grps = get_input()
    calc_shape_grps(shape_grps)

if __name__ == '__main__':
    # http://www.spoj.com/problems/HS12MBR
    main()
