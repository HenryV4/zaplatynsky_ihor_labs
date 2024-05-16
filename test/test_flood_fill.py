import unittest

from src.flood_fill import flood_fill, read_input, write_output


class TestFloodFill(unittest.TestCase):
    def test_flood_fill_same_color(self):
        num_rows, num_columns = 4, 5
        start_row, start_column = 1, 2
        new_color = "G"
        matrix = [
            ["G", "G", "G", "G", "G"],
            ["G", "G", "G", "G", "G"],
            ["G", "G", "G", "G", "G"],
            ["G", "G", "G", "G", "G"],
        ]
        expected_matrix = [
            ["G", "G", "G", "G", "G"],
            ["G", "G", "G", "G", "G"],
            ["G", "G", "G", "G", "G"],
            ["G", "G", "G", "G", "G"],
        ]
        self.assertEqual(
            flood_fill(
                num_rows, num_columns, matrix, start_row, start_column, new_color
            ),
            expected_matrix,
        )

    def test_flood_fill_boundary(self):
        num_rows, num_columns = 3, 3
        start_row, start_column = 1, 1
        new_color = "B"
        matrix = [["B", "B", "B"], ["B", "G", "B"], ["B", "B", "B"]]
        expected_matrix = [["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]]

        self.assertEqual(
            flood_fill(
                num_rows, num_columns, matrix, start_row, start_column, new_color
            ),
            expected_matrix,
        )

    def test_with_files(self):
        input_file = "resources/flood_fill_test_1_input.txt"
        output_file = "resources/flood_fill_test_1_output.txt"
        num_rows, num_columns, start_row, start_column, new_color, matrix = read_input(
            input_file
        )
        flood_fill(num_rows, num_columns, matrix, start_row, start_column, new_color)
        write_output(matrix, output_file)
        with open(output_file, "r") as file:
            matrix = []
            for line in file:
                row = list(line.strip().split())
                matrix.append(row)

        self.assertEqual(
            flood_fill(
                num_rows, num_columns, matrix, start_row, start_column, new_color
            ),
            matrix,
        )


if __name__ == "__main__":
    unittest.main()
