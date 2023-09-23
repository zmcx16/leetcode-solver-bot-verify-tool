def setZeroes(self, matrix):
    rows = set()
    cols = set()

    # Find the rows and columns that contain zeros
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Set the corresponding rows and columns to zeros
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0

    return matrix