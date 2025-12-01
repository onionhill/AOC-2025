with open('input.txt', 'r') as file:
    lines = file.readlines()

dial_value = 50
part1 = 0
part2 = 0

for line in lines:
  dir = line[0]
  steps = int(line[1:].strip())
  if dir == 'L':
    if dial_value > 0 and dial_value <= steps:
      part2 += 1
    dial_value -= steps
    if dial_value <= 0:
      part2 += -dial_value // 100
  else:
    dial_value += steps
    if dial_value >= 100:
      part2 += dial_value // 100

  dial_value %= 100
  if dial_value == 0:
    part1 += 1


print(f"Part 1: Hit the 0 dial {part1} number of times")
print(f"Part 2: Hit the 0 dial {part2} number of times")
