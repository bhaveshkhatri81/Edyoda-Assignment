# Implement Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    my_list = [12, 11, 13, 5, 6, 7]
    sorted_list = quick_sort(my_list)
    print(sorted_list)
