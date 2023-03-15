import unittest

from old_code.Algorithms.flood_fill import FillFunctions


class TestFloodFill(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix = [[0] * 10] * 10

    def test_matrix_is_created(self):
        cls = FillFunctions(10, 10)
        self.assertIsNotNone(cls.matrix)

    def test_matrix_rows_length(self):
        cls = FillFunctions(matrix_columns=1, matrix_rows=10)
        self.assertEqual(len(cls.matrix), 10)

    # def test_matrix_columns_length(self):
    #     cls = FillFunctions(matrix_columns=10, matrix_rows=1)
    #     self.assertEqual(len(cls.matrix[0]), 10)
    #
    # def test_range_validation_column_negative(self):
    #     cls = FillFunctions(10, 10)
    #     with self.assertRaises(ValueError):
    #         cls.flood_fill(1, 1, (-1, 9))
    #
    # def test_range_validation_column_positive(self):
    #     cls = FillFunctions(10, 10)
    #     with self.assertRaises(ValueError):
    #         cls.flood_fill(1, 1, (1, 90))
    #
    # def test_range_validation_row_negative(self):
    #     cls = FillFunctions(10, 10)
    #     with self.assertRaises(ValueError):
    #         cls.flood_fill(1, 1, (1, -9))
    #
    # def test_range_validation_row_positive(self):
    #     cls = FillFunctions(10, 10)
    #     with self.assertRaises(ValueError):
    #         cls.flood_fill(1, 1, (1, 90))

#
# from pprint import pprint
#
# m = [[2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4],
#      [2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4],
#      [3, 3, 3, 1, 3, 3, 4, 1, 4, 4, 0, 4],
#      [3, 3, 1, 1, 1, 3, 1, 1, 1, 4, 4, 4],
#      [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4],
#      [3, 1, 1, 0, 0, 0, 0, 0, 1, 1, 4, 4],
#      [3, 1, 1, 0, 0, 0, 0, 0, 1, 1, 4, 4],
#      [2, 1, 1, 1, 1, 0, 0, 0, 1, 1, 2, 2],
#      [2, 1, 1, 1, 0, 0, 0, 0, 1, 2, 2, 2],
#      [2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 1, 0],
#      [2, 2, 2, 1, 1, 0, 0, 2, 2, 2, 1, 1],
#      [2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 0]
#      ]
#
# matrix = [[0] * 10] * 9
#
#
# # def flood_recursive(matrix):
# #     width = len(matrix)
# #     height = len(matrix[0])
# #
# #     def fill(x, y, start_color, color_to_update):
# #         # if the square is not the same color as the starting point
# #         if matrix[x][y] != start_color:
# #             return
# #         # if the square is not the new color
# #         elif matrix[x][y] == color_to_update:
# #             return
# #         else:
# #             # update the color of the current square to the replacement color
# #             matrix[x][y] = color_to_update
# #             neighbors = [
# #                 (x - 1, y),
# #                 (x + 1, y),
# #                 (x - 1, y - 1),
# #                 (x + 1, y + 1),
# #                 (x - 1, y + 1),
# #                 (x + 1, y - 1),
# #                 (x, y - 1),
# #                 (x, y + 1)
# #             ]
# #             for n in neighbors:
# #                 if 0 <= n[0] <= width - 1 and 0 <= n[1] <= height - 1:
# #                     fill(n[0], n[1], start_color, color_to_update)
# #
# #     start_x = 6
# #     start_y = 6
# #     start_color = matrix[start_x][start_y]
# #     fill(start_x, start_y, start_color, 9)
# #     return matrix
#
#
# def simple_flood_fill(x, y, old, new):
#     # we need the x and y of the start position, the old value,
#     # and the new value
#     # the flood fill has 4 parts
#     # firstly, make sure the x and y are inbounds
#     if x < 0 or x >= len(m[0]) or y < 0 or y >= len(m):
#         return
#     # secondly, check if the current position equals the old value
#     if m[y][x] != old:
#         return
#
#     # thirdly, set the current position to the new value
#     m[y][x] = new
#     # fourthly, attempt to fill the neighboring positions
#     simple_flood_fill(x + 1, y, old, new)
#     simple_flood_fill(x - 1, y, old, new)
#     simple_flood_fill(x, y + 1, old, new)
#     simple_flood_fill(x, y - 1, old, new)
#
#
# def flood_fill(new_color: int, target_color: int, start_node: tuple):
#     """
#
#     :param new_color:
#     :param target_color:
#     :param start_node:
#     :return:
#     """
#     """
#     if start_node is None or not in matrix
#         error
#
#     change start_node to new_color
#     check if north node is target color
#         if true call flood fill with north node as start node
#     check if east node is target color
#         if true call flood fill with east node as start node
#     check if west node is target color
#         if true call flood fill with west node as start node
#     check if south node is target color
#         if true call flood fill with south node as start node
#
#     return/ display updated matrix
#     """
#     col = len(matrix)
#     row = len(matrix[0])
#     print(start_node[0], start_node[1])
#     print(col, row)
#
#     if (start_node[0] < 0 or start_node[0] > col) or (start_node[1] < 0 or start_node[1] > row):
#         raise ValueError(f"start_node:{start_node} is out side of the matrix: C:{col}, R:{row}")
#
#
# pprint(matrix)
# print(flood_fill(1, 1, (-1, 9)))
