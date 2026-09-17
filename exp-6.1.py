import random

def group_similar(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Store all elements
    elements = []

    for i in range(rows):
        for j in range(cols):
            elements.append(matrix[i][j])

    # Sort elements so similar elements come together
    elements.sort()

    # Create a new matrix
    new_matrix = []

    k = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(elements[k])
            k += 1
        new_matrix.append(row)

    return new_matrix


# Input matrix size
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

# Generate random matrix
matrix = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(random.randint(1, 5))
    matrix.append(row)

# Print original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Call function
result = group_similar(matrix)

# Print grouped matrix
print("\nMatrix with similar elements grouped:")
for row in result:
    print(row)
3