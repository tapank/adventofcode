max_calories = 0
top_calories = []
curr_calories = 0
elf_count = 0

def collect_calories(n):
        if len(top_calories) < 3:
                top_calories.append(n)
        elif n > top_calories[0]:
                top_calories.remove(top_calories[0])
                top_calories.append(n)
        top_calories.sort()

f = open('input1.txt')
for line in f:
        num = line.strip()
        if num != '':
                curr_calories += int(num)
        else:
                collect_calories(curr_calories)
                curr_calories = 0
                elf_count += 1
                print(f'Elf count: {elf_count}')

print(f'Max calories is: {top_calories[-1]}')
print('Top three are:', top_calories)
print(f'Sum of top 3 is: {sum(top_calories)}')
