def merge_dict(d1, d2):
    d1.update(d2)
    return d1

# Input two dictionaries
dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))

# Merge the dictionaries
result = merge_dict(dict1, dict2)

# Display the merged dictionary
print("Merged dictionary:", result)
