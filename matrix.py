
matrix = [[1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]]

regular_list = [1,2,3]
# print(matrix[1][2])

# for i in matrix:
#   for x in
rows = len(matrix)
print(rows)
columns = len(matrix[0])

# for row in matrix:
#     for column in row:
#         print(column)
# # for row_index in range(0, rows):
#   # for column in rows[]:
#
# for row_index in range(0, rows):
#     for column_index in range(0, columns):
#         print(matrix[row_index][column_index])


def left_diagonal(matrix):
    left_diagonal_list = list()
    row_counter = 0
    column_counter = 0
    while row_counter < rows:
        print(row_counter)
        left_diagonal_list.append((matrix[row_counter][row_counter]))
        row_counter += 1
    return left_diagonal_list

def right_diagonal(matrix):
    right_diagonal_list = list()
    row_counter = 0
    column_counter = len(matrix) - 1
    while row_counter < rows:
        right_diagonal_list.append((matrix[row_counter][column_counter]))
        row_counter += 1
        column_counter -1
    return right_diagonal_list



left_diagonal = sum(left_diagonal(matrix))
right_diagonal = sum(right_diagonal(matrix))

absolute_difference = abs(left_diagonal - right_diagonal)
print(absolute_difference)
