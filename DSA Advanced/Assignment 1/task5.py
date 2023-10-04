# Find duplicates in an array

def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Example usage
my_array = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
duplicates = find_duplicates(my_array)
print("Duplicates:", duplicates)
