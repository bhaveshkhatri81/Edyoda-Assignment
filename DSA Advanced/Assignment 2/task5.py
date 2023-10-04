# Write a program to sort list of strings (similar to that of dictionary)

def sort_strings_descending(input_list):
    sorted_list = sorted(input_list, reverse=True)
    return sorted_list

# Example usage
my_list = ["apple", "banana", "cherry", "date", "grape"]
sorted_list_descending = sort_strings_descending(my_list)

print(sorted_list_descending)
