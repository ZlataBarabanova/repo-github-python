class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        string = ''
        for row in self.matrix_data:
            for el in row:
                string += str(el) + ' '
            string += '\n'
        return string

    def __add__(self, other):
        new_matrix_data = []
        for row_count in range(len(self.matrix_data)):
            row = []
            for el_count in range(len(self.matrix_data[row_count])):
                row.append(self.matrix_data[row_count][el_count] +
                              other.matrix_data[row_count][el_count])
            new_matrix_data.append(row)
        return Matrix(new_matrix_data)


m1 = Matrix([[-2, 2, 3], [1, 8, 3], [1, 2, 3]])
m2 = Matrix([[3, 4, 3], [3, 2, 3], [3, 2, 5]])
print(m1)
print(m2)
print(m1 + m2)