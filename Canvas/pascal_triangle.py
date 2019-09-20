"""
    Given numRows, generate the first numRows of Pascal’s triangle.
    Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
    Example:
    Given numRows = 5,
    Return
    [
         [1],
         [1,1],
         [1,2,1],
         [1,3,3,1],
         [1,4,6,4,1]
    ]

"""

generate_triangle(num_of_rows):
    """ Generate pascal triangle based on """
    A = []
    row = 0
    column = 0

    while num_of_rows != 0:

        try:
            A[row][column] = A[row-1][column-1] + A[row-1][column]

        except:
            A[row][column] = 1

        num_of_rows -= 1


    return A


if __name__ == "__main__":
    print(generate_triangle(5))
