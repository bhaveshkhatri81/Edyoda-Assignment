def square(x):
    return x ** 2

sample_list = [4, 5, 2, 9]

result = list(map(square, sample_list))

print("Square the elements of the list:", result)
