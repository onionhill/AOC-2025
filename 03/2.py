
with open('input.txt', 'r') as file:
  banks = file.readlines()

total = 0

for bank in banks:
  bank = bank.strip()

  result = ""
  l = 12
  remaining_chars = len(bank)

  for i, digit in enumerate(bank):
    if l == 0:
      break
    chars_left = remaining_chars - i
    if chars_left == l:
      result += bank[i:]
      break
    can_skip = chars_left - l
    # Find the best digit in the range we can skip forward to.
    best_digit_ahead = max(bank[i:i+can_skip+1])
    if digit == best_digit_ahead:
      result += digit
      l -= 1
  total += int(result)

print(f"Total: {total}")