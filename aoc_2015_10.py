with open('data/aoc-2015-10.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

def rle(s):
    res = ''
    last_c = ''
    cnt = 0
    for c in s:
        if c != last_c:
            if cnt > 0:
                res += str(cnt) + last_c
            last_c = c
            cnt = 0
        cnt += 1
    if cnt > 0:
        res += str(cnt) + last_c
    return res

def part1(output = True):
    enc = dat[0]
    for _ in range(40):
        enc = rle(enc)

    return len(enc)

def part2(output = True):
    if output:
        print(' n len')
    enc = dat[0]
    for i in range(50):
        enc = rle(enc)
        if output:
            print(f'{i:2} {len(enc)}')

    return len(enc)

if __name__ == '__main__':
    print('Part 1:', part1(True))
    print('Part 2:', part2(True))
