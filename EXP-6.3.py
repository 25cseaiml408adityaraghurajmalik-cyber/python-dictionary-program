def transpose(matrix, n):
    print("\nTranspose of the matrix:")

    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=" ")
        print()


n = int(input("Enter the order of matrix: "))

matrix = []

print("Enter the matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(*row)

transpose(matrix, n)
