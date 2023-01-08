def first_marker(s, l):
        buffer = []
        for i, ch in enumerate(s):
                buffer.append(ch)
                if len(buffer) > l:
                        buffer.pop(0)
                if len(set(buffer)) == l:
                        return i + 1
        return -1

def process_file(fname):
        f = open(fname)
        for line in f:
                line = line.strip()
                print(f'The first marker for file {fname} is at {first_marker(line, 4)}')
                print(f'The first message for file {fname} is at {first_marker(line, 14)}')

process_file('input1sample.txt')
process_file('input1.txt')