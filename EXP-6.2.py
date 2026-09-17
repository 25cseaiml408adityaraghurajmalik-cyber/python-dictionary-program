def matrix_sum(matrix):
    print("Matrix with row sums:")

    for i in range(3):
        print(matrix[i], "=", sum(matrix[i]))

    print("\nColumn sums:")

    for j in range(3):
        total = 0
        for i in range(3):
            total += matrix[i][j]

        print("Column", j + 1, "=", total)


matrix = []

print("Enter 3 rows:")

for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

matrix_sum(matrix)
