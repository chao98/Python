from itertools import combinations


def identify_block(road_with_blocks):
    block_pos = []
    for i, elem in enumerate(road_with_blocks):
        if elem == '0':
            block_pos.append(i)

    return block_pos


def split_list(alist, c):
    found = False
    start, end = -1, -1

    splitted = []
    for i, elem in enumerate(alist):
        if elem != c and found is False:
            start = i
            found = True
        if (elem == c or i == len(alist)-1) and found is True:
            '''
            if i == len(alist) - 1:
                end = i + 1
            else:
                end = i
            '''
            end = (i+1) if (i == len(alist)-1) else i
            found = False
            splitted.append(alist[start:end])

    return splitted


def road_repair(k, road_with_blocks):
    block_pos = identify_block(road_with_blocks)
    tried_repair_pos = list(combinations(block_pos, k))

    #print(tried_repair_pos)

    check_length = []
    for possible_poses in tried_repair_pos:
        tmp_road_with_blocks = road_with_blocks[:]
        for pos in possible_poses:
            tmp_road_with_blocks[pos] = '1'

        tmp_sub_roads = split_list(tmp_road_with_blocks, '0')

        max_len = len(max(*tmp_sub_roads))
        check_length.append([possible_poses, max_len])

    #return max(*[length for a, length in check_length])
    return max(*map(lambda x: x[1], check_length))

def get_input():
    t = int(input())

    roads = []
    for i in range(t):
        n, k = map(int, input().split())
        road_with_blocks = input().split()
        roads.append([(n, k), road_with_blocks])

    return roads


def main():
    roads = get_input()

    for road in roads:
        k = road[0][1]
        road_with_blocks = road[1]
        print(road_repair(k, road_with_blocks))

    return

if __name__ == '__main__':
    # http://www.spoj.com/problems/REPROAD/
    main()
