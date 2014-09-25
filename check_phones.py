# -*- coding: utf-8 -*-

phone_list = raw_input().split()

count= 0

for phone in phone_list:
  numbers = phone.split()[0]

  increment = 0

  if not(numbers[0]==numbers[5]):

    n = int(numbers[0])

    increment = 1

    total = n

    for i in range(1,6):
      current = int(numbers[i])

      total = total + int(current)

      if (n == current):
        increment = 0

      n = current

    if (total % 2 != 0):
      increment = 0

    if (increment == 1):
      print(numbers)

  count= count + increment

print count
