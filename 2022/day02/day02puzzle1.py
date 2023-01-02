points = {'X': 1, 'Y': 2, 'Z': 3}
move_map = {'A': 'X', 'B': 'Y', 'C': 'Z'}

def score(play):
        sco = points[play[-1]]
        if play in ['A X', 'B Y', 'C Z']:
                return 3 + sco
        if play in ['C X', 'A Y', 'B Z']:
                return 6 + sco
        return sco

def convert_part2(s):
        # X lose, Y draw, Z win
        tokens = s.split()
        a, result = tokens[0], tokens[1]
        if result == 'X':
                if a == 'A':
                        my_move = 'Z'
                elif a == 'B':
                        my_move = 'X'
                elif a == 'C':
                        my_move = 'Y'
        if result == 'Y':
                my_move = move_map[a]
        if result == 'Z':
                if a == 'A':
                        my_move = 'Y'
                elif a == 'B':
                        my_move = 'Z'
                elif a == 'C':
                        my_move = 'X'
        return a + ' ' + my_move


def process_file(fname):
        score_part1 = 0
        score_part2 = 0
        cnt = 0
        f = open(fname)
        print(f'processing file: {fname}')
        for line in f:
                line = line.strip()
                score_part1 += score(line)
                line = convert_part2(line)
                score_part2 += score(line)
                cnt += 1
        print(f'Total score part 1: {score_part1}, from {cnt} plays')
        print(f'Total score part 2: {score_part2}, from {cnt} plays')

process_file('input1sample.txt')
process_file('input1.txt')
