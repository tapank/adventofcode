def process_file(fname):
        f = open(fname)
        last = 0
        x = 1
        step = 0
        line_num = 0
        score = 0
        checkpoints = [220, 180, 140, 100, 60, 20]
        display = ['.' for i in range(240)]
        for line in f:
                line_num += 1
                tokens =  line.split()
                l = len(tokens)
                last = 0
                if l == 2:
                        val = tokens[1]
                        last = int(val)    
                        if (step)%40 in [x-1, x, x+1]:
                                display[step] = '#'
                        if (step+1)%40 in [x-1, x, x+1]:
                                display[step+1] = '#'
                        x += last
                        step += 2
                elif l == 1:
                        if (step)%40 in [x-1, x, x+1]:
                                display[step] = '#'
                        step += 1
                else:
                        print(f'Expecting one or two tokens, but got this: "{line.strip()}"')
                if len(checkpoints) > 0 and step >= checkpoints[-1]:
                        cp = checkpoints.pop()
                        score += (x - last) * cp
        print(f'Part one: File {fname} -- score {score}')
        print_display(display)

def print_display(d):
        for i in range(0, 240, 40):
                print(' '.join(d[i:i+40]))

process_file('input1sample.txt')
process_file('input1.txt')
