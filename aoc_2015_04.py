from mrm.util import md5sum

with open('data/aoc-2015-04.txt', encoding = 'utf-8') as f:
    dat = [x.strip('\n') for x in f.readlines()]

def compute(num_zeros):
    start_match = '0' * num_zeros
    key = dat[0]
    idx = 0
    while True:
        digest = md5sum(key + str(idx))
        if digest.startswith(start_match):
            return idx
        idx += 1

def part1(output = True):
    return compute(5)

def part2(output = True):
    return compute(6)

if __name__ == '__main__':
    print('Part 1:', part1(True))
    print('Part 2:', part2(True))
