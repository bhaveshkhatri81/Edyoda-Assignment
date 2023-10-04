# Find the Kth largest and Kth smallest number in an array

def kth_largest_smallest(nums, k):
    nums.sort()
    kth_largest = nums[-k]
    kth_smallest = nums[k-1]
    return kth_largest, kth_smallest


nums = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3
kth_largest, kth_smallest = kth_largest_smallest(nums, k)
print(f"The {k}th largest number is: {kth_largest}")
print(f"The {k}th smallest number is: {kth_smallest}")
