class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_locations = []

        for r_i, row in enumerate(matrix):

            for column, val in enumerate(row):

                if val == 0:
                    zero_locations.append((r_i,column))

        for row_i, column in zero_locations:
            self.set_zeros_vertical(matrix, column)
            self.set_zeros_horizontal(matrix, row_i)


    def set_zeros_vertical(self, matrix, column):

        for arr in matrix:
            arr[column] = 0

    def set_zeros_horizontal(self, matrix, row):

        matrix[row] = [0]*len(matrix[0])

            
