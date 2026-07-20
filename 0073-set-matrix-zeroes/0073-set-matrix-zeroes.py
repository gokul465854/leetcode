class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row = False
        first_col = False

        # Check first row
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row = True
                break

        # Check first column
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col = True
                break

        # Mark rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeros based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero first row
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero first column
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0