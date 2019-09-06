def last_factorial_digit(n):
  factorial = 1
  for num in range(1, n+1):
    factorial = factorial * num
    print(factorial)

  factorial = str(factorial)

  return factorial[-1]


print(last_factorial_digit(5))
