with open('input.txt', 'r') as file:
  grid = [list(line.strip()) for line in file.readlines()]

max_y= len(grid)
max_x = len(grid[0])

directions = [(-1, -1), (-1, 0), (-1, 1), 
              (0, -1), (0, 1), 
              (1, -1), (1, 0), (1, 1)
]

def check_pos(grid, y, x):
  count = 0
  for dy, dx in directions:
    if 0 <= y + dy < max_y and 0 <= x + dx < max_x and grid[y + dy][x + dx] == '@':
      count += 1
  return count

def check_grid():
  count = 0
  rolls_cords =  []
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == '@':
        adjacent_rolls = check_pos(grid, y, x)
        if adjacent_rolls < 4:
          count += 1
          rolls_cords.append( (y,x) )
  return count, rolls_cords  

def update_grid(cords):
  for y,x in cords:
    grid[y][x] = 'X'
        

current_count, rolls_cords = check_grid()
total_count = current_count

print(f"Part 1: Accessible rolls: {total_count}")

update_grid(rolls_cords)
while( current_count > 0):
  current_count, rolls_cords = check_grid()
  update_grid(rolls_cords)
  total_count += current_count


print(f"Part 2: Accessible rolls: {total_count}")
update_grid(rolls_cords)



