import json

def rotate(self, matrix):
    n = len(matrix)
    start = 0
    end = n - 1

    while start < end:
        for i in range(end - start):
            # Top-left element
            temp = matrix[start][start + i]

            # Top-left element becomes top-right
            matrix[start][start + i] = matrix[end - i][start]

            # Top-right element becomes bottom-right
            matrix[end - i][start] = matrix[end][end - i]

            # Bottom-right element becomes bottom-left
            matrix[end][end - i] = matrix[start + i][end]

            # Bottom-left element becomes top-left
            matrix[start + i][end] = temp

        start += 1
        end -= 1

    return json.dumps(matrix)
