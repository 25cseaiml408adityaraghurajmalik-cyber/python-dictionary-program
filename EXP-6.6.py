# Input two arrays
a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

# Lambda function
intersection = list(filter(lambda x: x in b, a))

# Print result
print("Intersection of two arrays:", intersection)
