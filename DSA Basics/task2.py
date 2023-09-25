# 2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example
my_array = [1, 2, 3, 4, 5]
print("Original array:", my_array)

reverse_array(my_array)

print("Reversed array:", my_array)
