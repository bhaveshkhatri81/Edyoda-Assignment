
tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


tuple_list.sort(key=lambda x: x[-1])


print("Sorted List:", tuple_list)
