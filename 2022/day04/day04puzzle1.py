def validate_tuple(tu):
        return len(tu) == 2 and tu[0] <= tu[1]

def parse_tuples(line):
        tokens = line.replace(',', '-').split('-')
        nums = [int(i) for i in tokens]
        t1, t2 = (nums[0], nums[1]), (nums[2], nums[3])
        if not validate_tuple(t1) or not validate_tuple(t2):
                print('Invalid tuple in this pair: ', t1, t2)
                return (0, 0), (0, 0), False
        return t1, t2, True

def within(tu1, tu2):
        return (tu1[0] <= tu2[0] and tu1[1] >= tu2[1]) or \
                (tu1[0] >= tu2[0] and tu1[1] <= tu2[1])

def overlaps(tu1, tu2):
        return within(tu1, tu2) or (tu2[0] <= tu1[0] <= tu2[1]) or (tu2[0] <= tu1[1] <= tu2[1])

def process_file(fname):
        line_count = 0
        within_count = 0
        overlap_count = 0
        f = open(fname)
        for line in f:
                line_count += 1
                tup1, tup2, ok = parse_tuples(line)
                if ok:
                        within_count += 1 if within(tup1, tup2) else 0
                        overlap_count += 1 if overlaps(tup1, tup2) else 0
        print(f'Processed file: {fname} with {line_count} lines and found {within_count} entries which are subsets of each other')
        print(f'Processed file: {fname} with {line_count} lines and found {overlap_count} entries which are overlapping')

process_file('input1sample.txt')
process_file('input1.txt')
