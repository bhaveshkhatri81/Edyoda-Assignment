# 1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num

        if complement in seen:
            pairs.append((num, complement))

        seen.add(num)

    return pairs

# Example 
arr = [1, 2, 3, 4, 5, 6]
target_sum = 7

result = find_pairs_with_sum(arr, target_sum)

if result:
    print(f"Pairs with sum {target_sum}: {result}")
else:
    print(f"No pairs found with sum {target_sum}")
