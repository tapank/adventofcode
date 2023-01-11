# class Game2Knots:
#         moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#         def __init__(self):
#                 self.board = [[]]
#                 self.hx, self.hy, self.tx, self.ty = 0, 0, 0, 0
#                 self.tail_trail = set()
#                 self.tail_trail.add((self.tx, self.ty))
#                 # print('h', self.hx, self.hy)
#                 # print('t', self.tx, self.ty)
        
#         def move(self, d):
#                 dx, dy = Game2Knots.moves[d]
#                 self.hx += dx
#                 self.hy += dy
#                 # print('move', d)
#                 self.check_tail()
#                 # print('h', self.hx, self.hy)
#                 # print('t', self.tx, self.ty)
        
#         def check_tail(self):
#                 dx, dy = self.hx-self.tx, self.hy-self.ty
#                 if abs(dx) > 1 or abs(dy) > 1:
#                         if dx == 0 or dy == 0:
#                                 self.tx += int(dx/2)
#                                 self.ty += int(dy/2)
#                         else:
#                                 if dx != 0:
#                                         self.tx += 1 if dx > 0 else -1
#                                 if dy !=0:
#                                         self.ty += 1 if dy > 0 else -1
#                         self.tail_trail.add((self.tx, self.ty))
        
#         def tail_steps(self):
#                 # print(self.tail_trail)
#                 return len(self.tail_trail)

class GameNKnots:
        moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
        def __init__(self, knots):
                self.board = [[]]
                self.hx, self.hy, self.tx, self.ty = 0, 0, 0, 0
                self.pos_map = {}
                for i in range(knots):
                        self.pos_map[i] = (0, 0)
                self.tail_trail = set()
                self.tail_trail.add((self.tx, self.ty))
                # print('h', self.hx, self.hy)
                # print('t', self.tx, self.ty)
        
        def move(self, d):
                self.hx, self.hy = self.pos_map[0]
                self.tx, self.ty = self.pos_map[1]
                self.move_head(d)
                self.pos_map[0] = (self.hx, self.hy)
                self.pos_map[1] = (self.tx, self.ty)
                for i in range(1, len(self.pos_map) - 1):
                        if i < len(self.pos_map) - 1:
                                self.hx, self.hy = self.pos_map[i]
                                self.tx, self.ty = self.pos_map[i+1]
                                self.check_tail()
                                self.pos_map[i+1] = (self.tx, self.ty)
                self.tail_trail.add((self.tx, self.ty))

        def move_head(self, d):
                dx, dy = GameNKnots.moves[d]
                self.hx += dx
                self.hy += dy
                # print('move', d)
                self.check_tail()
                # print('h', self.hx, self.hy)
                # print('t', self.tx, self.ty)
        
        def check_tail(self):
                dx, dy = self.hx-self.tx, self.hy-self.ty
                if abs(dx) > 1 or abs(dy) > 1:
                        if dx == 0 or dy == 0:
                                self.tx += int(dx/2)
                                self.ty += int(dy/2)
                        else:
                                if dx != 0:
                                        self.tx += 1 if dx > 0 else -1
                                if dy !=0:
                                        self.ty += 1 if dy > 0 else -1
        
        def tail_steps(self):
                # print(self.tail_trail)
                return len(self.tail_trail)

def process_file(fname, knots):
        f = open(fname)
        game = GameNKnots(knots)
        for line in f:
                direction, count = line.split()
                count = int(count)
                for i in range(count):
                        game.move(direction)
        print(f'File: {fname}. Tail ({knots} knots) moved {game.tail_steps()} steps')

process_file('input1sample.txt', 2)
process_file('input2sample.txt', 10)
process_file('input1.txt', 10)
