def create_grids(fname):
        grid = []
        visibility = []
        f = open(fname)
        for line in f:
                line = line.strip()
                row = []
                vrow = []
                grid.append(row)
                visibility.append(vrow)
                for ch in line:
                        row.append(int(ch))
                        vrow.append(False)
        return grid, visibility

def mark_visible_l2r(grid, visiblity):
        for r, row in enumerate(grid):
                max = -1
                for c, v in enumerate(row):
                        if v > max:
                                visiblity[r][c] = True
                                max = v
                        if max == 9:
                                break

def mark_visible_r2l(grid, visiblity):
        for r, row in enumerate(grid):
                max = -1
                for i in range(len(row), 0, -1):
                        c = i-1
                        v = row[c]
                        if v > max:
                                visiblity[r][c] = True
                                max = v
                        if max == 9:
                                break

def mark_visible_t2b(grid, visiblity):
        for c in range(len(grid[0])):
                max = -1
                for r in range(len(grid)):
                        v = grid[r][c]
                        if v > max:
                                visiblity[r][c] = True
                                max = v
                        if max == 9:
                                break

def mark_visible_b2t(grid, visiblity):
        for c in range(len(grid[0])-1, -1, -1):
                max = -1
                for r in range(len(grid)-1, -1, -1):
                        v = grid[r][c]
                        if v > max:
                                visiblity[r][c] = True
                                max = v
                        if max == 9:
                                break

def count_visible(grid, visibility):
        mark_visible_l2r(grid, visibility)
        mark_visible_r2l(grid, visibility)
        mark_visible_t2b(grid, visibility)
        mark_visible_b2t(grid, visibility)
        cnt = 0
        for row in visibility:
                for v in row:
                        cnt += 1 if v else 0
        return cnt

def view_dist_r(grid, r, c):
        d = 0
        h = grid[r][c]
        for v in grid[r][c+1:]:
                d += 1
                if v >= h:
                        break
        return d

def view_dist_l(grid, r, c):
        d = 0
        h = grid[r][c]
        slice = grid[r][:c]
        slice.reverse()
        for v in slice:
                d += 1
                if v >= h:
                        break
        return d

def view_dist_u(grid, r, c):
        d = 0
        h = grid[r][c]
        for i in range(r-1, -1, -1):
                d += 1
                if grid[i][c] >= h:
                        break
        return d

def view_dist_d(grid, r, c):
        d = 0
        h = grid[r][c]
        for i in range(r+1, len(grid)):
                d += 1
                if grid[i][c] >= h:
                        break
        return d

def visibility_score(grid):
        max_vscore = 0
        for r, row in enumerate(grid):
                for c, v in enumerate(row):
                        udist = view_dist_u(grid, r, c)
                        ldist = view_dist_l(grid, r, c)
                        ddist = view_dist_d(grid, r, c)
                        rdist = view_dist_r(grid, r, c)
                        vscore = rdist * ldist * udist * ddist
                        # print(v, (r, c), udist, ldist, ddist, rdist, '=', vscore)
                        if vscore > max_vscore:
                                max_vscore = vscore
        return max_vscore

def process_file(fname):
        grid, visibility = create_grids(fname)
        print(f'Trees visible for input file {fname} are {count_visible(grid, visibility)}')
        print(f'Tree with max visibility score for input file {fname} is {visibility_score(grid)}')

process_file('input1sample.txt')
process_file('input1.txt')
