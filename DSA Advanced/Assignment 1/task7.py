# Move all the negative elements to one side of the array

def move_negative_elements(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1

# Example usage:
arr = [1, -2, 3, -4, 5, -6]
move_negative_elements(arr)
print(arr)
