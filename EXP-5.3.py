def remove_duplicates(d):
    new_dict = {}

    for key, value in d.items():
        if value not in new_dict.values():
            new_dict[key] = value

    return new_dict


# Enter a dictionary
d = eval(input("Enter a dictionary: "))

# Remove duplicate values
result = remove_duplicates(d)

print("Dictionary after removing duplicate values:", result)
