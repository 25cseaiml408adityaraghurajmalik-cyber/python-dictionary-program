def max_value_key(d):
    return max(d, key=d.get)

# Create a dictionary
d = eval(input("Enter a dictionary: "))

# Find the key with maximum value
key = max_value_key(d)

print("Key having maximum value:", key)
print("Maximum value:", d[key])
