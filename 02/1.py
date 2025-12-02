def is_double_substring(s: str) -> bool:
  if len(s) % 2 != 0:
    return False
  mid = len(s) // 2
  return s[:mid] ==  s[mid:]

def is_made_of_substrings(s: str) -> bool:
  n = len(s)
  if n == 0:
    return False
  # Only loop over half the string.
  for size in range(1, n // 2 + 1):
    # Can the string be split into equal parts
    if n % size == 0:
      # First substring
      sub = s[:size] 
      # Repeats substring n times to get the correct length and compare to the start string
      if sub * (n // size) == s: 
        return True
  return False

with open('input.txt', 'r') as file:
  content = file.read()
  parts = content.split(',')

part1 = 0
part2 = 0

for part in parts:
  numbs = part.split('-')
  n1 = int(numbs[0])
  n2 = int(numbs[1])
  for i in range(n1, n2+1):
    if is_double_substring(str(i)):
      part1 += i
    if is_made_of_substrings(str(i)):
      part2 += i

print("Part 1:", part1)
print("Part 2:", part2)