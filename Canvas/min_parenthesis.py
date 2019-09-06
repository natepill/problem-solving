# def minAddToMakeValid(S):
#
#   stack = []
#   counter = 0
#
#   for char in S:
#     print("char:", char)
#     if char == '(':
#       print("HELLO")
#       stack.append(char)
#     elif char == ')':
#       try:
#         stack.pop()
#       except:
#         counter += 1
#         continue
#     else:
#         continue
#
#     print(stack)

    # return counter+len(stack)



sampleInput = '((('
# print(minAddToMakeValid(sampleInput))



def minAddToMakeValid(S):
    stack = []
    counter = 0
    for char in S:
        if char == '(':
            stack.append(char)
            print(stack)
        elif char == ')':
            try:
                stack.pop()
            except:
                counter += 1
                continue
        else:
            continue

    return counter + len(stack)

print(minAddToMakeValid(sampleInput))
