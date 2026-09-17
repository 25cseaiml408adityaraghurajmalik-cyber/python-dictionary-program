# Enter list
lst = list(map(int, input("Enter list elements: ").split()))

# Enter value to search
value = int(input("Enter value to search: "))

# Lambda function
check = lambda x: x in lst

# Check the value
if check(value):
    print("Value is present in the list")
else:
    print("Value is not present in the list")
