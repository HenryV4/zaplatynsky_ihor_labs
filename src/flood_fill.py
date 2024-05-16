def flood_fill(num_rows, num_colomns, matrix, start_row, start_column, new_color):
    old_color = matrix[start_row][start_column]
    if old_color == new_color:
        return matrix

    new_matrix = [(start_row, start_column)]

    while new_matrix:
        row, column = new_matrix.pop()
        matrix[row][column] = new_color

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for delta_row, delta_column in directions:
            neighbor_row = row + delta_row
            neighbor_column = column + delta_column

            if (
                0 <= neighbor_row < num_rows
                and 0 <= neighbor_column < num_colomns
                and matrix[neighbor_row][neighbor_column] == old_color
            ):
                new_matrix.append((neighbor_row, neighbor_column))
    return matrix


def read_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

        num_rows, num_columns = map(int, lines[0].strip().split(","))
        start_row, start_column = map(int, lines[1].strip().split(","))
        new_color = lines[2].strip().strip("'")

        matrix = []
        for line in lines[3:]:
            row_data = line.strip().strip("[],").replace("'", "").split(", ")
            matrix.append(row_data)

    return num_rows, num_columns, start_row, start_column, new_color, matrix


def write_output(matrix, file_name):
    with open(file_name, "w") as file:
        for row in matrix:
            file.write(", ".join(row) + "\n")
