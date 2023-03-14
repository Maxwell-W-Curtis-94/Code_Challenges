class FillFunctions:

    def __init__(self, matrix_columns, matrix_rows):
        self.matrix = [[0] * matrix_columns] * matrix_rows  # this does not make a true 2d array the internal array is
        # duplicated not a new instance/ list  is created

    def flood_fill(self, target_color, new_color, start_location):
        col = len(self.matrix)
        row = len(self.matrix[0])
        if (start_location[0] < 0 or start_location[0] > col) or (start_location[1] < 0 or start_location[1] > row):
            return
            # raise ValueError(
            #     f"start_location:{start_location} is outside of the matrix: C:{col}, R:{row}")  # bad for recursion

        if self.matrix[start_location[0]][start_location[1]] == target_color:
            self.matrix[start_location[0]][start_location[1]] = new_color

            self.flood_fill(target_color, new_color, (start_location[0] + 1, start_location[1]))  # north
            self.flood_fill(target_color, new_color, (start_location[0] - 1, start_location[1]))  # south
            self.flood_fill(target_color, new_color, (start_location[0], start_location[1] + 1))  # east
            self.flood_fill(target_color, new_color, (start_location[0], start_location[1] - 1))  # west

        return self.matrix

    def display_matrix(self):
        for row in self.matrix:
            print(*row, sep='\t')


if __name__ == '__main__':
    cls = FillFunctions(10, 10)
    cls.display_matrix()
    cls.flood_fill(0, 1, (1, 1))
    cls.display_matrix()
