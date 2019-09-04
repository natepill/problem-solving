def minAddToMakeValid(S):
  stack = []
  counter = 0

  for char in S:
    if char == '(':
    
      stack.append(char)
    elif char == ')':
      try:
        stack.pop()
      except:
        counter += 1
        continue
    return counter+len(stack)


sampleInput = '((('
print(minAddToMakeValid(sampleInput))
