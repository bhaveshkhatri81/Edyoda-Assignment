# In an array, Count Pairs with given sum

def count_pairs_with_sum(arr, target_sum):
    element_freq = {}
    count = 0

    for num in arr:
        difference = target_sum - num

        if difference in element_freq:
            count += element_freq[difference]

        if num in element_freq:
            element_freq[num] += 1
        else:
            element_freq[num] = 1

    return count

# Example Usage
arr = [1, 2, 3, 4, 5, 6]
target_sum = 7
result = count_pairs_with_sum(arr, target_sum)
print(f"The number of pairs with sum {target_sum} is: {result}")
