
user_number = input("Find out your numbers divisors")
# user_number = 12
list_of_divisors = list()

for number in range(int(user_number/2), 0, -1):
  if user_number % number == 0:
      list_of_divisors.append(number)

print(list_of_divisors)
