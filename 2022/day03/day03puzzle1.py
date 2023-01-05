def priority(x):
        if 'a' <= x <= 'z':
                return ord(x) - 96
        if 'A' <= x <= 'Z':
                return ord(x) - 64 + 26

def find_error(items):
        l = int(len(items)/2)
        left, right = set(items[:l]), set(items[l:])
        return left.intersection(right).pop()

s1, s2, s3 = None, None, None
def process_line_part2(l):
        global s1, s2, s3
        lset = set(l)
        score = 0
        if s1 is None:
                s1 = lset
        elif s2 is None:
                s2 = lset
        elif s3 is None:
                s3 = lset

        if s1 is not None and s2 is not None and s3 is not None:
                score = priority(s1.intersection(s2).intersection(s3).pop())
                s1, s2, s3 = None, None, None
        return score

def priority_total(fileName):
        f = open(fileName)
        score_part1 = 0
        score_part2 = 0
        for line in f:
                line = line.strip()
                score_part1 += priority(find_error(line))
                score_part2 += process_line_part2(line)
        print(f'For file: {fileName}, priority total for part 1 is {score_part1}')
        print(f'For file: {fileName}, priority total for part 2 is {score_part2}')

priority_total("input1sample.txt")
priority_total("input1.txt")
