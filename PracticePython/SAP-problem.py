'''
Given a matrix, of set length (3 elements an array) determine if there is a path between 2 cells. Each element in an array is a cell

We are trying to get from the starting point to the destination

'''

# 0 - Wall
# 1 - Starting point
# 2 - Desination
# 3 - Door (Can pass through)

'''
Q1: For each array of cells in the matrix, count the number of valid paths there are.

Q2: What about going backwards in the same list?

Q3: What about paths to other lists?

Q4: What if given a list of cells that are not the same size?

'''


class FindPath(object):
''' Find possible path for each array of cells '''

    def __init__(self, matrix):
        self.matrix = matrix
        self.possible_paths = 0
        self.impossible_paths = 0
        self.starting_point = None
        self.destination = None


    def isPath (self, list_of_cells):
        '''Returns a boolean if a path is present or not'''

        # I don't know wheter or not it would be more effiecent to binary search for 1 or to enumerate over the list_of_cells
            # Maybe should google if its possible to determine indexes of elements w/o enumeration over an entire list
        for index, cell in enumerate(list_of_cells):

            
            # if cell == 1:
            #     self.starting_point = (index, cell) # Will be useful if we need to find a path from one list_of_cells to another list_of_cells
            #
            #     if list_of_cells[index + 1] == 2:
            #         self.destination = (index-1, list_of_cells[index-1])
            #         return True
            #
            #     if list_of_cells[index - 1] == 2:
            #         self.destination = (index+1, list_of_cells[index+1])
            #         return True
            #
            #     if list_of_cells[index + 1] == 3:
            #         self.destination = (index-1, list_of_cells[index-1])
            #         return True
            #
            #     if list_of_cells[index - 1] == 3:
            #         self.destination = (index+1, list_of_cells[index+1])
            #         return True
            #     #This is not accounting for doors (3),






if __name__ == "__main__":
    matrix = [[0,1,2], [1,3,2], [1,0,3]]
