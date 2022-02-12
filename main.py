import random

ask = int(input("How many sets? "))
print()
for i in range(ask):
  listNum = []
  while len(listNum) != 6:
    rand = random.randint(1, 49)
    if rand not in listNum:
        listNum.append(rand)
  listNum.sort()
  print(i+1,">", listNum)
  print()
