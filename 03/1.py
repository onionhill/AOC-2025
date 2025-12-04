with open('sample.txt', 'r') as file:
  banks = file.readlines()
sum = 0

for bank in banks:
  bank = bank.strip()
  highest_number = 0
  second_number = 0
  for i in range(len(bank)):
    if int(bank[i]) > highest_number and i+1 < len(bank):
      highest_number = int(bank[i])
      second_number = int(bank[i+1])
    elif int(bank[i]) > second_number:
      second_number = int(bank[i])
  sum += int(str(highest_number)+str(second_number))
print(sum)