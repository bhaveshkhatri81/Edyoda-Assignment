# Define a function to triple a number
def triple_number(num):
    return num * 3

sample_list = [1, 2, 3, 4, 5, 6, 7]

result_list = list(map(triple_number, sample_list))

print("Sample list:", sample_list)
print("Triple of list numbers:", result_list)
