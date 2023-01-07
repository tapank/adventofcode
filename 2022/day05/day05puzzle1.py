import re
import copy

def parse_starting_stacks(f):
        stacks = {}
        for line in f:
                line = line.rstrip()
                if '[' in line:
                        stack_num = 0
                        for i in range(1, len(line), 4):
                                stack_num += 1
                                if stack_num not in stacks:
                                        stacks[stack_num] = []
                                if line[i] != ' ':
                                        stacks[stack_num].append(line[i])
                elif '1' in line:
                        break
        for k in stacks:
                stacks[k].reverse()
        return stacks

def process_file(fname):
        f = open(fname)
        stack_count = 0
        starting_stack_count = 0
        stacks_part1 = parse_starting_stacks(f)
        stacks_part2 = copy.deepcopy(stacks_part1)
        # print('initial state:', stacks_part1)
        moves = 0
        bad_moves = 0
        for mv in f:
                if mv.strip() == '':
                        continue
                moves += 1
                tokens = re.findall(r'\d+', mv)
                if len(tokens) != 3:
                        print(f'problem with the move command. found: {mv}')
                        bad_moves += 1
                        continue
                crate_count, from_stack, to_stack = int(tokens[0]), int(tokens[1]), int(tokens[2])
                if len(stacks_part1[from_stack]) < crate_count:
                        print('Not enough crates to move! Stopped processing.')
                        break
                else:
                        for i in range(crate_count):
                                stacks_part1[to_stack].append(stacks_part1[from_stack].pop())

                        # print('crate count', crate_count, 'from', from_stack, 'to', to_stack)
                        leave_crates = stacks_part2[from_stack][:-crate_count]
                        mv_crates = stacks_part2[from_stack][-crate_count:]
                        # print('leave:', leave_crates, 'move', mv_crates)
                        stacks_part2[from_stack] = leave_crates
                        new_stack = stacks_part2[to_stack] + mv_crates 
                        stacks_part2[to_stack] = new_stack
                        # print(f'Current state of stack after move "{mv.strip()}" is {stacks_part2}')
        result_part1 = ''
        result_part2 = ''
        print('final state part 1:', stacks_part1)
        print('final state part 2:', stacks_part2)
        for i in range(1, len(stacks_part1) + 1):
                result_part1 += stacks_part1[i].pop()
                result_part2 += stacks_part2[i].pop()
        print(f'Made {moves} moves with {bad_moves} bad moves. Result part 1: {result_part1}, part 2: {result_part2}')

process_file('input1sample.txt')
process_file('input1.txt')
