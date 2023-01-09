class Dir:
        def __init__(self, name, parent):
                self.name = name
                self.size = 0
                self.parent = parent
                self.dirs = {}
                self.files = {}
        
        def add_dir(self, name):
                self.dirs[name] = Dir(name, self.name)
        
        def add_file(self, name, size):
                self.files[name] = size
                self.add_size(size)
        
        def add_size(self, size):
                self.size += size
                if self.parent is not None:
                        self.parent.add_size(size)

def print_tree(dir, indent):
        if dir.name == '/':
                print(f'/  ({dir.size})')
        else:
                print((indent - 1)*' ', f'{dir.name}/  ({dir.size})')
        for f in dir.files:
                print(indent*' ', f'{f}  ({dir.files[f]})')
        for d in dir.dirs:
                print_tree(dir.dirs[d], indent + 1)

def dir_sum_under100k(dir):
        sum = 0
        for d in dir.dirs:
                s = dir.dirs[d].size
                if s <= 100000:
                        sum += s
                sum += dir_sum_under100k(dir.dirs[d])
        return sum

def dir_sizes(dir):
        sizes = [dir.size]
        for d in dir.dirs:
                sizes.extend(dir_sizes(dir.dirs[d]))
        return sizes

def process_file(fname):
        f = open(fname)
        root = Dir('/', None)
        pwd = root
        for line in f:
                line = line.strip()
                # handle cd
                if line.startswith('$ cd '):
                        cd_to = line[5:]
                        if cd_to == '/':
                                pwd = root
                        elif cd_to == '..':
                                if pwd.parent is None:
                                        print(f'already in root!')
                                else:
                                        pwd = pwd.parent
                        else:
                                pwd = pwd.dirs[cd_to]
                # nothing to handle in ls!
                elif line == '$ ls':
                        pass
                # create dir
                elif line.startswith('dir '):
                        dir_name = line[4:]
                        pwd.dirs[dir_name] = Dir(dir_name, pwd)
                # create file
                else:
                        size, name = line.split()
                        pwd.add_file(name, int(size))
        
        # print_tree(root, 0)
        # part 1
        print(f'Part 1: The sum of under100k for file: {fname} is {dir_sum_under100k(root)}')

        # part 2
        sizes = dir_sizes(root)
        sizes.sort()
        delete_size = 0
        for s in sizes:
                delete_size = s
                remaining = 70000000 - (root.size - s)
                if remaining >= 30000000:
                        break
        print(f'Part 2: Delete folder size = {delete_size}')

process_file('input1sample.txt')
process_file('input1.txt')
